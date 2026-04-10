#!/usr/bin/env python3

from __future__ import annotations

import argparse
import math
import sys
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas

DEFAULT_TEXT = "© 江星 · 禁止转载传播 · 违者必究。"
DEFAULT_OUTPUT_DIRNAME = "waterprinted"
DEFAULT_GRAY = 0.78
DEFAULT_OPACITY = 0.24
DEFAULT_MIN_FONT_SIZE = 18.0
DEFAULT_MAX_FONT_SIZE = 64.0
DEFAULT_DIAGONAL_COVERAGE = 0.82
FONT_NAME = "STSong-Light"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply a diagonal watermark to one or more PDF files."
    )
    parser.add_argument("inputs", nargs="+", help="Input PDF files to watermark.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repo_root() / DEFAULT_OUTPUT_DIRNAME,
        help="Directory where watermarked PDFs are written. Default: %(default)s",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Explicit output file path. Only valid when one input PDF is provided.",
    )
    parser.add_argument(
        "--text",
        default=DEFAULT_TEXT,
        help="Watermark text. Default: %(default)s",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def register_font() -> None:
    try:
        pdfmetrics.getFont(FONT_NAME)
    except KeyError:
        pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))


def build_overlay(page_width: float, page_height: float, text: str):
    register_font()

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=(page_width, page_height))
    pdf.setFillColor(Color(DEFAULT_GRAY, DEFAULT_GRAY, DEFAULT_GRAY))
    if hasattr(pdf, "setFillAlpha"):
        pdf.setFillAlpha(DEFAULT_OPACITY)

    unit_width = pdfmetrics.stringWidth(text, FONT_NAME, 1)
    if unit_width <= 0:
        raise ValueError("Unable to measure watermark text width.")

    diagonal = math.hypot(page_width, page_height)
    font_size = diagonal * DEFAULT_DIAGONAL_COVERAGE / unit_width
    font_size = max(DEFAULT_MIN_FONT_SIZE, min(font_size, DEFAULT_MAX_FONT_SIZE))
    angle = -math.degrees(math.atan2(page_height, page_width))

    pdf.saveState()
    pdf.translate(page_width / 2, page_height / 2)
    pdf.rotate(angle)
    pdf.setFont(FONT_NAME, font_size)
    pdf.drawCentredString(0, -font_size * 0.3, text)
    pdf.restoreState()
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return PdfReader(buffer).pages[0]


def destination_for(input_path: Path, output_dir: Path, explicit_output: Path | None) -> Path:
    if explicit_output is not None:
        return explicit_output

    repo_output_dir = repo_root() / "output"
    resolved_input = input_path.resolve()

    try:
        relative_name = resolved_input.relative_to(repo_output_dir.resolve())
    except ValueError:
        relative_name = Path(input_path.name)

    return output_dir / relative_name


def watermark_pdf(source: Path, destination: Path, text: str) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Input PDF not found: {source}")

    if source.resolve() == destination.resolve():
        raise ValueError(f"Input and output paths must differ: {source}")

    reader = PdfReader(str(source))
    writer = PdfWriter()

    overlay_cache: dict[tuple[float, float], object] = {}
    for page in reader.pages:
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)
        cache_key = (page_width, page_height)
        overlay = overlay_cache.get(cache_key)
        if overlay is None:
            overlay = build_overlay(page_width, page_height, text)
            overlay_cache[cache_key] = overlay

        page.merge_page(overlay)
        writer.add_page(page)

    if reader.metadata:
        metadata = {
            key: value
            for key, value in reader.metadata.items()
            if isinstance(key, str) and isinstance(value, str)
        }
        if metadata:
            writer.add_metadata(metadata)

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as handle:
        writer.write(handle)


def main() -> int:
    args = parse_args()
    inputs = [Path(item).resolve() for item in args.inputs]

    if args.output is not None and len(inputs) != 1:
        print("--output can only be used with a single input PDF.", file=sys.stderr)
        return 2

    exit_code = 0
    for input_path in inputs:
        destination = destination_for(input_path, args.output_dir.resolve(), args.output)
        try:
            watermark_pdf(input_path, destination, args.text)
            print(f"{input_path} -> {destination}")
        except Exception as exc:  # noqa: BLE001
            exit_code = 1
            print(f"Failed to watermark {input_path}: {exc}", file=sys.stderr)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
