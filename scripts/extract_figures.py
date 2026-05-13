#!/usr/bin/env python3
"""Extract embedded images from a PDF into a directory.

Usage:
    python extract_figures.py input.pdf output_dir

Requires PyMuPDF:
    pip install pymupdf
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def extract_images(pdf_path: Path, output_dir: Path) -> int:
    try:
        import fitz  # type: ignore
    except ImportError as exc:
        raise SystemExit("Missing dependency: install pymupdf to extract figures.") from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    count = 0
    for page_index in range(len(doc)):
        page = doc[page_index]
        for image_index, image in enumerate(page.get_images(full=True), start=1):
            xref = image[0]
            base = doc.extract_image(xref)
            ext = base.get("ext", "png")
            data = base["image"]
            count += 1
            name = f"page-{page_index + 1:03d}_image-{image_index:02d}.{ext}"
            (output_dir / name).write_bytes(data)
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract embedded images from a PDF.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    if not args.pdf.exists():
        parser.error(f"PDF not found: {args.pdf}")

    count = extract_images(args.pdf, args.output_dir)
    print(f"Extracted {count} image(s) to {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
