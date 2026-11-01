#!/usr/bin/env python3
"""Build a Thin cut of Sleet Mono from the Regular.

  python tools/make_thin.py

Every stem is shaved by 2 * SHRINK units, the exact inverse of the dilation
make_bold.py applies: the band swept by each contour is subtracted from the
glyph instead of added to it.
"""

import pathops
from fontTools.ttLib import TTFont
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

SRC = "fonts/SleetMono-Regular.ttf"
OUT = "build/SleetMono-Thin.ttf"
FAMILY = "Sleet Mono"
PSNAME = "SleetMono-Thin"
STYLE = "Thin"

SHRINK = 1.0      # inward offset per side; stems lose 2 * SHRINK

CAP, JOIN = pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN


def thin(p, amount):
    """Erode the outline by `amount`, keeping the contours unioned."""
    ink = pathops.Path()
    p.draw(ink.getPen())
    ink.fillType = pathops.FillType.WINDING

    ring = pathops.Path()
    for c in p.contours:
        q = pathops.Path()
        c.draw(q.getPen())
        q.stroke(2 * amount, CAP, JOIN, 4)
        q.convertConicsToQuads(0.1)
        ring = pathops.op(ring, q, pathops.PathOp.UNION) if ring.verbs else q

    return pathops.op(ink, ring, pathops.PathOp.DIFFERENCE)


def set_thin_metadata(font):
    # Thin is outside the RIBBI four, so it becomes its own family name and
    # nameID 16/17 carry the real family/style pair.
    for nameID, value in {1: f"{FAMILY} {STYLE}", 2: "Regular",
                          4: f"{FAMILY} {STYLE}", 6: PSNAME,
                          16: FAMILY, 17: STYLE}.items():
        font["name"].setName(value, nameID, 3, 1, 0x409)
        font["name"].setName(value, nameID, 1, 0, 0)

    os2 = font["OS/2"]
    os2.usWeightClass = 100
    os2.fsSelection = (os2.fsSelection & ~0x20) | 0x40
    os2.panose.bFamilyType = 2
    os2.panose.bLetterForm = 11
    os2.panose.bProportion = 9
    os2.panose.bWeight = 2
    os2.panose.bContrast = 3
    os2.panose.bStrokeVariation = 3
    os2.panose.bArmStyle = 2
    os2.panose.bXHeight = 4
    font["head"].macStyle &= ~1


def main():
    font = TTFont(SRC)
    gs = font.getGlyphSet()
    glyf = font["glyf"]

    for name in font.getGlyphOrder():
        p = pathops.Path()
        gs[name].draw(p.getPen())
        adv = font["hmtx"][name][0]

        if p.verbs:
            pen = TTGlyphPen(None)
            thin(p, SHRINK).draw(Cu2QuPen(pen, 0.4, reverse_direction=True))
            glyf[name] = pen.glyph()
            glyf[name].recalcBounds(glyf)

        font["hmtx"][name] = (adv, glyf[name].xMin if glyf[name].numberOfContours else 0)

    set_thin_metadata(font)
    font.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
