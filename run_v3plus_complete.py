#!/usr/bin/env python3
"""Full V3+ pipeline test driver."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from PIL import Image, ImageDraw  # noqa: E402

from app.pipeline import Pipeline  # noqa: E402


def make_owl(path: Path) -> Path:
    """Synthetic owl if no sample photo is present."""
    img = Image.new("RGB", (640, 800), (28, 42, 58))
    d = ImageDraw.Draw(img)
    d.ellipse((160, 180, 480, 620), fill=(92, 64, 38))
    d.ellipse((200, 220, 340, 360), fill=(240, 230, 200))
    d.ellipse((300, 220, 440, 360), fill=(240, 230, 200))
    d.ellipse((240, 260, 300, 320), fill=(40, 90, 140))
    d.ellipse((340, 260, 400, 320), fill=(40, 90, 140))
    d.ellipse((255, 275, 285, 305), fill=(10, 10, 10))
    d.ellipse((355, 275, 385, 305), fill=(10, 10, 10))
    d.polygon([(300, 340), (340, 400), (280, 400)], fill=(220, 140, 40))
    d.polygon([(240, 580), (200, 760), (280, 620)], fill=(70, 48, 28))
    d.polygon([(400, 580), (440, 760), (360, 620)], fill=(70, 48, 28))
    d.ellipse((80, 80, 200, 160), fill=(180, 40, 50))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


def main() -> int:
    sample = ROOT / "samples" / "owl.png"
    if not sample.exists():
        make_owl(sample)
    out = ROOT / "output"
    pipe = Pipeline(out)
    result = pipe.run(sample, title="Midnight Owl", width=64, max_colors=28, aida=14)
    print("FOLDER", result.folder)
    print(result.qa_text)
    print("FILES")
    for f in result.files:
        print(" -", f, f.stat().st_size if f.exists() else 0)
    print("OK", result.pattern.width, "x", result.pattern.height, "colors", result.pattern.color_count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
