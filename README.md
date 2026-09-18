# Melanated in Tech Agent Skills

Open-source, portable workflows for AI agents doing practical work with evidence, clear authority boundaries, and reusable outputs.

## Skill catalog

| Skill | Purpose | Version |
| --- | --- | --- |
| [`governed-social-content`](skills/governed-social-content/SKILL.md) | Research, evaluate, draft, approve, and learn from social content without treating preparation as permission to publish. | 0.1.0 |

## Repository model

- **GitHub is canonical.** Skill instructions, supporting references, versions, and review history live here.
- **Knowledge systems are discovery layers.** Notion and similar tools may publish agent-facing copies that link back to a tagged version or commit.
- **Project repositories supply private context.** Brand rules, account configuration, internal evidence, and implementation details do not belong in this public repository.

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
