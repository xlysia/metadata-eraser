#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def remove_metadata(input_path: Path, output_path: Path) -> None:
    with Image.open(input_path) as image:
        normalized = ImageOps.exif_transpose(image)
        cleaned = Image.frombytes(
            normalized.mode, normalized.size, normalized.tobytes()
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        cleaned.save(output_path, format=image.format)


def build_output_path(input_path: Path, output_dir: Path) -> Path:
    return output_dir / f"{input_path.stem}_clean{input_path.suffix}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove metadata from one or more image files."
    )
    parser.add_argument("images", nargs="+", type=Path, help="Input image files")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("."),
        help="Directory for cleaned images (default: current directory)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    for image_path in args.images:
        if not image_path.is_file():
            raise FileNotFoundError(f"Image not found: {image_path}")

        output_path = build_output_path(image_path, args.output_dir)
        remove_metadata(image_path, output_path)
        print(f"Cleaned {image_path} -> {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
