"""A minimal WebTransport client over aioquic's HTTP/3: an extended CONNECT,
then HTTP/3 datagrams bound to that stream. Voice needs nothing else.

The hub's wtransport 0.7 speaks WebTransport draft-02 only
(SETTINGS_ENABLE_WEBTRANSPORT 0x2b603742, `Sec-Webtransport-Http3-Draft02`),
which is what aioquic's `enable_webtransport` sends and expects, so no
WebTransport library is involved: newer-draft clients refuse the hub
(Wavvon-server#417)."""

from __future__ import annotations

import asyncio
import hashlib
import hmac
import ssl
from contextlib import AsyncExitStack
from typing import Any, cast
from urllib.parse import urlsplit

from aioquic.asyncio.client import connect as quic_connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.h3.connection import H3Connection
from aioquic.h3.events import DatagramReceived, H3Event, HeadersReceived
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import ConnectionTerminated, QuicEvent
from cryptography.hazmat.primitives.serialization import Encoding

KEEPALIVE_SECONDS = 5.0
CONNECT_TIMEOUT = 15.0


class WebTransportError(Exception):
    """The WebTransport session could not be set up, or ended."""


class _Protocol(QuicConnectionProtocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.h3 = H3Connection(self._quic, enable_webtransport=True)
        self.stream_id = -1
        self.status: asyncio.Future[int] = asyncio.get_running_loop().create_future()
        self.datagrams: asyncio.Queue[bytes | None] = asyncio.Queue()

    def quic_event_received(self, event: QuicEvent) -> None:
        if isinstance(event, ConnectionTerminated):
            if not self.status.done():
                self.status.set_exception(
                    WebTransportError(f"connection closed: {event.reason_phrase or event.error_code}")
                )
            self.datagrams.put_nowait(None)
        for h3_event in self.h3.handle_event(event):
            self._h3_event(h3_event)

    def _h3_event(self, event: H3Event) -> None:
        if isinstance(event, HeadersReceived) and event.stream_id == self.stream_id:
            status = dict(event.headers).get(b":status", b"0")
            if not self.status.done():
                self.status.set_result(int(status))
        elif isinstance(event, DatagramReceived) and event.stream_id == self.stream_id:
            self.datagrams.put_nowait(event.data)


class WebTransportSession:
    """Datagrams over one CONNECT stream. Build with `WebTransportSession.connect`."""

    def __init__(self, stack: AsyncExitStack, proto: _Protocol) -> None:
        self._stack = stack
        self._proto = proto
        self._keepalive = asyncio.get_running_loop().create_task(self._ping())
        self._closed = False

    @classmethod
    async def connect(cls, url: str, cert_hash: str | None = None) -> WebTransportSession:
        """`url` carries the token already. A non-empty `cert_hash` (hex SHA-256) pins
        the hub's leaf certificate and is the only case where system verification
        is off."""
        parts = urlsplit(url)
        if parts.hostname is None:
            raise WebTransportError(f"not a WebTransport URL: {url}")
        want = b""
        if cert_hash:
            try:
                want = bytes.fromhex(cert_hash)
            except ValueError:
                want = b""
            if len(want) != hashlib.sha256().digest_size:
                raise WebTransportError("voice_cert_hash is not a SHA-256 digest")
        config = QuicConfiguration(
            is_client=True,
            alpn_protocols=["h3"],
            max_datagram_frame_size=65536,
            verify_mode=ssl.CERT_NONE if want else ssl.CERT_REQUIRED,
        )
        stack = AsyncExitStack()
        try:
            proto = cast(
                _Protocol,
                await asyncio.wait_for(
                    stack.enter_async_context(
                        quic_connect(parts.hostname, parts.port or 443, configuration=config, create_protocol=_Protocol)
                    ),
                    CONNECT_TIMEOUT,
                ),
            )
            if want:
                chain = proto._quic.tls.peer_certificates
                if not chain:
                    raise WebTransportError("the hub presented no certificate")
                got = hashlib.sha256(chain[0].public_bytes(Encoding.DER)).digest()
                if not hmac.compare_digest(got, want):
                    raise WebTransportError("the hub certificate does not match voice_cert_hash")
            proto.stream_id = proto._quic.get_next_available_stream_id()
            authority = parts.netloc.encode()
            proto.h3.send_headers(
                stream_id=proto.stream_id,
                headers=[
                    (b":method", b"CONNECT"),
                    (b":scheme", b"https"),
                    (b":authority", authority),
                    (b":path", (parts.path or "/").encode() + (b"?" + parts.query.encode() if parts.query else b"")),
                    (b":protocol", b"webtransport"),
                    (b"sec-webtransport-http3-draft02", b"1"),
                ],
            )
            proto.transmit()
            status = await asyncio.wait_for(proto.status, CONNECT_TIMEOUT)
            if not 200 <= status <= 299:
                raise WebTransportError(f"the hub answered the WebTransport CONNECT with {status}")
        except BaseException:
            await stack.aclose()
            raise
        return cls(stack, proto)

    def send_datagram(self, data: bytes) -> None:
        if self._closed:
            raise WebTransportError("session closed")
        self._proto.h3.send_datagram(self._proto.stream_id, data)
        self._proto.transmit()

    async def receive_datagram(self) -> bytes:
        """The next datagram; raises WebTransportError once the session is gone."""
        got = await self._proto.datagrams.get()
        if got is None:
            self._proto.datagrams.put_nowait(None)
            raise WebTransportError("session closed")
        return got

    async def _ping(self) -> None:
        # Idle listeners send nothing; a QUIC PING keeps the path and the idle timer alive.
        try:
            while True:
                await asyncio.sleep(KEEPALIVE_SECONDS)
                await self._proto.ping()
        except Exception:
            pass

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._keepalive.cancel()
        self._proto.datagrams.put_nowait(None)
        await self._stack.aclose()
