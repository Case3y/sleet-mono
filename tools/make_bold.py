#!/usr/bin/env python3
"""Build a Bold cut of Sleet Mono from the Regular.

  python tools/make_bold.py

Every stem is grown by 2 * GROW units, the same thing
font.changeWeight(2 * GROW, "LCG", 0, 0, "squish") does in FontForge.
"""

import pathops
from fontTools.ttLib import TTFont
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

SRC = "fonts/SleetMono-Regular.ttf"
OUT = "build/SleetMono-Bold.ttf"
FAMILY = "Sleet Mono"
PSNAME = "SleetMono-Bold"

GROW = 15.0        # outward offset per side; stems gain 2 * GROW
SB_MIN = 4         # keep at least this much sidebearing
ADVANCE = 600

CAP, JOIN = pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN


def embolden(p, amount):
    """Dilate the outline by `amount`, keeping the contours unioned."""
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

    return pathops.op(ink, ring, pathops.PathOp.UNION)


def clamp(p, amount):
    x0, _, x1, _ = p.bounds
    return max(0.0, min(amount, x0 - SB_MIN, ADVANCE - SB_MIN - x1))


def set_bold_metadata(font):
    for nameID, value in {1: FAMILY, 2: "Bold", 4: FAMILY, 6: PSNAME,
                          16: FAMILY, 17: "Bold"}.items():
        font["name"].setName(value, nameID, 3, 1, 0x409)
        font["name"].setName(value, nameID, 1, 0, 0)

    os2 = font["OS/2"]
    os2.usWeightClass = 700
    os2.fsSelection = (os2.fsSelection & ~0x40) | 0x20
    os2.panose.bFamilyType = 2
    os2.panose.bLetterForm = 11
    os2.panose.bProportion = 9
    os2.panose.bContrast = 4
    os2.panose.bStrokeVariation = 5
    os2.panose.bArmStyle = 5
    os2.panose.bXHeight = 4
    font["head"].macStyle |= 1


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
            embolden(p, clamp(p, GROW)).draw(Cu2QuPen(pen, 0.4, reverse_direction=True))
            glyf[name] = pen.glyph()
            glyf[name].recalcBounds(glyf)

        font["hmtx"][name] = (adv, glyf[name].xMin if glyf[name].numberOfContours else 0)

    set_bold_metadata(font)
    font.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
