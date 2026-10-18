"""Boots a real hub binary with a fresh database, sets it up as its owner (a
role carrying apps.register, an invite granting it, a channel), then runs
tests/smoke.py against it. Mirrors Wavvon-server's e2e harness.

    WAVVON_HUB_BIN        hub binary (default ../../server/target/debug/wavvon-hub[.exe])
    WAVVON_PG             PostgreSQL base URL (default postgres://postgres:postgres@localhost:5432)
    WAVVON_PG_CONTAINER   docker container used to create the database (default wavvon-pg)

Needs a running PostgreSQL. Does not build the hub. The binary is copied into
a temp directory first, so the running hub never locks the build output.
"""

from __future__ import annotations

import asyncio
import os
import random
import secrets
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

import httpx

from wavvon import WavvonClient, ok
from wavvon.rest.api.channels import create_channel
from wavvon.rest.api.invites import create_invite
from wavvon.rest.api.roles import create_role
from wavvon.rest.models.create_channel_body import CreateChannelBody
from wavvon.rest.models.create_invite_body import CreateInviteBody
from wavvon.rest.models.create_role_body import CreateRoleBody

ROOT = Path(__file__).resolve().parent.parent
EXE = "wavvon-hub.exe" if sys.platform == "win32" else "wavvon-hub"
DB = "wavvon_sdk_py_smoke"


def psql(container: str, sql: str) -> None:
    subprocess.run(["docker", "exec", container, "psql", "-U", "postgres", "-c", sql], check=True, capture_output=True)


async def setup(hub_url: str, owner: WavvonClient, hub: subprocess.Popen[bytes]) -> dict[str, Any]:
    deadline = time.monotonic() + 90
    async with httpx.AsyncClient() as http:
        while True:
            if hub.poll() is not None:
                raise RuntimeError(f"hub exited ({hub.returncode})")
            try:
                if (await http.get(f"{hub_url}/info")).status_code == 200:
                    break
            except httpx.TransportError:
                pass
            if time.monotonic() > deadline:
                raise RuntimeError("hub never answered")
            await asyncio.sleep(0.4)
    print(f"smoke-local: hub up at {hub_url}", flush=True)

    role_body = CreateRoleBody(name="Apps", priority=10, permissions=["apps.register"])
    role = ok(await create_role.asyncio_detailed(client=owner.rest, body=role_body))
    invite_body = CreateInviteBody(grant_role_id=role.id, max_uses=1)
    invite = ok(await create_invite.asyncio_detailed(client=owner.rest, body=invite_body))
    channel = ok(await create_channel.asyncio_detailed(client=owner.rest, body=CreateChannelBody(name="sdk-smoke")))
    print("smoke-local: role, invite and channel ready", flush=True)
    await owner.aclose()
    return {"invite": invite.code, "channel": channel.id}


def main() -> int:
    src = Path(os.environ.get("WAVVON_HUB_BIN") or ROOT / "../../server/target/debug" / EXE).resolve()
    if not src.exists():
        print(f"no hub binary at {src}; build Wavvon-server (cargo build -p wavvon-hub) or set WAVVON_HUB_BIN")
        return 2
    pg = os.environ.get("WAVVON_PG", "postgres://postgres:postgres@localhost:5432")
    container = os.environ.get("WAVVON_PG_CONTAINER", "wavvon-pg")
    psql(container, f"DROP DATABASE IF EXISTS {DB}")
    psql(container, f"CREATE DATABASE {DB}")

    port = 3900 + random.randrange(500)
    hub_url = f"http://localhost:{port}"
    cwd = Path(tempfile.mkdtemp(prefix="wavvon-sdk-py-smoke-"))
    binary = cwd / EXE
    shutil.copy2(src, binary)
    owner = WavvonClient(hub_url, seed=secrets.token_bytes(32))
    log_path = cwd / "hub.log"
    env = {
        **os.environ,
        "WAVVON_DATABASE_URL": f"{pg}/{DB}",
        # The bot's webhook receiver listens on localhost.
        "WAVVON_ALLOW_PRIVATE_WEBHOOKS": "true",
        "WAVVON_HTTP_PORT": str(port),
        "WAVVON_VOICE_UDP_PORT": str(port + 1),
        "WAVVON_PUBLIC_URL": hub_url,
        "WAVVON_OWNER_PUBKEY": owner.identity.public_key,
        "WAVVON_WEB_CLIENT_DIR": "",
    }
    with log_path.open("wb") as log:
        hub = subprocess.Popen([str(binary)], cwd=cwd, env=env, stdout=log, stderr=subprocess.STDOUT)
    code = 1
    try:
        made = asyncio.run(setup(hub_url, owner, hub))
        smoke_env = {
            **os.environ,
            "WAVVON_SMOKE_HUB": hub_url,
            "WAVVON_SMOKE_INVITE": made["invite"],
            "WAVVON_SMOKE_CHANNEL": made["channel"],
        }
        code = subprocess.run([sys.executable, str(ROOT / "tests" / "smoke.py")], env=smoke_env).returncode
        if code != 0 and os.environ.get("WAVVON_SMOKE_VERBOSE"):
            print(log_path.read_text("utf-8", "replace"))
    except Exception as e:
        print(f"smoke-local: {e!r}\n{log_path.read_text('utf-8', 'replace')}", file=sys.stderr)
    finally:
        if sys.platform == "win32":
            subprocess.run(["taskkill", "/PID", str(hub.pid), "/T", "/F"], capture_output=True)
        else:
            hub.kill()
        hub.wait()
        shutil.rmtree(cwd, ignore_errors=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
