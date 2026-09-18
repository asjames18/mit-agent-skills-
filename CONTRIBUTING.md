# Contributing

Contributions should improve a repeatable agent workflow rather than preserve a one-off answer.

## Add or update a skill

1. Create or update `skills/<skill-name>/SKILL.md`.
2. Keep discovery metadata concise and specific.
3. Put conditional procedures, schemas, and detailed checks in `references/`.
4. Add the skill or new version to `registry.yaml` and the catalog in `README.md`.
5. Remove private context and replace real identifiers with neutral placeholders.
6. Validate links, frontmatter, behavior, and authority boundaries.
7. Inspect the staged diff and run a secret scan before pushing.

Run the repository validator before opening a pull request:

```bash
python scripts/validate_skills.py
```

## Quality bar

A useful skill changes an agent's decisions, improves reliability, or preserves a non-obvious invariant. Avoid generic advice, duplicated documentation, large prompt dumps, speculative edge cases, and rules that do not apply outside one private project.

## Versioning

Use semantic versions per skill:

- Patch: clarification with no meaningful behavior change
- Minor: new workflow capability or compatible output field
- Major: incompatible routing, authority, or output changes

Record released versions in `registry.yaml`. A knowledge-system copy should identify the exact version or commit it mirrors.
