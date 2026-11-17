from __future__ import annotations

from enum import StrEnum


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


class RecipientHasNoKeyError(WavvonError):
    """A peer has published no DH key on this hub, so nothing can be encrypted
    or wrapped to it. Never sent in the clear instead."""

    def __init__(self, public_key: str) -> None:
        super().__init__(f"{public_key} has published no DH key on this hub")
        self.public_key = public_key


class DhKeyChangedError(WavvonError):
    """A peer's DH key differs from the one pinned on first use. Nothing is
    encrypted to it until the program calls `accept_dh_key`."""

    def __init__(self, public_key: str, pinned: str, fetched: str) -> None:
        super().__init__(f"DH key of {public_key} changed (pinned {pinned}, hub now has {fetched})")
        self.public_key = public_key
        self.pinned = pinned
        self.fetched = fetched


class DhKeyUnsignedError(WavvonError):
    """The hub holds a DH record for `public_key` that it did not sign. The hub
    is not trusted with it."""

    def __init__(self, public_key: str) -> None:
        super().__init__(f"DH key record for {public_key} is not signed by its owner")
        self.public_key = public_key


class DmErrorReason(StrEnum):
    NOT_SIGNED_BY_SENDER = "not_signed_by_sender"
    """The envelope is not signed by the member the hub names as its sender, directly or via a cert."""
    OWN_MESSAGE = "own_message"
    """A ratchet cannot read what it sent itself; keeping a copy is the program's business."""
    MALFORMED = "malformed"
    DECRYPTION_FAILED = "decryption_failed"
    NO_SESSION = "no_session"
    TOO_MANY_SKIPPED = "too_many_skipped"
    KEY_NOT_FOUND = "key_not_found"
    """No sender key from that member at that version."""
    CHAIN_ADVANCED = "chain_advanced"
    """The sender's chain was already advanced past this message."""


class DmError(WavvonError):
    """Why one DM could not be read or sent. Per message: a program keeps going."""

    def __init__(self, reason: DmErrorReason, detail: str = "") -> None:
        super().__init__(f"{reason.value}: {detail}" if detail else reason.value)
        self.reason = reason
        self.detail = detail
