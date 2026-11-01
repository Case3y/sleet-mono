#!/usr/bin/env python3
"""Build an Italic cut of Sleet Mono from the Regular.

  python tools/make_italic.py

The outlines are sheared by SLANT degrees about the middle of the
x-height.  Shearing about that line keeps lowercase centred in the
600-unit advance, while capitals and ascenders gain the usual forward
lean and descenders swing slightly left.  The advance width of every
glyph is left untouched, so the result stays strictly monospaced.
"""

import math

from fontTools.misc.transform import Transform
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

SRC = "fonts/SleetMono-Regular.ttf"
OUT = "build/SleetMono-Italic.ttf"
FAMILY = "Sleet Mono"
PSNAME = "SleetMono-Italic"
STYLE = "Italic"

SLANT = 10.0     # degrees of forward lean
PIVOT = 275      # middle of the x-height (x-height is 550)


def shear_matrix():
    """Map (x, y) to (x + (y - PIVOT) * tan(SLANT), y)."""
    k = math.tan(math.radians(SLANT))
    return Transform(1, 0, k, 1, -k * PIVOT, 0), k


def set_italic_metadata(font, k):
    for nameID, value in {1: FAMILY, 2: STYLE, 4: f"{FAMILY} {STYLE}",
                          6: PSNAME, 16: FAMILY, 17: STYLE}.items():
        font["name"].setName(value, nameID, 3, 1, 0x409)
        font["name"].setName(value, nameID, 1, 0, 0)

    os2 = font["OS/2"]
    os2.fsSelection = (os2.fsSelection & ~0x40) | 0x01
    os2.panose.bLetterForm = 9
    font["head"].macStyle |= 2
    font["post"].italicAngle = -SLANT

    # Caret follows the slant of the stems, like the italic of other
    # monospaced programming fonts.
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

    set_italic_metadata(font, k)
    font.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
