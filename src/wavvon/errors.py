from __future__ import annotations


class WavvonError(Exception):
    """Base class: every error this SDK raises on purpose is one of these."""


class UnsupportedByHubError(WavvonError):
    """The hub does not advertise a capability the call needs. Never a version check."""

    def __init__(self, capability: str) -> None:
        super().__init__(f'this hub does not advertise the "{capability}" capability')
        self.capability = capability


class HubUnavailableError(WavvonError):
    """The hub could not be reached or kept saying "not now" (429, 5xx, timeout,
    network) until the retry budget ran out. This is not an answer: the request
    may succeed later, and nothing about the resource can be concluded from it."""

    def __init__(self, message: str, last_status: int | None = None) -> None:
        super().__init__(message)
        self.last_status = last_status


class HubError(WavvonError):
    """A definitive refusal from the hub (4xx other than 429)."""

    def __init__(self, status: int, body: str) -> None:
        super().__init__(f"hub answered {status}: {body}")
        self.status = status
        self.body = body


class AuthSchemeError(WavvonError):
    """The challenge could not be answered safely (missing or unknown scheme)."""


class ReplayUnavailableError(WavvonError):
    """A poll cursor is older than the hub's 72-hour window: events after it
    were missed and cannot be replayed. Resynchronise from REST, then poll
    without a cursor."""

    def __init__(self, earliest_seq: int, earliest_at: int) -> None:
        super().__init__(f"events before seq {earliest_seq} are outside the hub's replay window")
        self.earliest_seq = earliest_seq
        self.earliest_at = earliest_at


class WebhookVerificationError(WavvonError):
    """A webhook request failed verification; answer it with 401 and do nothing."""
