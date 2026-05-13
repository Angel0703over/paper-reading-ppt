#!/usr/bin/env python3
"""Check Markdown slide drafts for overly dense bullets.

Usage:
    python check_slide_density.py slides.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)$")
BULLET_RE = re.compile(r"^\s*[-*]\s+(.+)$")


def check_density(path: Path, max_bullets: int, max_chars: int) -> int:
    current = "Document"
    counts: dict[str, int] = {}
    issues: list[str] = []

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        heading = HEADING_RE.match(line)
        if heading:
            current = heading.group(2).strip()
            counts.setdefault(current, 0)
            continue

        bullet = BULLET_RE.match(line)
        if not bullet:
            continue

        counts[current] = counts.get(current, 0) + 1
        content = bullet.group(1).strip()
        if len(content) > max_chars:
            issues.append(
                f"{path}:{line_number}: bullet is {len(content)} chars, "
                f"above limit {max_chars}"
            )

    for heading, count in counts.items():
        if count > max_bullets:
            issues.append(f"{heading}: {count} bullets, above limit {max_bullets}")

    if issues:
        print("\n".join(issues))
        return 1

    print("Slide density check passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Check slide bullet density.")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--max-bullets", type=int, default=5)
    parser.add_argument("--max-chars", type=int, default=80)
    args = parser.parse_args()

    if not args.markdown.exists():
        parser.error(f"Markdown file not found: {args.markdown}")

    return check_density(args.markdown, args.max_bullets, args.max_chars)


if __name__ == "__main__":
    sys.exit(main())
