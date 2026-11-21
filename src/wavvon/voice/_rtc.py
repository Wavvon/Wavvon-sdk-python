"""The voice transport (voice-transport-v3.md): one WebRTC data channel,
negotiated on stream 0, unordered, no retransmission. The hub is ICE-lite and
answers with its host candidates, so no STUN or TURN server is configured.
The room sees only send_datagram, receive_datagram and close."""

from __future__ import annotations

import asyncio

from aiortc import RTCDataChannel, RTCPeerConnection, RTCSessionDescription

OPEN_TIMEOUT = 10.0


class TransportError(Exception):
    """The voice data channel could not be set up, or ended."""


class RtcSession:
    """A peer with its voice channel. Build with `RtcSession.offer`, send the SDP
    as voice_rtc_offer, then `accept` the hub's answer."""

    def __init__(self, pc: RTCPeerConnection, channel: RTCDataChannel) -> None:
        self._pc = pc
        self._channel = channel
        self._inbox: asyncio.Queue[bytes | None] = asyncio.Queue()
        channel.on("message", self._on_message)
        channel.on("close", lambda: self._inbox.put_nowait(None))

        @pc.on("connectionstatechange")
        def _state() -> None:
            if pc.connectionState in ("failed", "closed"):
                self._inbox.put_nowait(None)

    def _on_message(self, data: bytes | str) -> None:
        if isinstance(data, bytes):
            self._inbox.put_nowait(data)

    @classmethod
    async def offer(cls) -> tuple[RtcSession, str]:
        pc = RTCPeerConnection()
        channel = pc.createDataChannel("voice", negotiated=True, id=0, ordered=False, maxRetransmits=0)
        s = cls(pc, channel)
        # aiortc gathers every candidate before setLocalDescription returns, so
        # the offer goes out whole: the hub has no trickle.
        await pc.setLocalDescription(await pc.createOffer())
        return s, pc.localDescription.sdp

    async def accept(self, answer: str) -> None:
        opened = asyncio.Event()
        self._channel.on("open", opened.set)
        try:
            await self._pc.setRemoteDescription(RTCSessionDescription(sdp=answer, type="answer"))
            if self._channel.readyState != "open":
                async with asyncio.timeout(OPEN_TIMEOUT):
                    await opened.wait()
        except (TimeoutError, ValueError) as e:
            await self.close()
            raise TransportError(f"voice data channel did not open: {e}") from e

    def send_datagram(self, data: bytes) -> None:
        if self._channel.readyState == "open":
            self._channel.send(data)

    async def receive_datagram(self) -> bytes:
        data = await self._inbox.get()
        if data is None:
            self._inbox.put_nowait(None)
            raise TransportError("voice data channel closed")
        return data

    async def close(self) -> None:
        await self._pc.close()
