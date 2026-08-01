#!/usr/bin/env python3
"""Generate original, trademark-neutral PNG icons for 5tratStore recipes."""

from pathlib import Path
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]


def base(colour: tuple[int, int, int]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGBA", (512, 512), (10, 14, 24, 255))
    draw = ImageDraw.Draw(image)
    for radius, alpha in ((220, 35), (175, 55), (130, 80)):
        layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
        halo = ImageDraw.Draw(layer)
        halo.ellipse(
            (256 - radius, 256 - radius, 256 + radius, 256 + radius),
            fill=(*colour, alpha),
        )
        image.alpha_composite(layer)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((42, 42, 470, 470), radius=92, outline=(*colour, 230), width=12)
    return image, draw


def uptime() -> Image.Image:
    image, draw = base((38, 214, 129))
    draw.line((105, 275, 185, 275, 220, 190, 275, 340, 315, 245, 405, 245), fill=(225, 255, 244), width=24, joint="curve")
    draw.ellipse((88, 258, 118, 288), fill=(38, 214, 129))
    draw.ellipse((392, 228, 422, 258), fill=(38, 214, 129))
    return image


def prometheus() -> Image.Image:
    image, draw = base((255, 123, 50))
    draw.line((105, 360, 105, 135), fill=(225, 235, 249), width=12)
    draw.line((105, 360, 410, 360), fill=(225, 235, 249), width=12)
    points = [(120, 325), (175, 280), (225, 305), (285, 195), (335, 230), (400, 135)]
    draw.line(points, fill=(255, 164, 85), width=24, joint="curve")
    for x, y in points:
        draw.ellipse((x - 14, y - 14, x + 14, y + 14), fill=(255, 240, 220))
    return image


def main() -> None:
    outputs = {
        ROOT / "uptime-kuma" / "icon.png": uptime(),
        ROOT / "prometheus" / "icon.png": prometheus(),
    }
    for path, image in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        image.save(path, "PNG", optimize=True)
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
