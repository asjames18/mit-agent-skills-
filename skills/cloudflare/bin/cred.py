"""Portable credential attachment for this skill's CLIs.

Two modes:
1. Platform mode: if the `dynamic_credentials` broker is importable, credentials
   come from the secure vault as single-use surrogates, attached per the
   connector's placement. Nothing secret touches disk or env.
2. Env fallback: anywhere else, set MIT_SKILLS_<CONNECTOR> (connector name
   uppercased with dots/dashes converted to underscores, e.g.
   MIT_SKILLS_CUSTOM_GITHUB) and the value is attached as
   `Authorization: Bearer <value>`.

Mirrors the broker subset this skill uses, so CLIs import from here instead of
the platform-specific module:
    from cred import add_surrogate_to_request, read_json_response
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse

_PLATFORM_BIN = "/opt/hatch/skills/skill-creator/bin"


class CredentialError(RuntimeError):
    """Raised when no usable credential is available."""


# Backwards-compatible alias for the platform broker's exception name.
DynamicCredentialError = CredentialError


def env_name(connector: str) -> str:
    """Env var holding the raw credential outside the original runtime."""
    return "MIT_SKILLS_" + re.sub(r"[^A-Z0-9]", "_", connector.upper())


def ensure_allowed_url(url: str, allowed_hosts) -> None:
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    allowed = {h.strip().lower() for h in allowed_hosts if h and h.strip()}
    if not host or host not in allowed:
        raise CredentialError(
            f"refusing authenticated request to {host or '<missing host>'}; "
            f"allowed hosts: {', '.join(sorted(allowed)) or '<none>'}"
        )


def _platform_module():
    if _PLATFORM_BIN not in sys.path:
        sys.path.insert(0, _PLATFORM_BIN)
    import dynamic_credentials

    return dynamic_credentials


def add_surrogate_to_request(request, connector: str, *, entry_name: str = "access_token",
                             allowed_hosts=()) -> None:
    """Attach a credential to a urllib request: vault surrogate or env Bearer."""
    ensure_allowed_url(request.full_url, allowed_hosts)
    try:
        dc = _platform_module()
    except ImportError:
        token = os.environ.get(env_name(connector))
        if not token:
            raise CredentialError(
                f"no credential broker found; set {env_name(connector)} to use "
                f"the '{connector}' credential outside the original runtime"
            )
        request.add_header("Authorization", f"Bearer {token}")
        return
    dc.add_surrogate_to_request(request, connector, entry_name=entry_name,
                                allowed_hosts=allowed_hosts)


def dynamic_credential_entry(connector: str, entry_name: str = "access_token") -> dict:
    """Return one credential entry: vault surrogate or env value."""
    try:
        dc = _platform_module()
    except ImportError:
        token = os.environ.get(env_name(connector))
        if not token:
            raise CredentialError(
                f"no credential broker found; set {env_name(connector)}"
            )
        return {"name": entry_name, "surrogate": token}
    return dc.dynamic_credential_entry(connector, entry_name)


def read_response_body(response, chunk_size: int = 65536) -> bytes:
    """Read an HTTP response without requiring Content-Length to be exact."""
    chunks = []
    while True:
        block = response.read(chunk_size)
        if not block:
            break
        chunks.append(block)
    return b"".join(chunks)


def read_json_response(response) -> dict:
    """Read an HTTP response body and parse it as JSON."""
    return json.loads(read_response_body(response).decode("utf-8"))
