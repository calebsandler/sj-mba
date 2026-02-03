# Root Cause Analysis

## The Core Problem (One Sentence)

Every team is optimizing for their own proxy metric, but all those metrics are downstream of the same thing: **accuracy to reality**.

## Dave's Three Collisions Framework

1. **Data Collision** — Teams using different/stale data sources
2. **Logic Collision** — Conflicting business rules across products
3. **Experience Collision** — Customer sees inconsistent information

## Why Collisions Happen

Teams aren't bad actors. They're building in isolation because:
- No visibility into what other teams are doing
- No shared definition of success
- Each team optimizes for their own OKR
- Data exists in silos — collisions are invisible until they hit the customer

## Current Team Structure & OKRs

| Team | VP | Product | OKR Focus |
|------|-----|---------|-----------|
| Data Science | — | Magic Apron | Engagement, AS Sales |
| Online | — | Recs, Search, App | Clicks, Suggested Sales, Downloads |
| ITS | — | Sponsored Ads | Ad Revenue |
| Delivery | Dave | Order Completion | Completion Rate, CSAT |
| Pro | — | Pro Experience | Accounts, Pro Sales |

## The Hidden Truth

All these OKRs are **downstream** of the same thing:

- Magic Apron engagement is high when it gives **correct** answers
- Rec clicks are high when products are **actually available**
- App downloads stick when inventory is **actually there**
- Pro sales happen when pros **trust** the data
- CSAT is high when orders **complete as promised**

**They all fail for the same reason: divergence from ground truth.**

## The Org Realignment Insight

Not about restructuring reporting lines. It's about adding a **shared North Star**:

> "How close are we to reality?"

Every team keeps their own OKRs. But there's a new shared metric that cuts across all of them — "reality divergence score" or "data accuracy rate."

## CEO Constraint (Critical)

The CEO explicitly forbids:
- Centralization of decision-making
- Slowing teams down
- Taking autonomy away from product teams

**The solution must preserve speed and autonomy while adding coordination.**

## Key Distinction

| Centralized Decisions | Shared Visibility |
|----------------------|-------------------|
| One team tells others what to do | Everyone can see each other's state |
| Kills speed, kills autonomy | Preserves autonomy, reduces collisions |
| CEO says NO | CEO hasn't ruled this out |
