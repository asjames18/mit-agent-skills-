#!/usr/bin/env python3
"""Deploy a prebuilt Cloudflare Worker.

Builds nothing; deploys a prebuilt worker directory via
`npx nitro deploy --prebuilt`.
Auth: uses the stored custom.cloudflare credential. The credential value is
handed to the child process only via CLOUDFLARE_API_TOKEN and is never
printed or logged.
"""
from __future__ import annotations

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cred import dynamic_credential_entry  # noqa: E402

SITE_DIR = os.environ.get("CLOUDFLARE_SITE_DIR") or os.path.expanduser("~/workspace/melanatedintech-site")


def main() -> int:
    try:
        entry = dynamic_credential_entry("custom.cloudflare", "access_token")
    except Exception as exc:  # noqa: BLE001
        print(f"error: could not load Cloudflare credential: {exc}", file=sys.stderr)
        return 2
    surrogate = entry["surrogate"]

    env = dict(os.environ)
    env["CLOUDFLARE_API_TOKEN"] = surrogate

    proc = subprocess.run(
        ["npx", "nitro", "deploy", "--prebuilt"],
        cwd=SITE_DIR,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=600,
    )
    output = proc.stdout.replace(surrogate, "[redacted]")
    print(output)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
