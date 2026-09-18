---
name: "supabase"
description: "Use Supabase when the user asks for Supabase or this provider's API."
---

# Supabase

## Purpose
Use Supabase with the user-connected `custom.supabase` credential.

## Tooling
`bin/mcp-call` — JSON-RPC client for the hosted Supabase MCP server
(Streamable HTTP). Always scope with `project_ref`, `read_only=true`, and
the smallest `features=` group the task needs:

```
mcp-call --params "read_only=true&features=account" tools
mcp-call --params "read_only=true&features=account" call list_projects
mcp-call --params "project_ref=<ref>&read_only=true&features=database" \
    call execute_sql --args '{"query": "select 1"}'
```

`bin/dump-schema` — read-only full-schema dump into an idempotent baseline
migration SQL file (project ref via `--project-ref` or `SUPABASE_PROJECT_REF`):

```
dump-schema --project-ref <ref> --out baseline_production_schema.sql
```

Python CLIs attach credentials through `bin/cred.py`: `from cred import add_surrogate_to_request, read_json_response`. On the original runtime this uses the secure vault (single-use surrogate values, attached per the connector's placement). Anywhere else, set `MIT_SKILLS_CUSTOM_SUPABASE` and the value is sent as `Authorization: Bearer`. Authenticated requests must only go to the hosts below.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, reconnect or replace the credential in your vault. The connector is named `custom.supabase` (env fallback: `MIT_SKILLS_CUSTOM_SUPABASE`).

## Operating Rules
1. Use this skill when the user asks for Supabase or this provider's API.
2. Restrict authenticated requests to: mcp.supabase.com.
3. Default to read-only: always pass `read_only=true`, scope with
   `project_ref`, and enable only the `features=` groups the task needs.
   Never use `apply_migration` or any write path without the user's explicit
   approval for that exact change.
4. Do not print, log, or persist raw credentials.
5. If auth is missing or rejected, follow the Auth section rather than asking for a key.
