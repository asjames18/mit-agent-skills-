# Melanated in Tech Agent Skills

Open-source, portable workflows for AI agents doing practical work with evidence, clear authority boundaries, and reusable outputs.

## Skill catalog

| Skill | Purpose | Version |
| --- | --- | --- |
| [`governed-social-content`](skills/governed-social-content/SKILL.md) | Research, evaluate, create platform-native drafts, approve, and learn from social content without treating preparation as permission to publish. | 0.2.0 |

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Public contributions must satisfy the privacy and security requirements in [AGENTS.md](AGENTS.md) and [SECURITY.md](SECURITY.md).

Validate all skills locally with:

```bash
python scripts/validate_skills.py
```

## License

Released under the [MIT License](LICENSE).
