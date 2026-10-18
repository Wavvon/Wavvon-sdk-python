# CLAUDE.md

Guidance for working in this repo: `wavvon-sdk` (import `wavvon`), the Python
SDK for programs (bots and apps) that talk to a Wavvon hub. The design is
[sdk.md](https://github.com/Wavvon/Wavvon-docs/blob/main/docs/sdk.md); this is
its tier 1. The TypeScript SDK
([Wavvon-sdk-js](https://github.com/Wavvon/Wavvon-sdk-js)) is the reference
for surface and behaviour; this one mirrors it idiomatically. Hub code lives in
[Wavvon-server](https://github.com/Wavvon/Wavvon-server), the REST spec and
protocol docs in [Wavvon-docs](https://github.com/Wavvon/Wavvon-docs).

## Commands

```sh
python -m venv .venv && .venv/bin/pip install -e . --group dev   # .venv\Scripts on Windows
python scripts/check          # ruff check + ruff format --check + mypy --strict + pytest. Must pass before a commit.
python -m pytest -q           # tests only
python scripts/generate.py [<path-to-Wavvon-docs>] [--ref <git-ref>]   # regenerate src/wavvon/rest
python scripts/smoke_local.py # real hub binary, see below
```

Code comments in English, only where the why is not obvious. No comments in
GitHub Actions workflow files: explain choices in the commit message.

## Layers

1. **Generated REST** - `src/wavvon/rest/`, from Wavvon-docs `openapi.yaml`
   by `scripts/generate.py` (openapi-python-client, pinned in the dev group).
   Committed; never edit by hand. `SPEC_COMMIT` records the docs commit:
   `-dirty` means local edits, `+refnull` means the script wrapped a
   `{$ref, nullable: true}` in `anyOf` (OpenAPI 3.0 ignores `$ref` siblings, so
   the model would reject the hub's `null`). Excluded from ruff and from mypy
   errors.
2. **Hand-written core** - `src/wavvon/`:
   `auth.py` challenge rules and login; `retry.py` backoff; `client.py`
   `WavvonClient` (the generated client over an httpx transport that adds the
   bearer, retries and re-authenticates on 401), capabilities, app
   registration, polling, `ok()`; `pager.py`; `events.py` the WebSocket stream
   and frame TypedDicts; `webhooks.py` dispatch and outgoing-webhook
   verification, reply TypedDicts, the framework-agnostic handler and `to_asgi`.
3. **Conformance** - `tests/test_conformance.py` reads Wavvon-server
   `crates/identity/wire-vectors.json` (default `../../server/...` relative
   to the working directory, or `WAVVON_WIRE_VECTORS`). Strings starting with
   `@` refer to `fixtures`. Never copied into this repo. Missing file: loud
   skip locally, failure when `CI` is set.

## Rules the SDK must keep (sdk.md §5, §6)

- **Capabilities, never versions.** Gate features on `GET /info`
  `capabilities` and raise `UnsupportedByHubError`. Never compare `version`.
- **429 is "not now", never "no".** Retry 429/5xx/timeouts/transport errors
  with capped exponential backoff and jitter. On exhaustion raise
  `HubUnavailableError`; never turn a transient failure into an empty list,
  "not found", or any other definitive answer. A pager page that fails must
  raise, not end the list. Only transport errors and timeouts are retried;
  a programming error propagates.
- **Unknown is loud.** Unknown socket frames and dispatch types are delivered
  as an `unknown` variant with the raw payload, never dropped. `info()`
  returns the hub's JSON rather than a generated model because generated enums
  raise on a value they do not know.
- **Re-auth on its own**, with the state observable (`on_state_change`).
- **Auth challenge**: `scheme: "tagged-v1"` -> sign
  `"wavvon/auth-challenge/v1\0" || challenge`; no scheme -> raw only at exactly
  32 bytes; unknown scheme -> error.
- **Never send the seed** or any private key anywhere. Never invent a wire
  format: signed bytes come from wire-format.md and the vectors; a new one is
  a server-side change first. Never model a bot as an account or send
  `is_bot`. Tier 1 is community-axis only (no DMs E2E, pairing, home hub).

Code is authoritative over docs. When they disagree, follow the hub code and
report the doc bug to Wavvon-docs.

## Facts verified against the hub that the docs get wrong or omit

- The challenge is hex. The hub removes a pending challenge when verify reads
  it, so a transient verify failure restarts from a fresh challenge.
- `resume` and `hub_event` push only work on a socket whose identity had an
  app profile **when it connected** (`is_app` is read at connect). Register
  first, then `connect()`. Replay can re-deliver: drop `seq <= last`.
- The app side of a mini-app sends `app_announce` / `app_dismiss` and talks to
  players with `mini_app_message` + `to_pubkey`. `app_join` is answered by the
  hub, not the app.
- Paging: a bare array plus `limit` (default 100, max 500) and `cursor` = key
  of the previous page's last row; the key differs per endpoint (`code`,
  `public_key`, `id`). Channel messages still page with `before`.
- Outgoing-webhook HKDF input is the **decoded** secret bytes (the admin sees
  base64url without padding); the HMAC key is the 32 HKDF bytes, not hex.
- `GET /me/events` rows are never written by the hub today
  (Wavvon-server#170); `poll_events` follows the spec and nothing relies on it.

## Smoke test

`tests/smoke.py` runs against a real hub (`WAVVON_SMOKE_HUB`,
`WAVVON_SMOKE_INVITE` for an invite whose role grants `apps.register`,
optional `WAVVON_SMOKE_CHANNEL`). `scripts/smoke_local.py` copies a hub binary
(`WAVVON_HUB_BIN`, default a sibling Wavvon-server checkout's
`target/debug/wavvon-hub`) into a temp directory, boots it on a fresh database
in a PostgreSQL docker container (`WAVVON_PG_CONTAINER`, default `wavvon-pg`),
sets up a role, invite and channel as owner, runs the smoke, and kills only
the hub it started. In-process tests have missed every cross-process bug this
project has had: run it when touching auth, the socket or webhooks.

## Git

Work on `develop`; `main` is for releases. Commit in logical steps.
