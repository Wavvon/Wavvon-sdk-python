from __future__ import annotations

import math

import pytest

from wavvon.voice._opus import FRAME_SAMPLES, OpusCodec, check_20ms


def test_pcm_roundtrip() -> None:
    try:
        codec = OpusCodec(bitrate=32000)
    except RuntimeError:
        pytest.skip("the opus extra or the libopus shared library is not available")
    tone = [0.3 * math.sin(2 * math.pi * 440 * n / 48000) for n in range(FRAME_SAMPLES)]
    for _ in range(5):  # the encoder needs a few frames to converge
        packet = codec.encode(tone)
    check_20ms(packet)
    for _ in range(3):
        out = codec.decode(1, packet)
    assert len(out) == FRAME_SAMPLES
    assert sum(x * x for x in out) / FRAME_SAMPLES > 1e-3
