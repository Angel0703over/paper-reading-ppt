#!/usr/bin/env python3
"""Extract plain text from a PDF for paper-reading workflows.

Usage:
    python extract_pdf_text.py input.pdf output.txt

Requires one of: pypdf, PyPDF2.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _load_reader():
    try:
        from pypdf import PdfReader  # type: ignore

        return PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader  # type: ignore

            return PdfReader
        except ImportError as exc:
            raise SystemExit(
                "Missing dependency: install pypdf or PyPDF2 to extract PDF text."
            ) from exc


def extract_text(pdf_path: Path) -> str:
    PdfReader = _load_reader()
    reader = PdfReader(str(pdf_path))
    chunks: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        chunks.append(f"\n\n===== Page {index} =====\n{text.strip()}")
    return "\n".join(chunks).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    if not args.pdf.exists():
        parser.error(f"PDF not found: {args.pdf}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(extract_text(args.pdf), encoding="utf-8")
    print(f"Wrote text to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
