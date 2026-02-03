# Solution Proposal: Visibility Layer

## Concept (One Sentence)

A lightweight event stream where teams publish their customer-facing decisions, enabling real-time conflict detection without centralizing decision-making power.

## What It Is / What It Isn't

| It IS | It ISN'T |
|-------|----------|
| Event stream (ephemeral) | Data warehouse (permanent) |
| Conflict detection | Conflict resolution |
| Shared visibility | Centralized control |
| Additive layer | Replacement of existing systems |
| Schema-light | Complex ETL pipelines |

## How It Works

```
[Magic Apron] ──┐
[Recs/Search] ──┼──▶ Event Stream ──▶ Conflict Detector ──▶ Alerts/Dashboard
[Sponsored]   ──┤         ▲
[Inventory]   ──┘         │
                    AI Analysis Layer
                   (async, not blocking)
```

### What Teams Do
- Publish a lightweight event when surfacing something to a customer
- Event = product ID, price, store, availability, timestamp (~200 bytes)
- That's it. No changes to their databases, models, or workflows.

### What The Layer Does
- Consumes events in real-time
- Checks for conflicts (price mismatch > X%, inventory disagreement, etc.)
- Logs everything, alerts on thresholds
- AI runs async to find patterns over time (process mining)

## The Shared OKR: "Accuracy to Reality"

All teams adopt a new shared metric **alongside** their existing OKRs (not replacing them):

| Metric | Definition | Target (6 Months) |
|--------|------------|-------------------|
| **Conflict Rate** | % of events with detected conflicts | < 2% (from unknown baseline) |
| **Mean Time to Detect** | Time from conflict occurrence to alert | < 5 minutes |
| **Resolution Rate** | % of flagged conflicts addressed within SLA | > 90% within 24 hours |
| **Customer Impact Incidents** | Conflicts that reached customers | < 10 per week |

**How it works with existing OKRs:**
- Teams keep 100% of their current OKRs (engagement, clicks, revenue, etc.)
- "Accuracy to Reality" is an **additional** shared metric visible to all
- No team is penalized for conflicts they didn't cause
- Incentive: teams that reduce conflicts in their domain get recognition

## Technical Feasibility

> **See [Technical Approach](technical-approach.md) for detailed architecture, event schema, and collision detection rules.**

### Scale Math

| Metric | Estimate |
|--------|----------|
| Daily transactions | 4.5 million |
| Events per transaction | 3-5 |
| Event size | ~200 bytes |
| Daily data volume | ~3-5 GB |
| Monthly data volume | ~100-150 GB |

This is trivial for modern event streaming (Kafka, AWS Kinesis, GCP Pub/Sub).

### Why It's Not a Data Warehouse

- Events flow through and expire (7-day retention)
- No ETL — teams just publish
- Schema is thin (5 fields)
- Optimized for real-time, not historical queries
- Cheap, fast, ephemeral

### Spaghetti Prevention

- Schema contracts: each team publishes to a defined format
- Layer rejects malformed events
- Lightweight governance, not integration hell

## Financial Analysis

> **See [Financial Analysis](financial-analysis.md) for detailed projections, scenarios, and assumptions.**

### Investment Summary

| Period | Cost |
|--------|------|
| Year 1 (Build) | $1.2-1.5M |
| Year 2+ (Operate) | $400-600K |
| **3-Year Total** | **$2.3M** |

### Cost of Doing Nothing (3-Year)

| Problem | Annual Cost | 3-Year Total |
|---------|-------------|--------------|
| Engineering redundancy (35-45% overlap) | $2.6M | $9M |
| Customer service friction | $660K | $2.3M |
| OOS-related revenue loss | $6.3M | $22M |
| **Known costs** | **$9.6M** | **$33M** |
| Customer defection risk | $159M at risk | — |

### ROI

| Metric | Value |
|--------|-------|
| 3-Year Net Benefit | $6-8M (moderate case) |
| Payback Period | 5-7 months |
| 3-Year ROI | 147% |
| NPV (10% discount) | $3M+ |

**Even in the worst case scenario, ROI is positive.**

## MVP Scope

**Start with the highest-conflict pair from the case:** Magic Apron + Inventory/Pricing

### What We Build (Weeks 1-12)

1. Instrument Magic Apron to publish price/availability events
2. Instrument Inventory system to publish ground truth (every 5 min)
3. Build conflict detector for:
   - Price mismatches > 5%
   - Inventory contradictions (chatbot says "in stock", system says 0)
4. Dashboard showing conflict rate, examples, trends
5. Slack alerts when conflicts spike

### Success Criteria (Go/No-Go for Expansion)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Events flowing | > 1M events/day from Magic Apron | Pub/Sub metrics |
| Conflict detection working | Detect > 95% of known test conflicts | Synthetic tests |
| False positive rate | < 10% | Manual review of 100 alerts |
| Mean time to detect | < 5 minutes | Timestamp comparison |
| Team adoption | Both teams acknowledge alerts within 24h | Alert response tracking |

**Decision gate at Week 12:** If targets met → expand to Recs/Search. If not → iterate on MVP.

## Implementation Roadmap

### Phase 1: Instrument (Weeks 1-4)
- Define event schema
- Magic Apron + Inventory publish to stream
- Basic conflict detection rules

### Phase 2: Visibility (Weeks 5-8)
- Dashboard for cross-team visibility
- Alert system for threshold breaches
- Shared OKR tracking

### Phase 3: AI Analysis (Weeks 9-12)
- Batch processing for pattern detection
- Process mining on historical events
- Automated escalation for ambiguous conflicts

### Phase 4: Expand (Months 4-6)
- Add Recs/Search to event stream
- Add Sponsored Ads
- Refine conflict rules based on learnings

## Why This Works

1. **Preserves autonomy** — Teams keep their tech, data, decisions. Zero changes to existing systems.
2. **Guardrails, not tollgates** — Like Amazon's two-pizza teams: teams move fast with safety rails, not approval gates.
3. **Non-threatening** — Framing: "Turn the lights on so you can see what's breaking your metrics" not "you're doing it wrong."
4. **Incremental** — Start with one pair (Magic Apron + Inventory), prove value, then expand.
5. **Cheap** — $1.2M Year 1 is < 0.001% of HD's revenue; proven at Walmart scale (11B events/day).
6. **Measurable** — Clear targets: < 2% conflict rate, < 5 min detection, > 90% resolution within 24h.
7. **Reversible** — If it doesn't work after 90 days, turn it off with no residual impact.

## Governance Model

### Who Owns the Visibility Layer?

**New small team (3-5 engineers + 1 PM) reporting to Dave (VP Delivery)**

Why Delivery?
- Closest to ground truth (inventory, fulfillment, completion)
- Already owns the "last mile" where collisions become visible
- Neutral party — not competing for screen space or clicks
- Dave explicitly understands the interface problem ("I get corrupted signals")

### Decision Authority Matrix

| Conflict Type | Detection | First Responder | Decision Authority | Escalation (if unresolved 24h) |
|---------------|-----------|-----------------|-------------------|-------------------------------|
| Price mismatch > 5% | Automated | Pricing team | VP Data Science | Sam (EVP Digital) |
| Inventory contradiction | Automated | Inventory + source team | Dave (Delivery) | Sam |
| Screen space conflict | Dashboard alert | Page owner | VP Online | Sam |
| Cross-team data collision | AI pattern detection | Both teams | Joint decision | Dave as tiebreaker |

### Guardrails, Not Tollgates

**Critical distinction for CEO buy-in:**

| Tollgate (We're NOT doing this) | Guardrail (What we ARE doing) |
|--------------------------------|------------------------------|
| Approval required before shipping | Ship freely; get alerted after conflicts detected |
| Central team decides what's right | Teams decide; layer shows when they disagree |
| Slows deployment velocity | Zero impact on deploy speed |
| Creates bottleneck | Creates visibility |

The visibility layer **never blocks** a team from shipping. It only turns the lights on so teams can see when their work conflicts with others.

### Conflict Resolution Process

```
1. Conflict Detected
   ↓
2. Alert sent to both teams (Slack + Dashboard)
   ↓
3. Teams have 24 hours to:
   a) Acknowledge and fix, OR
   b) Acknowledge and document why it's acceptable, OR
   c) Dispute the conflict detection (false positive)
   ↓
4. If unresolved after 24h → Auto-escalate to decision authority
   ↓
5. Decision authority has 48h to resolve
   ↓
6. If still unresolved → Escalate to Sam
```

### Rollback Plan

If the visibility layer causes problems:

| Scenario | Response | Timeline |
|----------|----------|----------|
| False positive rate > 20% | Loosen detection thresholds | 1 day |
| Teams overwhelmed by alerts | Increase severity thresholds, reduce alert volume | 1 day |
| Performance impact on source systems | Reduce event frequency or make async | 1 week |
| Fundamental approach not working | Pause expansion, evaluate after 90 days | 90 days |

**Abort criteria:** If after 90 days the conflict rate hasn't improved AND teams report negative productivity impact, recommend discontinuation.
