# Home Depot Case - Plain Language Breakdown

## Part 1: Glossary (What Do These Terms Mean?)

### Business/Org Terms

| Term | Plain English |
|------|---------------|
| **Vertical Team** | A product team that owns one specific area (like "Search" or "Mobile App"). They work top-to-bottom on their thing. |
| **OKR** | Objectives & Key Results. Basically: "What are we trying to achieve?" (objective) and "How do we measure success?" (key results). Each team has their own. |
| **Delivery Rate** | % of planned features that actually shipped on time. 65% means they only finished 65% of what they planned. |
| **Redundancy Rate** | % of a team's work that overlaps with another team's work. 45% redundancy = nearly half their work duplicates someone else's. |
| **Enterprise Coherence** | Everything working together as one system, not a bunch of disconnected pieces. |
| **Capability Collision** | When two products/features conflict with each other (give contradictory advice, fight for screen space, etc.) |

### Tech Terms

| Term | Plain English |
|------|---------------|
| **AI Model** | Software that makes predictions/recommendations (e.g., "you might like this product"). Each team has their own models. |
| **Tech Stack** | The set of technologies a team uses. Different stacks = hard to connect systems. |
| **API** | A way for one software system to talk to another. If there's no API, systems can't share data easily. |
| **Real-time sync** | Data updating instantly everywhere. If NOT synced: app says "in stock" but store says "sold out." |

### Products Mentioned

| Product | What It Does |
|---------|--------------|
| **Magic Apron** | AI chatbot that helps customers find products, plan projects, get advice. THE FOCUS OF THIS CASE. |
| **Recommendations Engine** | Shows "you might also like" product suggestions on the website |
| **Sponsored Ads (Orange Apron Media)** | Paid ads from vendors that appear on Home Depot's site |
| **Search** | The search bar and results on homedepot.com |
| **Mobile App** | Home Depot's phone app |
| **Pro Experience** | Special tools for contractor/professional customers |
| **Order Completion/Delivery** | Tracks orders and gets products to customers |

### Tools Mentioned (Fictional?)

| Tool | What It Does |
|------|--------------|
| **Dawg Depot Dashboard** | Portfolio planning tool - shows what all teams are working on |
| **Rover** | AI agent that helps search across products/teams |
| **Dawg Document** | Stores architecture diagrams, data definitions, AI model documentation |

---

## Part 2: The Actual Problem (Simple Version)

### What Home Depot Did Right
- Gave each product team independence to move fast
- Built impressive AI-powered tools (Magic Apron chatbot, recommendations, etc.)
- Each individual product works well in isolation

### What's Breaking
**The products don't talk to each other.** When a customer uses multiple products in one journey, they get conflicting information.

### Real Examples from the Case

**Example 1: The Deck Stain Disaster**
```
Customer uses chatbot → "Here are 3 stains for your deck"
Customer drives to store → 2 are out of stock, 1 is on clearance
Store associate → "I have no idea what you're talking about"
Customer → Drives to Lowe's
```
**Why it happened:** Chatbot's inventory data was old. Real inventory system wasn't connected.

**Example 2: The Screen Space Fight**
```
Recommendations team → Puts "best products for you" in prime spot
Sponsored Ads team → Puts paid ad in same prime spot
Result → Ad pushes recommendations below where customers see them
```
**Why it happened:** Nobody defined who "owns" that screen space.

**Example 3: The Duplicate Engine**
```
Magic Apron team needs product recommendations
Recommendations team has an engine for this
BUT → Magic Apron builds their own "lite" version anyway
Result → Two teams doing same work, features don't sync
```
**Why it happened:** Faster to build their own than coordinate with other team.

---

## Part 3: The Constraints (What We CAN'T Do)

The CEO explicitly said:

| Constraint | Why It Matters |
|------------|----------------|
| **No centralization** | Can't create one boss who controls all products. That would slow everything down. |
| **No uniformity** | Can't force everyone to use same tools/processes. Teams need flexibility. |
| **Preserve speed** | Can't add bureaucracy. Teams already "waste too much time in meetings." |
| **Preserve autonomy** | Can't take away teams' decision-making power. |
| **Preserve innovation** | Can't create bottlenecks that stifle creativity. |

**Translation:** We need to fix coordination WITHOUT creating a central authority or slowing anyone down.

---

## Part 4: The Components of the Problem

### Component 1: Organizational Structure
```
         CEO
          │
    ┌─────┼─────┐
    │     │     │
   EVP   EVP   EVP
    │     │     │
   VP    VP    VP
    │     │     │
  Team  Team  Team  ← Each team has own goals, own metrics, own roadmap
```
**Issue:** Vertical silos. Nobody owns the horizontal (customer journey across products).

### Component 2: Incentive System
Each team measured on their own OKRs:
- Ads team: "Maximize ad revenue"
- Recs team: "Maximize clicks on recommendations"
- Chatbot team: "Maximize engagement"

**Issue:** Optimizing YOUR metric can hurt THEIR metric. No shared metric for "overall customer experience."

### Component 3: Data/Technology
- Different teams use different data sources
- Data isn't synced in real-time
- AI models trained independently with different assumptions
- No shared definitions (what IS a "bathroom remodel project"?)

**Issue:** Systems literally don't speak the same language.

### Component 4: Governance
- Top level: Strategy exists ✓
- Bottom level: Teams have autonomy ✓
- Middle level: ??? ← WHO DECIDES when products conflict?

**Issue:** No process for resolving conflicts between teams.

---

## Part 5: What the Case Asks Us to Deliver

### Deliverable 1: Root Cause Analysis
**Question:** WHY are capabilities colliding?
**Need to explain:** The organizational, technical, and governance factors

### Deliverable 2: Strategic Recommendation
**Question:** HOW do we fix it?
**Must include:**
- How AI transforms redundancy from static metric → dynamic coordination
- Specific governance changes
- Shared metrics
- Coordination mechanisms

### Deliverable 3: Financial Analysis
**Question:** What's the cost/benefit?
**Must include:**
- Investment required
- Expected return
- Cost of doing nothing (projected future losses)

### Deliverable 4: Implementation Roadmap
**Question:** HOW do we roll this out?
**Must include:**
- Phased approach (start with Magic Apron, then expand)
- Milestones
- Success metrics
- Decision gates

---

## Part 6: Knowledge Gaps - What We Might Need to Research

### About Home Depot Specifically
| Question | Why It Matters | Researchable? |
|----------|----------------|---------------|
| How big is Home Depot's digital business? | Helps size the financial impact | Yes - public financials |
| What's their actual tech stack? | Validates technical recommendations | Partial - job postings, tech blogs |
| Who are their real competitors? | Lowe's mentioned, others? | Yes - public info |
| What's their customer base split (DIY vs Pro)? | Affects prioritization | Yes - investor reports |

### About the Problem Domain
| Question | Why It Matters | Researchable? |
|----------|----------------|---------------|
| How do other retailers solve this? | Best practices, benchmarks | Yes - case studies, articles |
| What AI coordination tools exist? | Validates solution feasibility | Yes - vendor landscape |
| What's industry standard for "redundancy"? | Context for their 45-50% rates | Maybe - analyst reports |

### About the Technology
| Question | Why It Matters | Researchable? |
|----------|----------------|---------------|
| How do enterprise AI governance frameworks work? | Solution design | Yes - Gartner, tech publications |
| What does "AI coherence layer" look like technically? | Implementation details | Yes - architecture patterns |
| Real-time data synchronization approaches? | Technical feasibility | Yes - engineering resources |

---

## Part 7: Key Numbers from the Case

| Metric | Value | Context |
|--------|-------|---------|
| Magic Apron Delivery Rate | 65% | Flagged as concerning by CEO |
| Recs Redundancy Rate | 45% | Highest redundancy |
| Mobile App Redundancy Rate | 50% | Highest redundancy |
| Pro customer trip cost | $300 | When inventory was wrong |
| 2026 Roadmap effort | 90,900 person-hours | Total planned work |
| Presentation length | 20 min + 10 min Q&A | Our constraint |

---

## Next: What Would Help?

1. **Home Depot public financials** - Size the problem in real dollars
2. **Competitor analysis** - How does Lowe's handle this?
3. **Industry frameworks** - What do analysts say about AI governance?
4. **Technical patterns** - What does an "AI coherence layer" actually look like?
