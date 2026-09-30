# CONTENT.md
## Japolic — Landing Page Content
### Single source of copywriting truth

---

## Brand Definition

**One-line description:**
Japolic is a routing layer that enforces protocol compliance between internal services.

---

## Core Capabilities (3)

**1. Protocol Arbitration**
Translates between conflicting internal protocols at the request boundary — HTTP/2,
gRPC, WebSocket — without requiring contract changes from either service.

**2. Policy-Gated Traffic**
Evaluates each request against a versioned ruleset before it reaches the destination.
Rules are written in a declarative config file, diffed in CI, and deployed atomically.

**3. Structured Failure Routing**
When a downstream service returns a defined error class, Japolic routes to a fallback
path or returns a structured error payload instead of surfacing a raw upstream fault.

---

## Primary Audience

Engineers and infrastructure leads at companies running 8–80 internal services, where
the cost of a misconfigured integration has become measurable — in incidents, in
engineer hours, or in customer SLA misses.

Secondary: Platform engineers standardising service interfaces across team-owned
microservices who cannot mandate framework choices per team.

---

## The Problem (sharp, one statement)

**Problem headline (< 10 words):**
> Services talk. Nobody agrees on the rules.

**Expanded (3 sentences — calm, factual):**
Every internal service boundary is a handshake negotiated ad hoc: one team uses REST
with custom error codes, another uses gRPC with Protobuf contracts, a third has a legacy
HTTP/1.1 endpoint that will not be migrated. When these services call each other, the
integration logic lives in application code — duplicated across teams, inconsistently
enforced, and opaque in failure. The result is incidents that trace back not to bad code,
but to boundary assumptions that were never written down.

---

## The Solution

**Solution headline (< 10 words):**
> One routing layer. Consistent rules at every boundary.

**Expanded (3 sentences):**
Japolic sits between services as a lightweight, stateless routing plane. It holds the
protocol negotiation, policy enforcement, and failure handling that currently lives
scattered across application codebases. Each rule is versioned in config, observable in
structured logs, and deployable in under two minutes.

**What it is not:**
Not a service mesh. Not a full API gateway. Not a replacement for your load balancer.
Japolic does one job: make the contract between two internal services explicit, enforced,
and auditable.

---

## Feature Deep-Dive: Policy Plane

**Feature headline (< 10 words):**
> Rules live in config. Violations surface in logs.

**What it is:**
The Policy Plane is Japolic's enforcement engine. You define traffic rules in a
`japolic.rules` YAML file alongside your service manifests. Rules specify: which services
may call which endpoints, under what conditions, with what required headers, and what
constitutes a valid response envelope.

**How it works:**
```
# japolic.rules (example)
route:
  source: payments-service
  destination: ledger-service
  method: POST
  path: /entries
  require-headers:
    - X-Idempotency-Key
    - X-Trace-ID
  response-schema: ./schemas/ledger-entry-response.json
  on-violation: return-structured-error
  error-code: PROTO_VIOLATION_4031
```

**Why it matters:**
- Rules are diffs. Every policy change is a PR, not a Slack message.
- Violations are not crashes. They return a documented error code at the boundary
  before bad data reaches the downstream service.
- No application code change required. Drop in the Japolic sidecar, apply config.
  The services are unaware of the enforcement layer.

**Key detail (for technical credibility):**
Rule evaluation adds < 1.2ms to request latency at p99, measured at 10,000 req/sec
in our internal benchmarks on a 2-core container.

---

## Use Cases (3, with believable metrics)

### Use Case 1 — Platform Team at a Fintech

**Situation:**
A 40-engineer fintech runs 22 internal services. Three teams have independently built
retry logic into their HTTP clients. After a downstream timeout cascade, the post-mortem
traces the failure to inconsistent retry intervals and missing idempotency headers.

**How Japolic is used:**
Platform team defines a single `retry-policy` rule applied globally to all
POST requests. Header requirements are enforced at the boundary. Teams remove their
own retry logic and consume the Japolic error payload instead.

**Outcome:**
- Timeout cascades: 0 in the 90 days following deployment
- Duplicate transaction incidents: reduced from 4/month to 0
- Lines of custom retry/error code removed across codebases: ~1,400

---

### Use Case 2 — Infrastructure Lead During a Protocol Migration

**Situation:**
A backend team is migrating 6 internal services from REST to gRPC over 3 months.
During the migration, callers and providers exist on different protocol versions
simultaneously. Testing the in-between state requires standing up mock services.

**How Japolic is used:**
Japolic's protocol arbitration layer translates gRPC calls to REST for legacy endpoints
during the migration window. The calling service is updated once and speaks only gRPC.
Japolic handles downward translation until each provider completes migration.

**Outcome:**
- Migration time reduced from estimated 6 months to 11 weeks
- Zero breaking changes surfaced to upstream callers during the migration window
- Mock infrastructure removed: 3 internal services decommissioned early

---

### Use Case 3 — On-Call Engineer Debugging a Boundary Failure

**Situation:**
An on-call engineer receives a P2 alert. The error surfaces in service A but originates
at the boundary between service B and service C. Standard logs show a 500 with no
structured payload. Tracing the chain manually takes 40–80 minutes per incident.

**How Japolic is used:**
Every boundary violation produces a structured log entry: source service, destination
service, rule violated, request hash, timestamp, and the response received. The engineer
queries the Japolic log stream with two filters and identifies the root cause in under
5 minutes.

**Outcome:**
- Mean time to boundary-root-cause: 4.5 minutes (previously 52 minutes estimated)
- Incidents requiring cross-team coordination to diagnose: down 60%
- On-call escalations to senior engineers: reduced by half over 8 weeks

---

## Navigation Labels

```
Wordmark:   Japolic

Nav links:
  - Docs
  - Protocol Reference
  - Changelog
  - Pricing

CTA (right):   Request Access →

Mobile nav (390px):
  - Hamburger collapses to: Docs / Protocol Reference / Changelog / Pricing / Request Access
```

---

## Footer Links

```
Column 1 — Product
  Overview
  Protocol Arbitration
  Policy Plane
  Failure Routing
  Changelog

Column 2 — Developers
  Documentation
  Protocol Reference
  API Reference
  SDKs
  Open Source

Column 3 — Company
  About
  Blog
  Security
  Status   (links to status.japolic.io)
  Contact

Column 4 — Legal
  Privacy Policy
  Terms of Service
  Data Processing Agreement

Bottom bar:
  © 2026 Japolic, Inc.  |  All rights reserved.
  [GitHub]  [X / Twitter]  [LinkedIn]
```

---

## Section Labels (for nav reference in design)

```
00 — Nav
01 — Hero
02 — Problem
03 — Solution
04 — Feature: Policy Plane
05 — Use Cases
06 — Footer
```

---

## Tone Reference

- **Use:** "enforces", "routes", "evaluates", "returns", "defines", "produces"
- **Avoid:** "powerful", "seamless", "revolutionary", "robust", "cutting-edge",
  "next-generation", "magic", "plug-and-play", "supercharge"
- **Voice:** A senior platform engineer writing internal documentation — precise,
  confident, no selling.
- **Sentence length:** Max 25 words per sentence in body copy. Headlines max 10 words.
- **Numbers:** Always specific. "< 1.2ms" not "minimal latency". "11 weeks" not "faster".

---

*Compiled: 2026-09-30 | For: Japolic landing page, 1440px + 390px*
*Status: Approved for layout. Do not alter without updating DESIGN.md accordingly.*
