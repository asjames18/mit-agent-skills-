#!/usr/bin/env python3
"""Validate the portable structure and public boundary of repository skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FORBIDDEN_PATTERNS = {
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\", re.IGNORECASE),
    "Unix home path": re.compile(r"/(?:home|Users)/[^/\s]+/", re.IGNORECASE),
    "Notion private page link": re.compile(r"https?://(?:www\.)?(?:notion\.so|app\.notion\.com)/", re.IGNORECASE),
    "GitHub token": re.compile(r"\bgh[opusr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "PEM private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[INSERT .+?\]", re.IGNORECASE)


def parse_frontmatter(text: str, skill_file: Path) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{skill_file}: missing YAML frontmatter")

    try:
        frontmatter, _body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError(f"{skill_file}: unclosed YAML frontmatter") from exc

    name_match = re.search(r"^name:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not name_match or not description_match:
        raise ValueError(f"{skill_file}: frontmatter requires name and description")

    return name_match.group(1).strip(" '\""), description_match.group(1).strip(" '\"")


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    try:
        name, description = parse_frontmatter(text, skill_file)
    except ValueError as exc:
        return [str(exc)]

    if name != skill_dir.name:
        errors.append(f"{skill_file}: name '{name}' must match folder '{skill_dir.name}'")
    if not NAME_PATTERN.fullmatch(name) or len(name) > 63:
        errors.append(f"{skill_file}: name must be lowercase hyphenated text under 64 characters")
    if len(description) < 30:
        errors.append(f"{skill_file}: description is too short to route reliably")

    for markdown_file in sorted(skill_dir.rglob("*.md")):
        markdown = markdown_file.read_text(encoding="utf-8")
        if PLACEHOLDER_PATTERN.search(markdown):
            errors.append(f"{markdown_file}: contains an unfinished placeholder")

        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(markdown):
                errors.append(f"{markdown_file}: contains {label}")

        for target in MARKDOWN_LINK_PATTERN.findall(markdown):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = target.split("#", 1)[0]
            if relative_target and not (markdown_file.parent / relative_target).resolve().is_file():
                errors.append(f"{markdown_file}: broken local link '{target}'")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("No skills directory found.", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("No skills found.", file=sys.stderr)
        return 1

    errors = [error for skill_dir in skill_dirs for error in validate_skill(skill_dir)]
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
