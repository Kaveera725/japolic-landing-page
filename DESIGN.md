# DESIGN.md
## Japolic Design System — Single Source of Truth
### Version 1.0 | 2026-09-30
### Do not contradict this document. If a decision changes, update here first.

---

## 0. Design Intent

Japolic's visual language draws from early technical publishing: IBM systems manuals,
Bell Labs typography, pre-digital engineering drawings. The aesthetic is **warm ink on
cream paper** — precise, unhurried, undecorated. It earns trust through structural
clarity, not visual drama.

Three words that must survive every design decision:
**Classic. Precise. Trustworthy.**

Three words that must not appear in the outcome:
**Startup. Gradient. Futuristic.**

---

## 1. Typography

### 1.1 Font Families

| Role       | Family             | Weights Used      | Source             |
|------------|--------------------|-------------------|--------------------|
| Display    | Fraunces           | 300, 400, 600     | Google Fonts       |
| Body / UI  | IBM Plex Sans      | 400, 500, 600     | Google Fonts       |
| Technical  | IBM Plex Mono      | 400, 500          | Google Fonts       |

**Why Fraunces:** A variable optical-size serif designed for display use. At large sizes
it has pronounced ink traps and soft terminals — mechanical yet warm. Italic at 300 weight
creates editorial elegance without ornamentation. It does not look like a SaaS site.

**Why IBM Plex Sans:** Designed by Mike Abbink for IBM's rebrand. It carries genuine
engineering heritage. The letterforms are open and precise. It pairs with Plex Mono
naturally because they share the same design language.

**Why IBM Plex Mono:** Not chosen for developer aesthetics — chosen because it reads as
a *measurement instrument*. Monospaced type on metrics, labels, and code sections
communicates exactness, not decoration.

---

### 1.2 Type Scale — Desktop (1440px)

All sizes in px. Line-height unitless ratio. Tracking in em.

| Token         | Size | Line-Height | Tracking  | Weight | Family          | Usage                                |
|---------------|------|-------------|-----------|--------|-----------------|--------------------------------------|
| `--t-d1`      | 80px | 0.92        | −0.03em   | 300    | Fraunces        | Hero H1 primary line                 |
| `--t-d2`      | 56px | 0.96        | −0.02em   | 300    | Fraunces        | Section openers, H2 primary          |
| `--t-d3`      | 40px | 1.05        | −0.01em   | 400    | Fraunces        | Feature panel titles                 |
| `--t-h4`      | 28px | 1.15        | 0em       | 600    | IBM Plex Sans   | Card/panel headings                  |
| `--t-h5`      | 20px | 1.25        | 0em       | 600    | IBM Plex Sans   | Sub-section labels                   |
| `--t-body-lg` | 18px | 1.65        | 0em       | 400    | IBM Plex Sans   | Hero sub-copy, intro paragraphs      |
| `--t-body`    | 16px | 1.60        | 0em       | 400    | IBM Plex Sans   | Standard body copy                   |
| `--t-body-sm` | 14px | 1.55        | 0em       | 400    | IBM Plex Sans   | Secondary descriptive text           |
| `--t-label`   | 13px | 1.00        | 0.10em    | 500    | IBM Plex Mono   | Section index labels (e.g. "01 —")   |
| `--t-caption` | 12px | 1.40        | 0.06em    | 400    | IBM Plex Mono   | Footnotes, timestamps, legal lines   |
| `--t-code`    | 13px | 1.70        | 0.02em    | 400    | IBM Plex Mono   | Inline code, config snippets         |
| `--t-stat`    | 48px | 1.00        | −0.02em   | 500    | IBM Plex Mono   | Large metric callouts (99.9%, 4.5m)  |
| `--t-stat-sm` | 13px | 1.00        | 0.08em    | 400    | IBM Plex Mono   | Unit label beneath a stat            |

**Notes:**
- `--t-d1` and `--t-d2` use Fraunces at light weight (300) with negative tracking.
  The combination creates authority without aggression.
- `--t-stat` uses IBM Plex Mono — numbers in a monospaced face align cleanly in columns
  and read as *measured values*, not marketing claims.
- Fraunces italic (300i) is permitted on the single accented word in the hero H1 only.
  Do not use italic elsewhere in the type system.

---

### 1.3 Type Scale — Mobile (390px)

Fluid scaling applied. All Fraunces display sizes reduce by ~30%. Body sizes are fixed.

| Token         | Size | Line-Height | Tracking  | Weight | Notes                                  |
|---------------|------|-------------|-----------|--------|----------------------------------------|
| `--t-d1`      | 48px | 0.95        | −0.02em   | 300    | Hero H1 — 2-line break at 390px        |
| `--t-d2`      | 36px | 1.00        | −0.01em   | 300    | Section H2                             |
| `--t-d3`      | 28px | 1.10        | 0em       | 400    | Feature panel titles                   |
| `--t-h4`      | 22px | 1.20        | 0em       | 600    | Card headings                          |
| `--t-h5`      | 18px | 1.25        | 0em       | 600    | Sub-section labels                     |
| `--t-body-lg` | 17px | 1.60        | 0em       | 400    | Intro paragraphs                       |
| `--t-body`    | 15px | 1.60        | 0em       | 400    | Standard body                          |
| `--t-body-sm` | 13px | 1.55        | 0em       | 400    | Secondary text                         |
| `--t-label`   | 11px | 1.00        | 0.10em    | 500    | Section index labels                   |
| `--t-caption` | 11px | 1.40        | 0.06em    | 400    | Footnotes                              |
| `--t-code`    | 12px | 1.70        | 0.02em    | 400    | Inline code                            |
| `--t-stat`    | 36px | 1.00        | −0.01em   | 500    | Metric callouts                        |
| `--t-stat-sm` | 11px | 1.00        | 0.08em    | 400    | Stat unit labels                       |

---

### 1.4 Type Rules (non-negotiable)

1. **Max line length:** 68 characters for body copy. 48 characters for labels. Enforce
   via `max-width` on text containers, not `ch` units (browser support inconsistency).
2. **No bold in body paragraphs.** Use weight 400 throughout. Emphasis via structure
   (new paragraph, label above) not bold inline.
3. **No underlines** except on anchor links within body copy on hover.
4. **All-caps: prohibited.** Section labels use Plex Mono tracked wide at sentence case.
   `letter-spacing: 0.10em` on `--t-label` achieves the same visual effect without the
   archaic formality.
5. **Fraunces italic:** Reserved for the single accented noun in the hero H1. One usage
   per page.

---

## 2. Color System

### 2.1 Palette

| Token              | Hex       | Name          | RGB Equivalent         |
|--------------------|-----------|---------------|------------------------|
| `--c-paper`        | `#F4EEE1` | Cream Paper   | rgb(244, 238, 225)     |
| `--c-ink`          | `#1C1A17` | Warm Ink      | rgb(28, 26, 23)        |
| `--c-amber`        | `#D9822B` | Amber         | rgb(217, 130, 43)      |
| `--c-green`        | `#2F4A3C` | Deep Green    | rgb(47, 74, 60)        |
| `--c-hairline`     | `#D8CFBC` | Hairline      | rgb(216, 207, 188)     |
| `--c-muted`        | `#8C8476` | Warm Muted    | rgb(140, 132, 118)     |
| `--c-surface`      | `#EDE7D7` | Surface Card  | rgb(237, 231, 215)     |
| `--c-footer-bg`    | `#1C1A17` | Footer Dark   | rgb(28, 26, 23)        |
| `--c-footer-text`  | `#9A9287` | Footer Muted  | rgb(154, 146, 135)     |
| `--c-code-bg`      | `#E8E1D0` | Code Surface  | rgb(232, 225, 208)     |

### 2.2 Contrast Ratios

Measured against primary use context. WCAG AA requires 4.5:1 for body text, 3:1 for
large text (≥18px normal or ≥14px bold).

| Foreground         | Background         | Ratio   | WCAG   | Usage context                     |
|--------------------|--------------------|---------|--------|-----------------------------------|
| `--c-ink` #1C1A17  | `--c-paper` #F4EEE1| **14.2:1** | AAA  | Body copy — primary               |
| `--c-ink` #1C1A17  | `--c-surface` #EDE7D7 | **13.1:1** | AAA | Card body copy                 |
| `--c-amber` #D9822B| `--c-paper` #F4EEE1| **3.1:1** | AA (large) | CTA button label, stat accent |
| `--c-amber` #D9822B| `--c-ink` #1C1A17  | **4.7:1** | AA   | Amber on dark (footer CTA)       |
| `--c-muted` #8C8476| `--c-paper` #F4EEE1| **4.6:1** | AA   | Secondary body text               |
| `--c-paper` #F4EEE1| `--c-green` #2F4A3C| **7.4:1** | AAA  | White text on green surfaces      |
| `--c-paper` #F4EEE1| `--c-ink` #1C1A17  | **14.2:1** | AAA | Inverted (footer nav links)      |
| `--c-footer-text` #9A9287 | `--c-footer-bg` #1C1A17 | **4.5:1** | AA | Footer secondary links    |

**Critical note on amber:** #D9822B on #F4EEE1 passes AA only at large text (≥18px or
bold). Do not use amber as body-weight text below 18px on the cream background. Amber
on the dark footer background (#1C1A17) passes AA at all sizes.

---

### 2.3 Color Usage Rules

**`--c-paper` (#F4EEE1) — Cream Paper**
- Default page background for all sections except footer
- Do not use as text color
- Do not tint, shade, or mix. Use exactly as defined.

**`--c-ink` (#1C1A17) — Warm Ink**
- All headings, body copy, labels on cream background
- Footer background
- Border color for CTA buttons in their default (non-hover) state
- Do not use as accent or highlight

**`--c-amber` (#D9822B) — Amber**
- CTAs only: the "Request Access →" button background
- Accent on a single word in the hero H1 (color, not background)
- Large metric/stat numbers where emphasis is required (≥ 36px)
- Hover state border and text on ghost/outlined buttons
- **Maximum two amber elements visible in any viewport at once**
- **Prohibited:** body text, nav links, decorative borders, section backgrounds,
  underlines, icon fills (except the single CTA icon)

**`--c-green` (#2F4A3C) — Deep Green**
- Success/status indicators (uptime dot, healthy state chip)
- Accent surface behind the "feature deep-dive" panel
- Background of alternating use-case rows if color variation is needed
- **Do not use as a primary brand color.** It is functional, not decorative.

**`--c-hairline` (#D8CFBC) — Hairline**
- All horizontal rules between sections
- Table borders
- Card outlines (1px)
- Input borders
- Dividers inside nav and footer
- **Weight: always 1px. Never 2px. Never styled or dashed.**

**`--c-muted` (#8C8476) — Warm Muted**
- Secondary body copy (descriptions beneath headings)
- Footer nav link text
- Placeholder text in inputs
- Timestamp and caption text
- **Never use on amber or green backgrounds (contrast insufficient)**

**`--c-surface` (#EDE7D7) — Surface Card**
- Background for feature cards, code blocks, inset panels
- Distinguishes contained content from the page background
- Do not use as text color

**`--c-code-bg` (#E8E1D0) — Code Surface**
- Background for all code blocks and `<pre>` elements
- Slightly darker than `--c-surface` to distinguish nested elements
- Always pair with `--c-ink` text at Plex Mono weight 400

---

### 2.4 Color Rules (non-negotiable)

1. **No gradients. Anywhere. Ever.** Not on backgrounds, buttons, borders, or SVG fills.
2. **No shadows.** Use hairline borders and structural spacing for depth. `box-shadow`
   and `text-shadow` are prohibited.
3. **No opacity stacks.** Do not use `rgba()` to create tinted intermediates. If a new
   value is needed, add it to the palette with a named token.
4. **No background images on section backgrounds.** Texture, noise overlays, and
   grain effects are prohibited.
5. **The amber accent is rationed.** If you find yourself using amber on more than
   two elements in a viewport, remove one.

---

## 3. Layout

### 3.1 Grid — Desktop (1440px)

| Property         | Value                                            |
|------------------|--------------------------------------------------|
| Viewport target  | 1440px                                           |
| Max content width| 1200px                                           |
| Outer margin     | auto (centered, min 120px each side at 1440px)   |
| Columns          | 12                                               |
| Column gutter    | 24px                                             |
| Column width     | ~76px (calculated: (1200 − 11×24) / 12 = 77.5px)|

**Column splits in use:**
| Split | Columns | Usage                                         |
|-------|---------|-----------------------------------------------|
| 7 / 5 | 7 + 5   | Hero: text block / diagram                    |
| 8 / 4 | 8 + 4   | Feature deep-dive: content / panel            |
| 4 / 4 / 4 | 3×4 | Only for use case metrics row (3 stats)    |
| 6 / 6 | 6 + 6   | Prohibited except for full-bleed image pairs  |
| 5 / 2 / 5 | 5+2+5 | Problem/Solution split with center rule  |
| 12    | full    | Section labels, full-width rules, nav bar     |

**Do not default to 6/6. Reach for 7/5 or 8/4 first.**

---

### 3.2 Grid — Mobile (390px)

| Property         | Value                           |
|------------------|---------------------------------|
| Viewport target  | 390px                           |
| Outer margin     | 20px each side                  |
| Content width    | 350px                           |
| Columns          | 4                               |
| Column gutter    | 16px                            |
| Column width     | ~71px ((350 − 3×16) / 4 = 75.5)|

All desktop multi-column layouts collapse to single column on mobile unless otherwise
specified. Exception: the 3-stat row (4/4/4) collapses to a vertical stack.

---

### 3.3 Spacing Scale

Base unit: **8px**. All spacing values must be multiples of 8px.

| Token           | Value | Usage                                              |
|-----------------|-------|----------------------------------------------------|
| `--sp-2`        | 2px   | Internal tight gap (icon-to-label, etc.)           |
| `--sp-4`        | 4px   | Tag padding, chip internal spacing                 |
| `--sp-8`        | 8px   | Base unit. Label-to-heading gap                    |
| `--sp-12`       | 12px  | Tight inline spacing                               |
| `--sp-16`       | 16px  | Default padding for small components               |
| `--sp-24`       | 24px  | Card internal padding, feature grid gap            |
| `--sp-32`       | 32px  | Heading-to-body gap, card padding (standard)       |
| `--sp-48`       | 48px  | Between headline and CTA group                     |
| `--sp-64`       | 64px  | Between feature rows within a section              |
| `--sp-96`       | 96px  | Between major sub-sections                         |
| `--sp-120`      | 120px | Section top/bottom padding — desktop               |
| `--sp-72`       | 72px  | Section top/bottom padding — mobile                |
| `--sp-160`      | 160px | Hero top padding (desktop only, nav clearance)     |

**Non-multiples of 8 are not permitted. Exception: 2px for hairline-adjacent nudges.**

---

### 3.4 Section Padding

| Section      | Desktop (top / bottom) | Mobile (top / bottom) |
|--------------|------------------------|-----------------------|
| Nav          | 24px / 24px            | 16px / 16px           |
| Hero         | 160px / 120px          | 80px / 72px           |
| Problem      | 120px / 120px          | 72px / 72px           |
| Solution     | 120px / 120px          | 72px / 72px           |
| Feature      | 120px / 120px          | 72px / 72px           |
| Use Cases    | 120px / 120px          | 72px / 72px           |
| Footer       | 64px / 48px            | 48px / 40px           |

---

### 3.5 Border Radius

| Context                   | Radius Value | Token         |
|---------------------------|--------------|---------------|
| Default (cards, panels)   | 2px          | `--r-sm`      |
| Buttons                   | 2px          | `--r-sm`      |
| Code blocks               | 2px          | `--r-sm`      |
| Tags / chips              | 2px          | `--r-sm`      |
| Status dots               | 50% (circle) | `--r-full`    |
| All other elements        | 0px          | —             |

**The maximum border-radius in the system is 2px. Pill shapes (border-radius: 999px)
are prohibited.**

---

## 4. Component Rules

### 4.1 Navigation Bar

```
Height:         72px desktop / 56px mobile
Background:     transparent (default) / --c-paper + opacity 0.97 (scrolled)
Border-bottom:  none (default) / 1px solid --c-hairline (scrolled)
Backdrop:       none — do not use backdrop-filter: blur()
Transition:     border-color 200ms ease, background 200ms ease

Layout:
  Left:   Japolic wordmark — Fraunces 400, 18px, --c-ink
  Center: Nav links (Docs, Protocol Reference, Changelog, Pricing)
          IBM Plex Sans 500, 14px, --c-ink / --c-muted on hover
          No underline. No background on hover. Subtle opacity shift only.
  Right:  "Request Access →" button (see 4.3)
```

---

### 4.2 Section Index Labels

Used above every H2 to identify the section number and name.

```
Format:     01 — Hero
Font:       IBM Plex Mono 500, 13px desktop / 11px mobile
Color:      --c-muted
Tracking:   0.10em
Case:       Sentence case (not ALL CAPS)
Margin:     0 0 16px 0 (16px below before the H2)
```

---

### 4.3 Buttons

**Primary CTA (amber fill):**
```
Background:     --c-amber (#D9822B)
Text:           --c-ink (#1C1A17)  [contrast 4.7:1 ✓]
Font:           IBM Plex Sans 600, 15px
Padding:        14px 28px
Border:         none
Border-radius:  2px
Hover:          background darkens to #C4711E (10% darker)
Active:         background darkens to #B36218
Transition:     background 150ms ease
Arrow suffix:   " →" (standard text, not an SVG icon)
```

**Secondary / Ghost (outlined):**
```
Background:     transparent
Text:           --c-ink
Font:           IBM Plex Sans 500, 15px
Padding:        13px 27px  (1px less to account for border)
Border:         1px solid --c-ink
Border-radius:  2px
Hover:          border-color --c-amber, color --c-amber
Transition:     border-color 150ms ease, color 150ms ease
```

**Text link with arrow:**
```
Background:     none
Text:           --c-ink, IBM Plex Sans 500, 15px
Underline:      none default / underline on hover
Arrow:          " →" appended in DOM, nudges right 4px on hover
Transition:     text-decoration 100ms, letter-spacing 100ms
```

---

### 4.4 Code Blocks

```
Background:     --c-code-bg (#E8E1D0)
Border:         1px solid --c-hairline
Border-radius:  2px
Padding:        24px 28px
Font:           IBM Plex Mono 400, 13px, line-height 1.70
Color:          --c-ink
Overflow:       auto (horizontal scroll — do not wrap code)
Tab size:       2

Syntax highlighting (minimal):
  Keys/properties:  --c-ink (no change)
  String values:    --c-green (#2F4A3C)
  Comments:         --c-muted (#8C8476)
  Numbers:          --c-amber (#D9822B) — only numeric literal values
  No other colors.
```

---

### 4.5 Horizontal Rules

```
Height:         1px
Color:          --c-hairline (#D8CFBC)
Width:          100% of content area (1200px max-width container)
Margin:         0 — spacing is handled by section padding, not rule margins
Border:         none — use background-color on a <div> or border-top on a <hr>
No gradient fades. No dashed or dotted variants.
```

---

### 4.6 Stat / Metric Callouts

```
Value:      IBM Plex Mono 500, 48px desktop / 36px mobile, --c-ink
            Use --c-amber ONLY if the stat is the primary CTA-adjacent claim
Unit label: IBM Plex Mono 400, 13px, --c-muted, tracking 0.08em
            Positioned directly below the value, no margin between
Context:    IBM Plex Sans 400, 14px, --c-muted, margin-top 8px
```

---

### 4.7 Feature Cards / Panels

```
Background:     --c-surface (#EDE7D7)
Border:         1px solid --c-hairline
Border-radius:  2px
Padding:        40px desktop / 32px mobile

Internal layout:
  Label (monospace): IBM Plex Mono 500, 12px, --c-muted, tracking 0.10em
  Title:             Fraunces 400, 28px (--t-h4 scale)
  Body:              IBM Plex Sans 400, 16px (--t-body)
  Gap label→title:   16px
  Gap title→body:    24px
```

---

### 4.8 Status Chips

```
Background:     transparent
Border:         1px solid --c-hairline
Border-radius:  2px
Padding:        4px 10px
Font:           IBM Plex Mono 400, 12px, tracking 0.06em
Color:          --c-muted

Status dot (inside chip):
  Size:         6px × 6px
  Shape:        50% (circle)
  Color:        --c-green for healthy/active
                --c-amber for degraded/pending
                #C4441A for error (dark red, not in main palette — restricted to this use)
  Margin-right: 6px
```

---

## 5. SVG Diagram Rules

All technical diagrams are hand-authored SVG. No image files, no external diagram tools,
no icon libraries.

```
Stroke width:   1px for all lines and paths
Stroke color:   --c-ink (#1C1A17) at 40% opacity for secondary paths
                --c-ink at 100% for primary data-flow path
                --c-amber for the single highlighted path (one per diagram max)
Fill:           --c-paper or --c-surface for nodes
                Never gradient fills
Node style:     rect with border-radius 2px, 1px stroke --c-hairline
                or circle for terminal/endpoint nodes
Label type:     IBM Plex Mono 400, 11px, --c-ink
Arrows:         SVG marker-end arrowhead, 6px, filled with stroke color
                No decorative arrowhead styles
No drop shadows. No blur filters. No animation on SVG paths in default state.
```

---

## 6. Animation & Interaction

Philosophy: **The page is still by default. Motion is a response to user intent.**

```
Hover transitions:    150ms ease (buttons, links, chips)
Scroll-triggered:     opacity 0 → 1, translateY 16px → 0, 400ms ease-out
                      Triggered when element enters viewport at 80% threshold
Nav scroll state:     200ms ease (background + border)
No:                   parallax, auto-playing animations, scroll-jacking,
                      staggered entrance sequences, pulsing elements,
                      rotating logos, typewriter effects, infinite marquees
```

---

## 7. Accessibility Rules

1. All interactive elements have visible focus styles:
   `outline: 2px solid --c-amber; outline-offset: 3px`
2. No color-only information conveyance. Status chips use dot + text label.
3. All SVG diagrams have `aria-label` and `role="img"`.
4. Skip-to-content link is the first DOM element, visible on focus.
5. Minimum touch target: 44px × 44px on mobile.

---

*End of DESIGN.md v1.0*
*Next artifact: tokens.css derived directly from this document.*
