#!/usr/bin/env python3
"""Build a Bold Italic cut of Sleet Mono from the Bold.

  python tools/make_bold.py        # build/SleetMono-Bold.ttf
  python tools/make_bolditalic.py  # build/SleetMono-BoldItalic.ttf

The outlines are sheared by SLANT degrees about the middle of the
x-height, exactly like make_italic.py, but applied to the Bold cut.
Advance widths are left untouched, so the result stays monospaced.
"""

import math

from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

SRC = "fonts/SleetMono-Bold.ttf"
OUT = "build/SleetMono-BoldItalic.ttf"
FAMILY = "Sleet Mono"
PSNAME = "SleetMono-BoldItalic"
STYLE = "Bold Italic"

SLANT = 10.0     # degrees of forward lean
PIVOT = 275      # middle of the x-height (x-height is 550)


def shear_matrix():
    """Map (x, y) to (x + (y - PIVOT) * tan(SLANT), y)."""
    k = math.tan(math.radians(SLANT))
    return Transform(1, 0, k, 1, -k * PIVOT, 0), k


def set_bold_italic_metadata(font, k):
    for nameID, value in {1: FAMILY, 2: STYLE, 4: f"{FAMILY} {STYLE}",
                          6: PSNAME, 16: FAMILY, 17: STYLE}.items():
        font["name"].setName(value, nameID, 3, 1, 0x409)
        font["name"].setName(value, nameID, 1, 0, 0)

    os2 = font["OS/2"]
    os2.usWeightClass = 700
    os2.fsSelection = (os2.fsSelection & ~0x40) | 0x21   # bold + italic
    os2.panose.bLetterForm = 11
    font["head"].macStyle |= 3
    font["post"].italicAngle = -SLANT

    hhea = font["hhea"]
    hhea.caretSlopeRise = 1000
    hhea.caretSlopeRun = round(1000 * k)
    hhea.caretOffset = 0


def main():
    font = TTFont(SRC)
    gs = font.getGlyphSet()
    glyf = font["glyf"]
    xform, k = shear_matrix()

    for name in font.getGlyphOrder():
        p = gs[name]
        adv = font["hmtx"][name][0]

        if glyf[name].numberOfContours:
            pen = TTGlyphPen(None)
            p.draw(TransformPen(pen, xform))
            glyf[name] = pen.glyph()
            glyf[name].recalcBounds(glyf)

        font["hmtx"][name] = (adv, glyf[name].xMin if glyf[name].numberOfContours else 0)

    set_bold_italic_metadata(font, k)
    font.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
