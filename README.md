# Japolic — Developer Infrastructure Landing Page
### Senior Web Designer Internship Assessment & Design System

A Figma-ready, zero-framework web design system and landing page for **Japolic**, an internal service protocol arbitration and routing layer.

---

## Deliverables Summary

| Artifact | File | Description |
|---|---|---|
| **Live Landing Page** | [`index.html`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/index.html) | Full 6-section landing page (Nav, Hero, Problem, Solution, Feature, Use Cases, Footer). Responsive for 1440px desktop & 390px mobile. |
| **Web-Direction Board** | [`direction.html`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/direction.html) | Design system board: color contrast audit, type specimens, component specs, and studio critique matrix. |
| **SVG Asset Library** | [`assets.html`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/assets.html) | Hand-crafted SVG library: isometric server rack, Hollerith punch card, registration marks, and 12 line icons (1.5px stroke). |
| **Design System Spec** | [`DESIGN.md`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/DESIGN.md) | Single source of truth: typography, color tokens, grid ratios, spacing scale, component rules, contrast measurements. |
| **Copywriting Spec** | [`CONTENT.md`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/CONTENT.md) | Copywriting single source of truth: brand def, 3 capabilities, headline rules, 3 use cases with authentic metrics. |
| **Design Research** | [`REFERENCES.md`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/REFERENCES.md) | Studio benchmark analysis across 4 reference sites: 8 applied principles and 6 anti-patterns rejected. |
| **CSS Tokens** | [`tokens.css`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/tokens.css) | 1:1 CSS Custom Properties implementation derived from `DESIGN.md`. |
| **Landing Styles** | [`landing.css`](file:///c:/Users/anush/OneDrive/Desktop/practicle%20DevOps/japolic/japolic-landing-page/landing.css) | Clean component stylesheet referencing CSS custom properties exclusively. |

---

## Design Thesis & Heritage

Japolic draws aesthetic and conceptual inspiration from early computing history and classic technical publishing:
- **Warm Ink on Cream Paper:** `#1C1A17` on `#F4EEE1` provides high contrast (14.2:1 AAA) with an analog, printed manual feel reminiscent of Bell Labs and IBM systems documentation.
- **Precision Instrument Typography:**
  - **Fraunces:** Optical-size display serif at light 300 weight with subtle ink traps.
  - **IBM Plex Sans:** Modernist grotesque engineered by Mike Abbink for IBM.
  - **IBM Plex Mono:** Measurement and telemetry face with tabular exactness.
- **Honest Structure:**
  - Zero gradients.
  - Zero box-shadows.
  - 1px hairline rules (`#D8CFBC`) for all structural divides.
  - Max 2px border-radius (`--r-sm`) — no bubbly pill shapes.
  - Amber (`#D9822B`) strictly rationed (max 2 visible elements per viewport).

---

## Responsive Breakpoints & Grids

- **Desktop (1440px):**
  - 1200px max content width (`var(--container-width)`)
  - 12-column grid with 24px gutters
  - 120px section padding (`--sp-120`)
  - Asymmetric splits: 7/5 Hero, 5/1/6 Problem, 8/4 Feature deep-dive
- **Mobile (390px):**
  - 350px content width with 20px outer margins
  - 4-column grid with 16px gutters
  - 72px section padding (`--sp-72`)
  - Collapsible navigation drawer with accessible ARIA toggle

---

## Presentation & Defense Talking Points (Video Ready)

1. **Why not a dark-mode neon theme like typical dev tools?**
   - *Defense:* Internal service protocol enforcement is serious, foundational infrastructure. Mainframe and Bell Labs documentation earned trust through restraint and legibility, not gaming-aesthetic neon glow.
2. **Why Fraunces for a developer tool?**
   - *Defense:* Fraunces at light weight (300) evokes vintage engineering editorial design. Paired with IBM Plex Mono, it positions Japolic as a mature, timeless system rather than another ephemeral SaaS startup.
3. **Why 7/5 and 8/4 column splits instead of 6/6?**
   - *Defense:* Symmetrical 6/6 and centered H1s create passive, generic layouts. Asymmetry guides the eye naturally from technical narrative to technical schematic.
4. **How is accessibility guaranteed?**
   - *Defense:* All text combinations meet WCAG AA or AAA standards. Interactive elements have 2px offset amber focus rings. Color is never used as the sole indicator of state (status chips pair colored dots with explicit monospaced labels).