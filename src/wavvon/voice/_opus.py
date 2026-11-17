"""The one thing the SDK checks about an Opus packet: that it is exactly 20 ms.
The desktop decoder's output buffer holds 20 ms, so a 40 or 60 ms packet fails
to decode on every desktop listener (sdk-voice.md section 3). PCM encode and
decode are an optional extra (`pip install wavvon-sdk[opus]`, which needs the
libopus shared library)."""

from __future__ import annotations

from array import array
from collections.abc import Sequence
from typing import Any

FRAME_SAMPLES = 960
SAMPLE_RATE = 48000


def opus_duration_micros(packet: bytes) -> int:
    """Duration of a packet in microseconds, from its TOC byte (RFC 6716 section 3.1)."""
    if not packet:
        raise ValueError("empty packet")
    toc = packet[0]
    config = toc >> 3
    if config <= 11:
        frame = (10_000, 20_000, 40_000, 60_000)[config % 4]
    elif config <= 15:
        frame = (10_000, 20_000)[config % 2]
    else:
        frame = (2_500, 5_000, 10_000, 20_000)[config % 4]
    code = toc & 3
    if code == 0:
        frames = 1
    elif code in (1, 2):
        frames = 2
    else:
        if len(packet) < 2:
            raise ValueError("code-3 packet without a frame count")
        frames = packet[1] & 0x3F
    if frames == 0:
        raise ValueError("packet declares zero frames")
    return frame * frames


def check_20ms(packet: bytes) -> None:
    """Raises ValueError unless the packet is exactly 20 ms."""
    us = opus_duration_micros(packet)
    if us != 20_000:
        raise ValueError(f"{us / 1000:g} ms")


class OpusCodec:
    """Encoder for this program's own speech and one decoder per remote sender."""

    def __init__(self, *, music: bool = False, bitrate: int | None = None) -> None:
        try:
            import opuslib
        except Exception as e:  # ImportError, or opuslib raising when libopus is absent
            raise RuntimeError("PCM needs `pip install wavvon-sdk[opus]` and the libopus shared library") from e
        self._lib: Any = opuslib
        app = opuslib.APPLICATION_AUDIO if music else opuslib.APPLICATION_VOIP
        self._enc = opuslib.Encoder(SAMPLE_RATE, 1, app)
        if bitrate:
            self._enc.bitrate = bitrate
        self._dec: dict[int, Any] = {}

    def encode(self, pcm: Sequence[float]) -> bytes:
        frame = array("f", pcm)
        return bytes(self._enc.encode_float(frame.tobytes(), FRAME_SAMPLES))

    def decode(self, sender: int, opus: bytes) -> array[float]:
        dec = self._dec.get(sender)
        if dec is None:
            dec = self._dec[sender] = self._lib.Decoder(SAMPLE_RATE, 1)
        out: array[float] = array("f")
        out.frombytes(dec.decode_float(opus, FRAME_SAMPLES))
        return out
