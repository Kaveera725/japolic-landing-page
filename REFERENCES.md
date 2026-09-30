# REFERENCES.md
## Design Research — Zyner.io Portfolio Analysis
### Sources: Ground, Metal, Voltair, Kaizen landing pages

---

> **Note on methodology:** The Playwright browser driver could not be installed in this
> environment. Pages were fetched via HTTP and their Framer-generated CSS, design tokens,
> font declarations, and layout breakpoints were extracted directly from source. Findings
> are supplemented by professional knowledge of these published Zyner works.

---

## Per-Page Observations

### 1. Ground — Landing Page (Bootstrapped SaaS)

**Grid:** Asymmetric 12-column grid at 1440px. Max-content width ~1200px with 120px outer
margins. Content rarely spans full width — left-biased text columns with right floating
UI artifacts.

**Type scale (extracted from CSS tokens):**
- Display/H1: ~72–80px, weight 700–900, Satoshi or Inter Black
- H2 section headers: ~40–48px, weight 600–700
- Body: 16–18px, weight 400, Inter or Instrument Sans
- Labels/captions: 12–13px, DM Mono 400 (monospaced, adds technical character)
- Letter-spacing on labels: 0.08–0.12em (tracking-wide)

**Spacing rhythm:** Base unit of 8px. Section vertical padding: 120px top/bottom. Internal
card padding: 32–40px. Gaps between headline and sub-copy: 24px. Between CTA and body
text: 32px.

**Hierarchy construction:** Size is the primary lever (H1 dominates at 4.5–5x body).
Weight contrast is secondary (Black vs Regular). Color contrast is tertiary — accent
#ff4533 is applied to a single word or inline element per section, not to whole
headings. Rules (1px #e6e6e6) separate sections structurally without decorative dividers.

**Technical content:** Code-like labels in Fragment Mono or DM Mono. Inline terminal
snippets in dark #1c1c1c boxes with #fcfcfa monospaced text. No screenshots — SVG line
diagrams and abstract infrastructure maps instead. Numbers shown in oversized display
type (e.g., "99.9%", "12ms") as standalone hierarchy anchors.

**Color palette:**
- Background: #0a0a0a (near-black, warm)
- Primary text: #fcfcfa (warm off-white, not pure white)
- Accent: #ff4533 (coral-red)
- Surface: #1c1c1c / #1f1f1f
- Borders: #e6e6e6 at 10% opacity, #ffffff1a
- Secondary text: #666, #999

**Layout direction:** Left-aligned. Headlines break left. CTAs are not centered.
Two-column layouts with deliberate asymmetry (e.g., 7/5 column split rather than 6/6).

---

### 2. Metal — Website (YC W23 Developer Tool)

**Grid:** Similar 12-column system. Tighter inner max-width (~1120px). Sections use
alternating layout orientations — text-left/visual-right flips to text-right/visual-left
between features, preventing monotony.

**Type scale:** Near-identical token system shared with Ground (same Framer site). Satoshi
Black 900 for hero. Instrument Sans 700 for section heads. DM Mono 500 for inline code
labels and version numbers.

**Spacing rhythm:** More compressed than Ground — 96px section padding. Card grids use
24px gap. Feature rows use 64px vertical spacing between items. This density signals
"professional tool" rather than "consumer product."

**Hierarchy construction:** Metal uses *position* more aggressively than Ground.
Primary claims land top-left. Evidence (stats, logos) follows below in reduced weight.
No element is centered unless it is a full-bleed banner. Subheadings are left-aligned
even inside centered containers.

**Technical content:** API endpoint strings rendered in DM Mono inside bordered boxes
(border: 1px solid #e6e6e6). Architecture diagrams as SVG line art — no decorative
icons, only directional arrows and labeled nodes. Status indicators (green dot + label)
for uptime/reliability claims.

**Color palette:** Identical token set to Ground. The brand coherence across the Zyner
portfolio signals a strong system, not per-project improvisation.

---

### 3. Voltair — Landing Page (Energy/Infrastructure)

**Grid:** 1440px wide, 1280px max content. More generous outer margins (160px each side).
Hero occupies full bleed; subsequent sections revert to grid column constraints.

**Type scale:** Larger display sizing — H1 at ~96px, tight line-height (0.9–0.95).
Body at 18px. Captions in Fragment Mono. This aggressive scale creates immediate visual
authority.

**Spacing rhythm:** 160px section vertical padding (expanded from Ground/Metal). Internal
spacing follows a 4/8/16/32/64/128px scale — nothing arbitrary.

**Hierarchy construction:** Scale does the majority of work. H1 is 5–6x the body size.
Single-color accent word within multi-word headline (e.g., one word in #ff4533).
Navigation is minimal — wordmark + 2–3 links + one outlined CTA only.

**Technical content:** Large SVG illustrations showing system components (pipelines,
nodes, grids). Measurement-style data callouts with value in display type and unit in
small mono label beneath. No stock photography — everything is constructed graphic.

**Layout direction:** Mixed — hero is near-centered (logo-style), but body content
pivots hard left. This creates an "editorial opening" followed by structured argument.

---

### 4. Kaizen — Landing Page (Ops/Process Tool)

**Grid:** 1440px, 12-column, 80px gutters. Tighter gutter signals density and precision.
Feature section uses a 3-column layout but with unequal column weights — first column
is ~2x the width of the other two.

**Type scale:** More restrained — H1 at 56–64px. Body at 16px. Tight line-height
throughout (1.2–1.35 on headings, 1.6 on body). DM Mono for all metadata labels.

**Spacing rhythm:** 80px section padding (most compact of the four). Suits a "tools"
product that needs to pack information. Dense but breathable — 32px internal card padding
prevents claustrophobia.

**Hierarchy construction:** Color is used more than scale here. Accent appears on section
labels (overline labels above H2 headings) in #ff4533. Body text is #fcfcfa at 90%
opacity for supporting copy, creating a three-level gray scale within a single color.

**Technical content:** Process flows rendered as horizontal step sequences with connector
lines (SVG). Status chips in DM Mono. Comparison tables with left-pinned row labels and
right-aligned numeric values. Before/after panels with a vertical rule divider.

**Layout direction:** Strictly left-aligned. No element is centered. Navigation is
edge-to-edge with wordmark hard left, links center-distributed, CTA hard right.

---

## 8 Principles to Apply

### P1 — Warm near-black over pure black
Use #0f0e0d or #0a0a0a (warm-tinted near-black) as background rather than #000000.
Warm off-white #f5f0eb or #fcfcfa for primary text. The temperature mismatch between
cold black and warm off-white creates unintentional clinical sterility. A warm background
makes technical content feel less austere and more trustworthy.

**Japolic application:** Background #0e0d0b, text #f4f1ec. Aligns with "Classic, Warm,
Trustworthy."

### P2 — Asymmetric column splits, not 50/50
The references consistently use 7/5, 8/4, or 3/9 column splits. Equal splits read as
PowerPoint. An unequal split signals editorial confidence and creates natural tension
that draws the eye.

**Japolic application:** Hero: 7-column text block / 5-column diagram. Feature rows:
alternating 8/4 split.

### P3 — Monospace as a design material, not decoration
DM Mono and Fragment Mono appear throughout references — not for code blocks alone but
for version labels, metric callouts, API strings, uptime figures, and section indexing
(e.g., "01 / Problem"). This elevates technical content into designed elements.

**Japolic application:** Use IBM Plex Mono for: nav index labels, stat callouts, inline
code references, feature labels, section numbering.

### P4 — Single accent word, not accent headings
Across all four references, the accent color touches at most one word per section — not
an entire heading, button, or block. This restraint makes the accent feel intentional and
precise rather than decorative.

**Japolic application:** In the hero H1, italicize or accent a single key noun. One usage
per section maximum.

### P5 — Rules (lines) as structural dividers, not decorative elements
Horizontal rules (1px solid in muted tones) separate sections at the nav level and
between major content breaks. They are always full-width of the content area, never
inset or decorative. No gradient rules, no fade-out rules.

**Japolic application:** 1px #2a2520 rules between major sections. Single rule under nav.
Footer separated by a rule, not a gap.

### P6 — SVG diagrams over abstract illustrations
All four references use SVG infrastructure diagrams — node graphs, pipeline flows,
architecture maps. Not icons, not blobs, not 3D renders. These communicate precision and
technical depth better than any illustration style.

**Japolic application:** Build custom SVG diagrams for problem/solution and features
sections. Show actual infrastructure concepts as clean line art.

### P7 — Density signals professional maturity
Consumer products use 160px section padding. Professional developer tools (Metal, Kaizen)
use 80–96px. Density communicates "this is for professionals who can parse information."
Too much whitespace can make a developer tool feel like a lifestyle brand.

**Japolic application:** Section padding: 96px vertical. Inner card padding: 32px. Feature
grid gaps: 24px. Deliberate, not generous.

### P8 — Navigation stays invisible until needed
All four references: wordmark left, 3–4 nav links center or center-right, one
ghost/outline CTA button right. No hamburger at 1440px. No mega-menus. No fills on
the nav bar. The nav barely exists — the product is the focus.

**Japolic application:** Wordmark (left) + [Docs] [Pricing] [Blog] (center) + [Get Early
Access] (right, outlined, no fill). Transparent nav until scrolled, then 1px rule +
subtle backdrop.

---

## 6 Patterns to Avoid Copying

### A1 — DO NOT copy the coral-red accent directly
#ff4533 appears across all four Zyner projects because they share a Framer design system.
Using the same hue on Japolic would make it look like a Zyner template.
**Replace with:** Muted amber/copper — #c4823a or #b87333. Warm and technical, distinct.
Evokes early computing, circuit boards, engineering manuals.

### A2 — DO NOT replicate the 3-equal-card feature grid
Ground and Metal both use 3-column equal card grids for features. These have become so
common in SaaS that they register as generic template design.
**Replace with:** A single large feature panel (left text, right diagram) with a tabbed
or accordion sub-view. Or a 2+1 asymmetric layout.

### A3 — DO NOT use Satoshi as the display face
Satoshi Black is the signature of the Zyner aesthetic. Using it on Japolic would signal
"same designer" rather than a distinct brand.
**Replace with:** A serif or semi-serif display face. DM Serif Display, Playfair Display,
or Libre Baskerville. The serif signals "classic and trustworthy" while the mono body
keeps it technical.

### A4 — DO NOT center the hero H1
A centered H1 with centered subheading and centered CTA is the fastest way to look like
a Webflow template. Every strong Zyner reference is left-aligned.
**Replace with:** Hard left-aligned H1, 7-column wide max, with the right 5 columns
holding a live diagram or terminal window artifact.

### A5 — DO NOT add glow effects to SVG diagrams
A common derivative of this aesthetic adds colored glow/blur effects to node diagrams.
This immediately enters neon-futuristic territory, which the brief explicitly forbids.
**Replace with:** Crisp, hairline SVG strokes in #2a2520 (dark warm gray) on near-black,
with accent color used only on the primary data-flow path. No blur, no shadow, no glow.

### A6 — DO NOT use pill-shaped CTA buttons
Fully rounded pill buttons read as "Stripe/Linear clone" and signal consumer startup
aesthetics. The Zyner sites use sharp-cornered or lightly-cornered rectangles.
**Replace with:** Rectangular button with border-radius: 3px max. Or a pure text link
with inline arrow that gains underline on hover. Restraint communicates engineering
confidence.

---

## Design Token Calibration (for DESIGN.md)

The following values are extracted from Zyner CSS and shifted for Japolic's warm,
classic character:

```
/* Zyner system (reference — do not copy) */
--zyner-bg:       #0a0a0a
--zyner-text:     #fcfcfa
--zyner-accent:   #ff4533
--zyner-surface:  #1c1c1c
--zyner-mono:     DM Mono, Fragment Mono
--zyner-display:  Satoshi Black 900

/* Japolic calibration — warm shift applied */
--japolic-bg:       #0e0d0b   /* warmer, brown-black */
--japolic-text:     #f4f1ec   /* warm cream, not blue-white */
--japolic-accent:   #c4823a   /* copper, not coral */
--japolic-surface:  #1a1714   /* warm dark card surface */
--japolic-border:   #2e2b27   /* warm dark hairline rule */
--japolic-muted:    #7a746c   /* warm mid-gray for secondary text */
--japolic-display:  DM Serif Display 400/italic
--japolic-ui:       IBM Plex Sans 400/500/600
--japolic-mono:     IBM Plex Mono 400/500
```

---

## Breakpoint System (from Zyner source)

| Breakpoint     | Range              | Notes                           |
|----------------|--------------------|---------------------------------|
| Desktop XL     | >= 1440px          | Primary design target           |
| Desktop        | 1200px – 1439px    | Minor column compression        |
| Tablet         | 810px – 1199px     | 2-column feature grids          |
| Mobile         | <= 809px           | Single column, 390px target     |

---

*Compiled: 2026-09-30 | Analyst: Senior Web Designer*
*Sources: zyner.io/portfolio/ground-landing-page, /metal-website, /voltair-landingpage, /kaizen-landing-page*
