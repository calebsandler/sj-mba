# Home Depot Case Analysis Summary

## 1. Root Cause Analysis

### The Core Problem
Home Depot's capability collisions are **not execution failures—they're coordination architecture failures**:

- **Decentralized ownership without journey accountability**: Vertical teams own product components but nobody owns the end-to-end customer journey where those components intersect
- **Local OKRs without system constraints**: Each team optimizes rationally for their metrics (ads→revenue, recs→clicks, chatbot→engagement) but no shared metrics for system health
- **Governance gap in the middle**: Clear strategy at top, team autonomy at bottom, but no governance where capabilities overlap
- **AI as fragmentation amplifier**: Parallel AI models deployed independently, trained on different data, generating invisible conflicts

### Three Types of Collisions (Dave's Framework)

| Type | Example | Root Cause |
|------|---------|------------|
| **Direct conflict** | Sponsored Ads bumps Recs below fold | Competing for same screen space; no page ownership defined |
| **Parallel development** | Magic Apron builds "Recs lite" | Teams untied operationally; faster to duplicate than coordinate |
| **Tech stack stalemate** | Human Agent chat vs Magic Apron | Different stacks, non-overlapping OKRs; no incentive to integrate |

### Alex's Critical Insight
> "Redundancy rates are static snapshots, while capability collisions are interactional and temporal phenomena that emerge through use."

Current metrics can't detect collisions because they measure what teams *say* they're doing, not what AI systems are *actually deciding* in real-time.

---

## 2. Stakeholder Map

### Executive Level
| Stakeholder | Optimizes For | Key Constraint |
|-------------|---------------|----------------|
| **CEO** | Enterprise coherence + speed | "No uniformity or centralization" |
| **Sam (EVP Digital)** | Cross-product integration | Must preserve decentralized model |

### VP Level Tensions
| VP | OKRs | Collision Points |
|----|------|------------------|
| **VP Data Science** (Magic Apron) | Engagement, AI Sales | Depends on 5+ other teams; inventory sync failures |
| **VP Delivery** (Dave) | Completion rate, CSAT | Downstream recipient of upstream collisions |
| **VP Online** (Recs, Search, App) | Clicks, Downloads | Highest redundancy (45-50%); unclear ownership |
| **Sponsored Ads** | Ad Revenue | Direct conflict with Recs for screen real estate |
| **VP Pro** | Accounts, Pro Sales | Inventory mismatch; fragmented delivery tracking |

### Ground Level
- **Maria (Store Manager)**: "Five tools that each think they're the only one in the store"
- **Associates**: Apologizing for "digital promises the store can't keep"
- **Customers**: Lost trust, defected to Lowe's

---

## 3. Financial Impact Data

### Quantified Costs
| Category | Evidence |
|----------|----------|
| **Customer trip waste** | $300 per Pro customer (inventory mismatch) |
| **Engineering duplication** | 90,900 person-hours in 2026 roadmap |
| **Redundancy rates** | Mobile App 50%, Recs 45%, Ads 30% |
| **Customer defection** | "I drove to Lowe's" (explicit competitor loss) |

### Cost Categories (Finance Team)
1. **Revenue leakage** - declining conversion from inconsistent experiences
2. **Duplicated engineering** - parallel capabilities vs shared assets
3. **Customer service volume** - fulfillment errors from conflicting recs
4. **Incident losses** - AI models with contradictory signals

### Hidden Costs
- Associate morale ("Orange Apron fatigue")
- Leadership attention diverted from growth
- Customer trust erosion (harder to measure, material impact)
- AI collisions "less visible and harder to unwind"

---

## 4. AI Solution Framework

### Sam's Vision: AI-Powered Coherence Layer
> "Continuously monitor interactions between products—flagging when recommendation logic from one team conflicted with optimization rules from another before the collision reached customers"

### Required Capabilities

#### A. Real-Time Detection
1. **Decision provenance tracking** - log every AI decision (model, data, objective, confidence)
2. **Cross-model signal reconciliation** - detect when models pull in opposite directions
3. **Data currency monitoring** - flag when models use stale/divergent data
4. **Customer journey collision detection** - track contradictions across touchpoints

#### B. Prevention (Guardrails)
5. **Shared semantic model** - unified definitions across all AI systems
6. **Dynamic conflict resolution** - AI arbitrator when models conflict
7. **Cross-team dependency validation** - pre-deployment collision checks
8. **Governance automation** - bounded autonomy with system health constraints

#### C. Resolution (Adaptive)
9. **Dynamic recommendation blending** - intelligently combine conflicting outputs
10. **Incident response orchestration** - real-time remediation when collisions occur
11. **Continuous alignment service** - detect model drift before it surfaces
12. **Customer coherence scoring** - replace static redundancy with live metric

### The Transformation
| From (Static) | To (Dynamic) |
|---------------|--------------|
| Quarterly redundancy rates | Continuous coherence monitoring |
| Post-hoc problem identification | Real-time collision detection |
| Team-level surveys | Decision-level AI tracking |
| Manual governance reviews | Automated conflict flagging |

---

## 5. Strategic Constraints (CEO's Requirements)

Any solution must:
- Preserve speed, autonomy, and innovation
- NOT revert to uniformity or centralization
- NOT add significant administrative burden
- Focus on Magic Apron first, then scale

---

## 6. Key Quotes for Presentation

**On the problem:**
> "We've optimized for product autonomy so much that we've lost system harmony. We've given everyone a compass, but no one is using the same map." — Sam

**On customer impact:**
> "When our digital tools give conflicting advice, my associates look like they don't know their own products." — Maria

**On AI risk:**
> "AI does not necessarily create new redundancy, it multiplies the speed, scale, and impact of redundancy." — Sam

**On the solution direction:**
> "An investment in AI is a productive avenue to help address the core limitation of treating redundancy rates as a static, product-level signal rather than a dynamic, system-level phenomenon." — Alex

---

## Next Steps for Case Deliverables

1. **Root cause section**: Use the 7 structural conditions framework
2. **Strategic recommendation**: AI coherence layer with specific capabilities
3. **Financial analysis**: Build cost model from data above + projection of continued collision costs
4. **Implementation roadmap**: Phase 1 Magic Apron pilot → Phase 2 scale to other products
