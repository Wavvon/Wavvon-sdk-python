from __future__ import annotations

import json

import httpx
import pytest

from wavvon import HubUnavailableError, RetryOptions, SessionState, UnsupportedByHubError, WavvonClient, ok
from wavvon.rest.api.channels import list_channels

SEED = "02" * 32
FAST = RetryOptions(base_delay=0.001, max_delay=0.001)


class FakeHub:
    """A hub with a token that can be revoked mid-run and a flaky /channels."""

    def __init__(self, capabilities: list[str]) -> None:
        self.capabilities = capabilities
        self.tokens = 0
        self.valid = ""
        self.flaky = 0
        self.log: list[str] = []
        self.events: list[dict[str, object]] = []
        self.transport = httpx.MockTransport(self.handle)

    def handle(self, req: httpx.Request) -> httpx.Response:
        path = req.url.path
        self.log.append(f"{req.method} {path}")
        if path == "/info":
            return httpx.Response(200, json={"public_key": "aa", "capabilities": self.capabilities})
        if path == "/auth/challenge":
            return httpx.Response(200, json={"challenge": "00" * 32, "scheme": "tagged-v1"})
        if path == "/auth/verify":
            self.tokens += 1
            self.valid = f"t{self.tokens}"
            return httpx.Response(200, json={"token": self.valid, "scope": "member", "canonical_pubkey": "me"})
        if req.headers.get("authorization") != f"Bearer {self.valid}":
            return httpx.Response(401, text="expired")
        if path == "/channels" and self.flaky > 0:
            self.flaky -= 1
            return httpx.Response(429)
        if path == "/me/app/commands":
            return httpx.Response(200)
        if path == "/me/events":
            return httpx.Response(200, json={"events": self.events})
        return httpx.Response(200, json=[{"id": "c1", "name": "general"}])

    def client(self, retry: RetryOptions = FAST) -> WavvonClient:
        return WavvonClient("http://hub", seed=SEED, retry=retry, transport=self.transport)


async def test_adds_the_bearer_and_reauthenticates_once_on_401() -> None:
    hub = FakeHub([])
    states: list[SessionState] = []
    async with hub.client() as client:
        client.on_state_change(states.append)
        channels = ok(await list_channels.asyncio_detailed(client=client.rest))
        assert [c.name for c in channels] == ["general"]
        hub.valid = "revoked"
        assert (await list_channels.asyncio_detailed(client=client.rest)).status_code == 200
    assert hub.log.count("POST /auth/verify") == 2
    assert states == ["authenticating", "ready", "authenticating", "ready"]


async def test_retries_429_and_fails_loudly_once_the_budget_is_spent() -> None:
    hub = FakeHub([])
    async with hub.client(RetryOptions(base_delay=0.001, max_delay=0.001, max_attempts=3)) as client:
        hub.flaky = 2
        assert (await list_channels.asyncio_detailed(client=client.rest)).status_code == 200
        hub.flaky = 10
        with pytest.raises(HubUnavailableError):
            await list_channels.asyncio_detailed(client=client.rest)


async def test_gates_app_registration_on_apps_register() -> None:
    async with FakeHub([]).client() as without:
        with pytest.raises(UnsupportedByHubError):
            await without.set_app_commands([])
    hub = FakeHub(["apps.register"])
    async with hub.client() as client:
        await client.set_app_commands([{"name": "echo", "description": "Echo"}])
    assert "PUT /me/app/commands" in hub.log


async def test_polls_and_parses_payloads() -> None:
    hub = FakeHub([])
    hub.events = [{"id": "e1", "event_type": "slash_command", "payload": json.dumps({"x": 1}), "created_at": 5}]
    async with hub.client() as client:
        got = await client.poll_events(since=3)
    assert got[0].payload == {"x": 1}
    assert "GET /me/events" in hub.log
