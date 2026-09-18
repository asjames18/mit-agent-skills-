# Melanated in Tech Agent Skills

Open-source, portable workflows for AI agents doing practical work with evidence, clear authority boundaries, and reusable outputs.

## Skill catalog

| Skill | Purpose | Version |
| --- | --- | --- |
| [`governed-social-content`](skills/governed-social-content/SKILL.md) | Research, evaluate, create platform-native drafts, approve, and learn from social content without treating preparation as permission to publish. | 0.2.0 |
| [`tiered-technical-product-review`](skills/tiered-technical-product-review/SKILL.md) | Produce a source-backed adopt, test, defer, or reject brief for a technical product, AI tool, vendor, or implementation option without treating research as permission to act. | 0.1.0 |
| [`cloudflare`](skills/cloudflare/SKILL.md) | Call the Cloudflare API and deploy prebuilt workers, with portable credential attachment. | 1.0.0 |
| [`elevenlabs`](skills/elevenlabs/SKILL.md) | ElevenLabs text-to-speech CLI: list voices and synthesize speech to MP3. | 1.0.0 |
| [`github`](skills/github/SKILL.md) | Call the GitHub REST API with scoped, credential-brokered auth. | 1.0.0 |
| [`notion`](skills/notion/SKILL.md) | Notion CLI: search, read pages, query databases, append and update content. | 1.0.0 |
| [`supabase`](skills/supabase/SKILL.md) | Supabase helpers: hosted MCP JSON-RPC client and a read-only production schema dump. | 1.0.0 |
| [`threads-post`](skills/threads-post/SKILL.md) | Publish and reply on Threads via Meta's Threads API with an approval-gated posting queue. | 1.0.0 |
| [`copyright-guard`](skills/copyright-guard/SKILL.md) | Pre-publish screen for copyright-risk patterns in drafts: long quotes, lyrics, copyrighted Bible translations, unattributed quotes, unlicensed images. Heuristic screen, not legal clearance. | 0.1.0 |

## Repository model

- **GitHub is canonical.** Skill instructions, supporting references, versions, and review history live here.
- **Knowledge systems are discovery layers.** Notion and similar tools may publish agent-facing copies that link back to a tagged version or commit.
- **A separate private skills repository supplies personal context.** Voice profiles, account configuration, private evidence, internal project details, and personalized overlays do not belong in this public repository.

## Public and private repositories

The public repository contains reusable base Skills. A separate private repository may copy or depend on a pinned public version, then add private overlays for a person, organization, brand, account, or project.

Keep the private repository independent rather than using a workflow that can accidentally merge private history into public. Moving an improvement from private to public requires a new sanitized change in the public repository, followed by privacy review, validation, staged-diff inspection, and secret scanning.

## Using a skill

Open the skill's `SKILL.md` and give it to an agent that supports file-based instructions, or copy the skill folder into that platform's supported skills directory. Read only the supporting references routed by the entrypoint.

Skills do not grant external authority. A skill that prepares a draft, approval packet, deployment plan, or message does not itself authorize the external action.

## Authentication

Skills with `bin/` CLIs attach credentials through a small `bin/cred.py` shim
included in each skill. On the original runtime it uses the secure vault
(single-use surrogate values, requests restricted to the skill's documented
hosts). Anywhere else, set `MIT_SKILLS_<CONNECTOR>` — the connector name
uppercased with dots and dashes converted to underscores (for example,
`MIT_SKILLS_CUSTOM_GITHUB`) — and the value is sent as
`Authorization: Bearer`. Never commit a real credential; the `.gitignore`
excludes common secret files, and CI runs the structural validator on every
push.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Public contributions must satisfy the privacy and security requirements in [AGENTS.md](AGENTS.md) and [SECURITY.md](SECURITY.md).

Validate all skills locally with:

```bash
python scripts/validate_skills.py
```

## License

Released under the [MIT License](LICENSE).
