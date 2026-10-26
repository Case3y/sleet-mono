# Sleet Mono

A monospaced programming typeface with a casual, hand-drawn Comic style.
Open forms, generous spacing, made for reading code.

![Sleet Mono](images/hero.png)

## Why Sleet Mono

I love Comic-style typefaces, but I wasn't happy with some of the glyph metrics in
[Comic Shanns](https://github.com/shannpersand/comic-shanns). So I started from its
outlines and reworked the proportions myself, using
[JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) as a reference for the
vertical metrics and spacing.

## Character set

Currently **103 glyphs**: complete Basic Latin (`U+0020`–`U+007E`), plus curly quotes
and arrows. More glyphs and additional weights are in progress — see the
[roadmap](ROADMAP.md).

![Character set](images/charset.png)

## In use

![Sleet Mono in an editor](images/code.png)

## Symbols

![Symbols](images/symbols.png)

## Roadmap

Sleet Mono currently has one style and 103 codepoints. The goal is parity with
JetBrains Mono: four styles and 1,372 codepoints.

| Milestone | Scope |
| --- | --- |
| M1 | Bold, Italic and Bold Italic at the current character set |
| M2 | Complete the GF Latin Kernel set |
| M3 | Western European text and typography |
| M4 | Coding symbols: arrows, math, box drawing, control pictures |
| M5 | Greek and Cyrillic |
| M6 | Remaining blocks: APL, double-struck, dingbats, Nerd Font extras |

See [ROADMAP.md](ROADMAP.md) for the full checklist.

## Installation

### Homebrew (macOS)

```sh
brew install --cask Case3y/fonts/font-sleet-mono
```

For the Nerd Font patched build, which adds terminal and editor icons:

```sh
brew install --cask Case3y/fonts/font-sleet-mono-nerd-font
```

### Manual

Download `SleetMono-Regular.ttf` from [`fonts/`](fonts/), then install it with your
system font manager.

## Credits

- Glyph outlines derived from [Comic Shanns](https://github.com/shannpersand/comic-shanns)
  by Shannon Miwa.
- Glyph proportions and vertical metrics referenced from
  [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono).

## License

Sleet Mono is licensed under the [MIT](LICENSE) License. 
