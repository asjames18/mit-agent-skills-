---
name: "elevenlabs"
description: "Use Elevenlabs when the user asks for Elevenlabs or this provider's API."
---

# Elevenlabs

## Purpose
Use Elevenlabs with the user-connected `custom.elevenlabs` credential.

## Tooling
Add service-specific CLIs under `bin/`.

Python CLIs attach credentials through `bin/cred.py`: `from cred import add_surrogate_to_request, read_json_response`. On the original runtime this uses the secure vault (single-use surrogate values, attached per the connector's placement). Anywhere else, set `MIT_SKILLS_CUSTOM_ELEVENLABS` and the value is sent as `Authorization: Bearer`. Authenticated requests must only go to the hosts below.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, reconnect or replace the credential in your vault. The connector is named `custom.elevenlabs` (env fallback: `MIT_SKILLS_CUSTOM_ELEVENLABS`).

## Operating Rules
1. Use this skill when the user asks for Elevenlabs or this provider's API.
2. Restrict authenticated requests to: api.elevenlabs.io.
3. Do not print, log, or persist raw credentials.
4. If auth is missing or rejected, follow the Auth section rather than asking for a key.
