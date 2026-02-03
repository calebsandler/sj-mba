# Strategic Framing: Initial Thoughts

> **Status:** Working draft — capturing thinking before building specifics
> **Date:** February 2026

---

## The Core Insight

From the research and case analysis, one thing is clear:

**Home Depot doesn't have a technology problem. They have a visibility problem.**

The teams are good. The products are good. The AI is working. What's missing is the ability to *see* when independently-good decisions collide in the customer journey.

---

## What We Learned from Research

### 1. This is an Industry Pattern, Not an HD Failure

Lowe's faced the same thing:
- Legacy 1990s systems
- "Dispersed data, hundreds of integration points"
- Teams "spending disproportionate time wrangling data"

Lowe's solution was consolidation and centralization. **HD's CEO has ruled that out.** So we need a different path.

### 2. The Scale is Manageable

| Benchmark | HD Estimate | Industry Proven |
|-----------|-------------|-----------------|
| Daily events | ~72M | Walmart: 11B/day |
| Annual data | ~550 GB | Sainsbury's: 500M events/day |
| Infrastructure cost | $50-150K/year | Standard Kafka/Pub-Sub |

The technical problem is solved. This is about organizational design.

### 3. The Financial Case Writes Itself

| Problem | Quantification |
|---------|----------------|
| Redundancy waste | 45% rate × $6.5M roadmap = ~$3M/year |
| Customer defection from OOS | 43% defect rate; Maria's verbatim validates |
| NPS gap to revenue | HD's 14-point lead = ~$3.2B advantage to protect |
| J.D. Power gap | HD trails by 39 points despite market leadership |

The paradox: HD has higher NPS than Lowe's but lower J.D. Power satisfaction. This suggests:
- Customers *like* HD conceptually (brand strength)
- But *experience* friction in practice (coordination failures)

---

## The CEO's Constraints (Non-Negotiable)

| Constraint | What It Means | Implication |
|------------|---------------|-------------|
| No centralization | Can't create central authority | Solution must be distributed |
| No uniformity | Can't force single tech stack | Solution must be additive |
| Preserve speed | Can't add bureaucracy | Solution must be lightweight |
| Preserve autonomy | Can't take away team decisions | Solution must be visibility, not control |
| Preserve innovation | Can't create bottlenecks | Solution must enable, not constrain |

**Translation:** We need to add *awareness* without adding *approval gates*.

---

## The Mental Model Shift

### Current State: "Compass Without Map"

> "We've given everyone a compass, but no one is using the same map." — Sam

Each team has:
- Clear objectives ✓
- Strong metrics ✓
- Autonomy to execute ✓

What's missing:
- Visibility into adjacent teams' decisions
- Shared understanding of "ground truth"
- Real-time awareness of conflicts

### Future State: "Shared Radar"

Teams keep their compass (autonomy). We add a shared radar (visibility) that shows:
- What other teams are telling customers right now
- Where signals diverge from reality
- Where decisions conflict

---

## Three Types of Collisions (Dave's Framework)

| Type | Example | Root Cause |
|------|---------|------------|
| **Ownership collision** | Sponsored ads bump recommendations below fold | No defined priority for screen space |
| **Capability collision** | Magic Apron builds "Recs lite" | Faster to duplicate than coordinate |
| **Tech stack collision** | Human agent chat vs Magic Apron stalemate | No incentive to resolve |

Each type needs a different intervention:
1. Ownership → Governance (who decides)
2. Capability → Visibility (what exists)
3. Tech stack → Economics (make coordination cheaper than duplication)

---

## What "AI Transforming Redundancy" Means

The case explicitly asks us to show how AI transforms redundancy from a "static, product-level signal" to a "dynamic, system-level phenomenon."

### Current: Static Redundancy Rate
- Measured quarterly
- Product-by-product snapshot
- Tells you *that* overlap exists
- Doesn't tell you *when* or *why* it becomes harmful

### Future: Dynamic Collision Detection
- Measured in real-time
- System-level interactions
- Tells you *when* conflicts reach customers
- Shows *which* collisions cause harm
- Surfaces patterns across products

**The AI layer doesn't replace human judgment — it makes conflicts visible so humans can act.**

---

## Open Strategic Questions

### 1. Where to Start?

| Option | Pros | Cons |
|--------|------|------|
| Magic Apron + Inventory | Highest visibility collision (case focus) | Complex multi-system integration |
| Magic Apron + Recs | Capability overlap is clearest | Less customer-facing impact |
| Recs + Sponsored Ads | Screen space conflict is tangible | Political sensitivity (ad revenue) |

**Initial thinking:** Magic Apron + Inventory — most direct customer impact, aligns with case narrative.

### 2. What's the Governance Model?

| Option | Description | Risk |
|--------|-------------|------|
| New "coherence team" | Dedicated team owns visibility layer | Could become bottleneck |
| Rotating ownership | Teams take turns | Diffused accountability |
| Platform team model | Provides service, teams consume | Requires buy-in |

**Initial thinking:** Platform team model — aligns with Team Topologies "X-as-a-Service" interaction mode.

### 3. What's the Shared Metric?

| Option | Description | Measurable? |
|--------|-------------|-------------|
| "Accuracy to Reality" | How often customer-facing signals match ground truth | Yes — event comparison |
| "Collision Rate" | % of customer interactions with conflicts | Yes — event analysis |
| "Resolution Time" | How fast conflicts get fixed once detected | Yes — timestamp delta |
| "Customer Impact Score" | Weighted by severity and customer segment | Harder — needs definition |

**Initial thinking:** Start with "Collision Rate" — simple, measurable, actionable.

### 4. How to Get Buy-In?

Teams might resist because:
- "More work for me"
- "You're watching us"
- "This will slow us down"

Counter-narrative:
- "This protects your work from being undermined by other teams"
- "This gives you visibility into what's breaking your metrics"
- "This is guardrails, not tollgates"

---

## What We're NOT Proposing

| We're NOT saying... | We ARE saying... |
|---------------------|------------------|
| Teams are bad | Teams are locally optimized without system visibility |
| Centralize everything | Add visibility without central control |
| Slow down | Illuminate without blocking |
| Rebuild systems | Add lightweight event layer |
| Replace AI models | Use AI to detect conflicts between models |
| Create bureaucracy | Create transparency |

---

## Financial Framing (Directional)

### Investment Required

| Phase | Duration | Cost Range |
|-------|----------|------------|
| MVP (Magic Apron + Inventory) | 3 months | $300-500K |
| Expansion (+ Recs, Ads) | 3 months | $400-600K |
| Maturation (AI analysis) | 6 months | $500-800K |
| **Year 1 Total** | — | **$1.2-1.9M** |

### Savings Potential

| Source | Calculation | Range |
|--------|-------------|-------|
| Redundancy reduction | 20% of $3M wasted = $600K | $400K-800K |
| OOS-related defection | 10% reduction of $63M attributable = $6.3M | $3-10M |
| Support cost reduction | 10% of coordination-caused calls | $50-100K |
| **Year 1 Total** | — | **$3.5-11M** |

### ROI Summary

- Investment: ~$1.5M
- Conservative savings: ~$3.5M
- Payback: <6 months

---

## Next Steps (Not Yet)

1. Define specific event schema
2. Map integration points for MVP
3. Design conflict detection rules
4. Build governance proposal
5. Create implementation timeline
6. Develop change management approach

**But first:** Validate this framing with the full team. Make sure we're solving the right problem before building the right solution.

---

## One-Liner Summary

**We're proposing to turn the lights on in a dark room — so teams can see each other's work and avoid stepping on each other — without hiring a traffic cop.**
