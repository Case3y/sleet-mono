# Sleet Mono Roadmap

The long-term goal is coverage parity with
[JetBrains Mono](https://github.com/JetBrains/JetBrainsMono): **4 styles**,
**1,372 mapped codepoints** and **153 ligatures**.

Today Sleet Mono has 1 style, 103 codepoints and no OpenType layout tables, so
1,269 codepoints are still missing.

> The counts below were computed by diffing the `cmap` tables of
> `JetBrainsMono-Regular.ttf` and `SleetMono-Regular.ttf`. They will drift as
> glyphs are added; regenerate them rather than editing by hand.

## Milestones

| Milestone | Scope |
| --- | --- |
| M1 | Regular, Bold, Italic, Bold Italic at the current 103-glyph charset |
| M2 | Complete the GF Latin Kernel set referenced in the Fontra project (17 glyphs short today) |
| M3 | Latin-1 Supplement, Latin Extended-A/B, typography punctuation, currency |
| M4 | Coding symbols: arrows, math, box drawing, block elements, control pictures |
| M5 | Greek and Cyrillic |
| M6 | Remaining JetBrains Mono blocks (APL, double-struck, dingbats, Nerd Font extras) |

## Weights and styles

- [ ] **Bold** — redraw the stems rather than emboldening Regular; JetBrains Mono
      Bold is redrawn (`l` widens from 520 to 532 units, `I` from 390 to 420)
- [ ] **Italic** — a true italic, not a mechanical slant: redesign `a`, `e`, `f`,
      `g`, `i`, `l` and friends, then apply the −9° slant
- [ ] **Bold Italic**
- [ ] Keep the 600-unit advance width and the vertical metrics (ascender 1020,
      descender −300, x-height 550, cap height 730) identical in every style
- [ ] Per-style `name` table, `usWeightClass` (400 for Regular/Italic; for Bold,
      either 700 or JetBrains Mono's 558), `fsSelection`, `macStyle`,
      `italicAngle` and unique ID
- [ ] Optional, later: a variable font build

## Glyph coverage

Counts below are the codepoints JetBrains Mono has that Sleet Mono does not. The
tiers add up to the 1,214 codepoints that fall in named Unicode blocks; the other
55 are listed under Tier 6.

### Tier 1 — Western European text (95 glyphs)

- [ ] Latin-1 Supplement (95 of the 96 in the block; JetBrains Mono skips the
      soft hyphen `U+00AD`): `¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º »
      ¼ ½ ¾ ¿`, plus all accented capitals and lowercase (`À Á Â Ã Ä Å Æ Ç È … ÿ`)

### Tier 2 — Typography and extended Latin (234 glyphs)

- [ ] General Punctuation (28): `‐ – — ‖ ‚ ‛ „ ‟ † ‡ • ․ … ‰ ′ ″ ‴ ‹ › ‼ ‽ ‾ ‿
      ⁄ ⁅ ⁆` and the space characters `U+2001`, `U+200B`
- [ ] Superscripts and Subscripts (19): `⁰ ⁴⁵⁶⁷⁸⁹ ⁺ ⁼ ₀₁₂₃₄₅₆₇₈₉`
- [ ] Currency Symbols (6): `€ ₫ ₮ ₴ ₽ ₿`
- [ ] Letterlike Symbols (12): `ℂ ℍ ℓ ℕ № ℙ ℚ ℝ ™ ℤ ℮ ⅀`
- [ ] Latin Extended-A (128): Polish, Czech, Slovak, Hungarian, Turkish, Romanian,
      Baltic and Esperanto letters
- [ ] Latin Extended-B (41): `Ə Ɛ ƒ ƛ Ơ ơ Ư ư Ǎ ǎ Ǐ ǐ Ǒ ǒ Ǔ ǔ Ǖ ǖ Ǘ ǘ Ǚ ǚ Ǜ ǜ Ǧ ǧ Ǫ
      ǫ Ǵ ǵ Ǽ ǽ Ǿ ǿ Ș ș Ț ț Ȳ ȳ ȷ`

### Tier 3 — Coding symbols (548 glyphs)

Most of this tier is geometric and can be generated from a small set of
components instead of drawn by hand.

- [ ] Arrows (31): `↔ ↕ ↖ ↗ ↘ ↙ ↝ ↞ ↠ ↢ ↣ ↥ ↦ ↧ ↩ ↪ ↭ ↾ ⇉ ⇐ ⇑ ⇒ ⇓ ⇔ ⇛ ⇞ ⇟ ⇥ ⇧
      ⇨ ⇪`
- [ ] Mathematical Operators (119): `∀ ∂ ∃ ∅ ∇ ∈ ∉ ∋ ∏ ∑ − √ ∝ ∞ ∟ ∠ ∣ ∤ ∥ ∧ ∨ ∩
      ∪ ∫ ∴ ∼ ≃ ≅ ≈ ≉ ≋ ≍ ∘ ∙ ≠ ≡ ≤ ≥ ≪ ≫ ≺ ≻ ⊂ ⊃ ⊆ ⊇ ⊕ ⊗ ⊥ ⋈ ⋯ ⋮ ⌈ ⌉ ⌊ ⌋`
- [ ] Miscellaneous Technical (115): ceiling and floor brackets, corner pieces,
      `⌘`, `⌥`, `⌫`, `⏎`, the Power symbols, the 69 APL functional symbols, and the
      19 bracket-piece glyphs
- [ ] Box Drawing (128) and Block Elements (32): full light/heavy/double/rounded
      set plus shade and quadrant blocks
- [ ] Geometric Shapes (43): `■ □ ▪ ▫ ▲ △ ▶ ▷ ▼ ▽ ◀ ◁ ◆ ◇ ○ ◎ ● ◯`
- [ ] Control Pictures (36): `␀`–`␡`, `␣`, `␤` for whitespace visualisation
- [ ] Supplemental arrows and math (20): `⟅ ⟆ ⟜ ⟦ ⟧ ⟨ ⟩ ⟪ ⟫ ⟵ ⟶ ⟷ ⤖ ⥊ ⦇ ⦈ ⨀ ⨅
      ⨆ ⭘`
- [ ] Dingbats (12): `✓ ✕ ✗ ✶ ❮ ❯ ❰ ❱ ➔ ➜ ➝ ➞`
- [ ] Miscellaneous Symbols (5): `♭ ♯ ⚇ ⚠ ⚡`
- [ ] Powerline / Nerd Font (7): `U+E0A0`–`U+E0A2`, `U+E0B0`–`U+E0B3`

### Tier 4 — Greek and Cyrillic (201 glyphs)

- [ ] Greek and Coptic (79): monotonic Greek, including final sigma, the tonos
      forms and `ϕ ϖ ϗ`
- [ ] Cyrillic (122): Russian, Ukrainian, Serbian, Macedonian, plus the extended
      letters JetBrains Mono ships

### Tier 5 — Additional Latin and marks (136 glyphs)

- [ ] Latin Extended Additional (97): Vietnamese `Ạ`–`ỹ`, plus `Ẁ ẁ Ẃ ẃ Ẅ ẅ` and
      `ẞ`
- [ ] Spacing Modifier Letters (14): `ʹ ʺ ʼ ˆ ˇ ˉ ˘ ˙ ˚ ˛ ˜ ˝ ˳ ˷`
- [ ] Combining Diacritics (23): `U+0300`–`U+0338`, needed for decomposed text
- [ ] Number Forms (2): `↊ ↋`

### Tier 6 — Remainder (55 glyphs)

- [ ] Double-struck mathematical alphanumerics `U+1D538`–`U+1D56B` (45 glyphs,
      for `ℝ ℕ ℤ`-style names)
- [ ] `U+0259`, `U+025B`, `U+0AEA`, `U+16910`, `U+FE62`, `U+FEFF`, `U+FF5B`,
      `U+FF5D`, `U+FFFD`, `U+000D`

## OpenType features

Sleet Mono currently has no `GSUB`, `GPOS` or `GDEF` tables, so all of this is
new work. JetBrains Mono's set is the reference.

- [ ] **Ligatures (`calt`)** — 153 in JetBrains Mono. Suggested order:
      - [ ] Arrows: `-> --> <- <-- => ==> <= <== <-> <--> <=> <==>`
      - [ ] Comparison: `!= !== == === =/= =< >= <= <=> <<< >>>`
      - [ ] Fancy arrows: `<| <|| <||| <|> <||> <|||> |> ||> |||>`
      - [ ] Box drawing from `- | = _`: `-- --- == === || ||| __ ___`
      - [ ] Comments: `// /// /* */ #! #region #endregion`
      - [ ] Others: `:: ::= := ?: ?? ??? !! !!! . .. ... + ++ +++ ~~~ ~~>`
- [ ] `case` — punctuation for all-caps settings (`colon.case` etc.)
- [ ] `ccmp` — mark composition for decomposed accents
- [ ] `frac`, `ordn`, `sups`, `subs` — fractions and figures
- [ ] `zero` — slashed or dotted zero
- [ ] `locl` — language-specific forms
- [ ] `ss01` (classic construction), `ss02` (closed construction), `ss19`, `ss20`
- [ ] `cv01`–`cv20` and `cv99` character variants (20 in JetBrains Mono)
- [ ] `GPOS` mark positioning and `GDEF` for combining marks

## Housekeeping

- [ ] Set up the Fontra project with one source per style
- [ ] Add a charset-parity and advance-width check to the build
- [ ] Regenerate the charset and symbols images for each style
- [ ] Ship the new styles in the Homebrew cask and the Nerd Font build
- [ ] Bump the version and update the character set count in the README
