---
name: "threads-post"
description: "Publish and reply on Threads via Meta's Threads API: text/image posts, replies, reply moderation, quota checks, and an approval-gated posting queue."
---

# Threads Post

## Purpose
Publish posts and replies to the user's Threads account, moderate replies,
and run an approval-gated queue for scheduled/autopilot posting. Auth comes
from the connector `custom.threads` (OAuth2, scopes:
`threads_content_publish`, `threads_read_replies`, `threads_manage_replies`,
`threads_manage_insights`). On the original runtime the raw token never
touches disk, env, or logs; elsewhere set `MIT_SKILLS_CUSTOM_THREADS`.

## Tooling
`bin/threads-post` — Python client for `https://graph.threads.com/v1.0`.
Always sends a custom User-Agent. Credentials attach through `bin/cred.py`
(vault surrogate on the original runtime, `Authorization: Bearer` from
`MIT_SKILLS_CUSTOM_THREADS` elsewhere).

```
threads-post me                          # resolve the Threads user id
threads-post quota                       # posts/replies/deletes quota usage
threads-post post --text "..."           # publish a text post (two-step)
threads-post post --text "..." --reply-to <post-id>
threads-post post-image --image-url <public-url> [--text "..."]
threads-post replies --post-id <id>      # read replies on a post
threads-post hide-reply --reply-id <id>
threads-post unhide-reply --reply-id <id>
threads-post queue-add --text "..." [--not-before <ISO>]
threads-post queue-list
threads-post run-queue                    # publishes approved, due items only
```

Images must be publicly reachable URLs (Meta fetches them server-side).
Text posts are capped at 500 characters by the API.

## Auth
The credential is already stored; nothing here collects one. Never ask the
user to paste a raw token in chat.

Threads access tokens expire after ~60 days and must be renewed by the user
re-completing the vault capture flow (or refreshing `MIT_SKILLS_CUSTOM_THREADS`
outside the original runtime). If every call starts failing with auth
errors, the token likely expired — renew it before debugging further.
The connector is named `custom.threads`.

A 401/403 is a question about the request before it is about the token: check
the credential was attached and the scopes cover the call before blaming auth.

## Operating Rules
1. **Approval gate (standing rule).** Never publish a post or reply the user
   has not approved. The queue exists for this: draft with `queue-add`
   (`approved=false` by default), the user flips items to approved in batches,
   and `run-queue` publishes only approved, due, unposted items. Stops on the
   first failure rather than burning the queue.
2. **Autopilot scope.** Autopilot covers: (a) publishing the user's own queued
   content on schedule, and (b) replying to comments on the user's own posts.
   It does NOT cover cold replies on strangers' posts or mass outreach
   commenting — that is the fastest way to get the account flagged for spam,
   and it needs per-target approval.
3. **Reply guardrails.** When auto-replying on the user's own posts: never
   post duplicate text twice, keep it conversational and human, cap at ~10
   auto-replies per day, and skip anything that looks like abuse, scams, or
   harassment (hide those instead, with a note to the user).
4. **Rate awareness.** Check `quota` before bulk runs. API limits: 250 posts
   and 1,000 replies per rolling 24h.
5. Do not print, log, or persist raw credentials. Only the credential value
   leaves this machine, and only to `graph.threads.com`.
6. If the user asks for full autopilot including cold outreach commenting,
   restate the account-standing risk first and get explicit confirmation that
   they accept it before enabling.
