# Research Prompt: Home Depot Capability Collision Case

> **Purpose:** For deep research agents (Perplexity, Gemini, ChatGPT, etc.)
> **Primary Mode:** Validation of our strategic approach
> **Secondary Mode:** Exploration of new information
> **Last Updated:** February 2026

---

## Context

We're developing a strategic recommendation for an MBA case competition focused on Home Depot's "capability collision" problem — where autonomous digital product teams (chatbot, recommendations, ads, search, delivery) optimize independently and create customer friction.

**Our proposed solution:** A lightweight "visibility layer" that lets teams see each other's customer-facing decisions in real-time, enabling coordination without centralizing control.

**The CEO's constraints:** No centralization, preserve team autonomy, preserve speed, no bureaucracy.

---

## Research Modes

### 🎯 PRIMARY: Validation Mode

Your main job is to **validate or challenge** our approach. We have a hypothesis — help us test it.

### 🔍 SECONDARY: Exploration Mode

If you find something unexpected or important that we didn't ask about, include it. Good research surfaces what we didn't know to ask.

---

## What We've Already Established ✅

**Don't spend time on these unless you find contradicting information:**

| Topic | What We Know | Source |
|-------|--------------|--------|
| HD Revenue | $159.5B (FY2024) | Annual Report |
| HD Online Sales | ~$21B | Digital Commerce 360 |
| HD Tech Investment | ~$4B ICT spend/year | GlobalData |
| HD Technologists | 8,500+ | Former CIO LinkedIn |
| HD CIO | Angie Brown (May 2025) | HD Corporate |
| Magic Apron Launch | March 6, 2025 | HD Corporate |
| Event Streaming Scale | Walmart does 11B events/day | Confluent |
| NPS → Revenue | 7 NPS points = 1% revenue | Temkin/LSE |
| OOS Customer Defection | 43% go to competitor | Mirakl |
| Lowe's Had Similar Issues | Legacy systems, data fragmentation | CDO Magazine |

---

## Validation Questions (Priority Order)

### 1. Solution Pattern Validation ⭐⭐⭐

**Core question:** Has any company successfully implemented coordination/visibility across autonomous teams WITHOUT centralizing control?

**What we need:**
- Case studies of "visibility layers," "coherence layers," or "federated coordination"
- Platform team models that provide visibility without becoming bottlenecks
- "Guardrails not tollgates" implementations
- Event-driven coordination at enterprise retail scale

**Good search terms:**
- `"event-driven architecture" retail coordination decentralized case study`
- `"platform team" retail visibility coordination Spotify model`
- `"data mesh" retail federated governance implementation`
- `"Team Topologies" retail enterprise case study`

**Ideal finding:** "[Company] implemented [approach] to coordinate [X] autonomous teams, achieving [measurable result] while preserving team autonomy."

---

### 2. Home Depot Specific Gaps ⭐⭐⭐

**2a. Pro Customer Economics**

We know Pro = 10% of customers, 50% of sales. We need:
- Pro vs DIY customer lifetime value (CLV) difference
- Pro customer acquisition cost
- Cost of losing a Pro customer

**Search:** `"Home Depot" Pro customer lifetime value CLV revenue`

**2b. Magic Apron Performance**

We know it launched March 2025. We need:
- Usage metrics (sessions, queries, conversion)
- Customer feedback (positive or negative)
- Any reported accuracy issues

**Search:** `"Home Depot" "Magic Apron" usage metrics performance reviews`

**2c. Organization Structure**

We know 8,500+ technologists under CIO Angie Brown. We need:
- How teams are structured (vertical pods? platform teams?)
- Who owns Magic Apron, Recommendations, Search, etc.
- Any public org charts or leadership announcements

**Search:** `"Home Depot" technology organization structure VP digital`

---

### 3. Financial Model Inputs ⭐⭐

**3a. Event Streaming Real Costs**

We estimated $50-150K/year for infrastructure. We need:
- What Walmart, Target, or Sainsbury's actually spent
- Cost per million events at scale
- Operational costs beyond infrastructure

**Search:** `Walmart Kafka event streaming cost investment Confluent`

**3b. Coordination Failure Costs**

We estimated redundancy waste at ~$3M/year. We need:
- Documented cases of coordination failures causing losses
- Industry benchmarks for "cost of misalignment"
- Revenue impact of "digital friction"

**Search:** `retail digital friction revenue impact omnichannel inconsistency cost`

---

### 4. Risk and Failure Cases ⭐⭐

**Core question:** What could go wrong with our approach?

**What we need:**
- Examples of visibility/platform team approaches that failed
- Why event-driven coordination didn't work somewhere
- Organizational resistance patterns
- Unintended consequences

**Search:** `platform team implementation failure case study lessons learned`

**Ideal finding:** "[Company] tried [similar approach] and it failed because [reason]." This helps us anticipate risks.

---

### 5. Lowe's Deep Dive ⭐

**Core question:** What exactly did Lowe's do about their similar problem?

We know Lowe's had legacy systems and data fragmentation. We need:
- Did they centralize or federate?
- What was their specific approach?
- Did it work? What were the results?
- How is Seemantini Godbole's strategy different from HD's?

**Search:** `Lowe's technology transformation 2024 2025 Seemantini Godbole strategy results`

**Why this matters:** If Lowe's centralized and succeeded, we need to explain why HD's decentralized approach is still better. If Lowe's centralized and struggled, that validates our approach.

---

## Exploration Zone (If You Find Something Good)

If you discover important information we didn't ask about, include it. Examples:

- A competitor doing something innovative we should know about
- A new framework or approach relevant to our problem
- Recent HD announcements we missed
- Industry trends affecting our recommendation
- Expert opinions challenging conventional wisdom

Tag these as `[EXPLORATION]` so we know they're bonus findings.

---

## Source Priority

**🟢 Tier 1 — Always prefer:**
- `corporate.homedepot.com`, `ir.homedepot.com`
- SEC filings (10-K, 10-Q, 8-K)
- Earnings call transcripts (direct executive quotes)
- Official partner announcements (Google Cloud, Confluent, etc.)

**🟡 Tier 2 — Good sources:**
- Digital Commerce 360, Supply Chain Dive, Retail Dive, Chain Store Age
- CIO Dive, Marketing Dive
- McKinsey, BCG, Gartner (with methodology)
- Confluent, AWS, Google Cloud case studies

**🟠 Tier 3 — Use with caution (flag as estimate):**
- Analyst reports without methodology
- Aggregators (Statista) — trace to original source
- Blog posts, opinion pieces

**🔴 Tier 4 — Avoid:**
- Unattributed claims
- Content older than 2023 (flag if used)
- Social media speculation
- Sites that don't cite sources

---

## Output Format

```markdown
## [Validation Question #]: [Finding Title]

**Answer:** [Direct answer to the question]

**Evidence:**
- [Specific fact or metric]
- [Supporting data point]

**Source:** [Publication] | [Date] | [URL]

**Verification:** 🟢 VERIFIED / 🟡 CREDIBLE / 🟠 ESTIMATE

**Implication for Our Approach:**
[1-2 sentences: Does this validate, challenge, or refine our strategy?]
```

For exploration findings:
```markdown
## [EXPLORATION]: [Finding Title]

**Discovery:** [What you found]

**Why It Matters:** [Why we should care]

**Source:** [Publication] | [Date] | [URL]
```

---

## Success Criteria

After research, we should be able to confidently answer:

| Question | Needed Confidence |
|----------|-------------------|
| Has "visibility without control" worked elsewhere? | 🟢 Case study confirmed |
| What's Pro vs DIY CLV difference? | 🟢 Data found |
| What did similar event platforms actually cost? | 🟡 Credible estimate |
| How exactly did Lowe's approach this? | 🟢 Specifics confirmed |
| What's the main risk to our approach? | 🟢 Failure case identified |
| Is our financial model reasonable? | 🟡 Benchmarks validated |

---

## The One-Liner

We're proposing to **turn the lights on** so teams can see each other's work — without hiring a traffic cop. Help us prove this works.
