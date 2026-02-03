# Technical Approach: Visibility Layer Architecture

> **Purpose:** Detailed technical specification for implementing the visibility layer — event schema, architecture, integration points, AI capabilities, and MVP scope.

---

## 1. Architecture Overview

### System Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         VISIBILITY LAYER                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐              │
│   │ Magic Apron  │    │    Recs/     │    │  Sponsored   │              │
│   │   Chatbot    │    │   Search     │    │     Ads      │              │
│   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘              │
│          │                   │                   │                       │
│          ▼                   ▼                   ▼                       │
│   ┌──────────────────────────────────────────────────────┐              │
│   │              EVENT STREAM (Kafka/Pub-Sub)            │              │
│   │                                                      │              │
│   │  Topics:  /product-surfaced  /price-shown            │              │
│   │          /inventory-claimed  /recommendation-made    │              │
│   └──────────────────────┬───────────────────────────────┘              │
│                          │                                               │
│          ┌───────────────┼───────────────┐                              │
│          ▼               ▼               ▼                              │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                       │
│   │  Real-Time  │ │   Conflict  │ │     AI      │                       │
│   │   Monitor   │ │  Detector   │ │  Analyzer   │                       │
│   │  (< 100ms)  │ │  (< 500ms)  │ │   (async)   │                       │
│   └──────┬──────┘ └──────┬──────┘ └──────┬──────┘                       │
│          │               │               │                              │
│          ▼               ▼               ▼                              │
│   ┌─────────────────────────────────────────────────────┐               │
│   │                 OUTPUTS                              │               │
│   │  • Dashboard (cross-team visibility)                 │               │
│   │  • Alerts (Slack, PagerDuty, email)                 │               │
│   │  • Metrics API (for OKR tracking)                   │               │
│   │  • Weekly Pattern Reports                           │               │
│   └─────────────────────────────────────────────────────┘               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

                              ▲
                              │
              ┌───────────────┴───────────────┐
              │      GROUND TRUTH SOURCES      │
              │  • Inventory System (ERP)      │
              │  • Pricing Service             │
              │  • Store POS Data              │
              └───────────────────────────────┘
```

### Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Non-blocking** | All processing is async; teams never wait for visibility layer |
| **Schema-light** | Minimal required fields; teams can add optional metadata |
| **Fail-safe** | If visibility layer is down, products continue working |
| **Observable** | Layer itself emits metrics for monitoring |
| **Ephemeral** | Events expire after 7 days; this is not a data warehouse |

---

## 2. Event Schema Definition

### Core Event Structure

Every event published to the visibility layer follows this schema:

```json
{
  "event_id": "uuid-v4",
  "event_type": "product_surfaced | price_shown | inventory_claimed | recommendation_made",
  "timestamp": "2026-02-03T14:30:00.000Z",
  "source": {
    "team": "magic_apron | recs | search | sponsored_ads | inventory | mobile_app",
    "service": "chatbot-v2.1",
    "environment": "production"
  },
  "product": {
    "sku": "123456789",
    "price_shown": 29.99,
    "availability_claimed": "in_stock | limited | out_of_stock",
    "store_id": "0123",
    "quantity_claimed": 5
  },
  "customer_context": {
    "session_id": "hashed-session-id",
    "customer_segment": "diy | pro",
    "channel": "web | mobile_app | chatbot"
  },
  "metadata": {
    "confidence_score": 0.95,
    "model_version": "recs-v3.2",
    "custom_fields": {}
  }
}
```

### Required Fields (5 Core Fields)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `sku` | string | Product identifier | "123456789" |
| `price_shown` | decimal | Price displayed to customer | 29.99 |
| `availability_claimed` | enum | Inventory status shown | "in_stock" |
| `store_id` | string | Store location | "0123" |
| `timestamp` | ISO8601 | When customer saw this | "2026-02-03T14:30:00Z" |

### Event Types by Team

| Team | Event Types Published | Trigger |
|------|----------------------|---------|
| **Magic Apron** | `product_surfaced`, `price_shown`, `inventory_claimed` | Chatbot recommends a product |
| **Recommendations** | `recommendation_made`, `price_shown` | Rec carousel rendered |
| **Search** | `product_surfaced`, `price_shown` | Search results displayed |
| **Sponsored Ads** | `product_surfaced`, `price_shown` | Ad impression served |
| **Mobile App** | `product_surfaced`, `inventory_claimed` | Product detail page viewed |
| **Inventory (Ground Truth)** | `inventory_actual`, `price_actual` | Periodic sync (every 5 min) |

### Event Size Estimate

| Component | Size |
|-----------|------|
| Core fields | ~150 bytes |
| Customer context | ~50 bytes |
| Metadata | ~50 bytes |
| JSON overhead | ~50 bytes |
| **Total per event** | **~300 bytes** |

---

## 3. Collision Detection Rules

### Dave's Three Collision Types → Detection Rules

#### Type 1: Data Collision (Different/Stale Data)

**Definition:** Teams using different data sources, resulting in conflicting information.

| Rule ID | Rule Name | Trigger Condition | Severity |
|---------|-----------|-------------------|----------|
| DC-001 | Price Mismatch | `abs(price_shown - price_actual) / price_actual > 0.05` (5% variance) | HIGH |
| DC-002 | Inventory Contradiction | `availability_claimed = "in_stock" AND inventory_actual.quantity = 0` | CRITICAL |
| DC-003 | Stale Data | `timestamp - inventory_actual.last_updated > 30 minutes` | MEDIUM |
| DC-004 | Store Mismatch | `event.store_id != customer_context.preferred_store` | LOW |

**Example:**
```
Magic Apron says: "Deck stain in stock at Store 0123"
Inventory system: Store 0123 quantity = 0
→ Triggers DC-002 (CRITICAL)
```

#### Type 2: Logic Collision (Conflicting Business Rules)

**Definition:** Different products applying conflicting optimization logic.

| Rule ID | Rule Name | Trigger Condition | Severity |
|---------|-----------|-------------------|----------|
| LC-001 | Competing Recommendations | Same SKU recommended by 2+ systems with different prices | HIGH |
| LC-002 | Screen Space Conflict | Sponsored Ad and Organic Rec for same SKU within same session | MEDIUM |
| LC-003 | Contradictory Ranking | Same product ranked #1 by Recs, buried by Search | MEDIUM |
| LC-004 | Promotion Conflict | Different discount shown by different systems | HIGH |

**Example:**
```
Recommendations: Shows "Premium Deck Stain" at $34.99
Sponsored Ads: Shows same SKU at $29.99 (promotional price)
→ Triggers LC-001 and LC-004 (HIGH)
```

#### Type 3: Experience Collision (Inconsistent Customer Experience)

**Definition:** Customer sees conflicting information across touchpoints.

| Rule ID | Rule Name | Trigger Condition | Severity |
|---------|-----------|-------------------|----------|
| EC-001 | Multi-Channel Inconsistency | Same session, same SKU, different price across channels | CRITICAL |
| EC-002 | Journey Fragmentation | Customer sees >3 different product recommendations in single session | MEDIUM |
| EC-003 | Trust Violation | Customer clicks "in stock" → PDP shows "out of stock" | CRITICAL |
| EC-004 | Pro/DIY Mismatch | Pro customer shown DIY-only pricing/products | HIGH |

**Example:**
```
Session 123:
  - Chatbot shows: "Item A, $29.99, in stock"
  - Customer clicks to PDP: "$34.99, limited availability"
→ Triggers EC-001 (CRITICAL) and EC-003 (CRITICAL)
```

### Alert Thresholds

| Severity | Response Time | Notification | Auto-Escalation |
|----------|---------------|--------------|-----------------|
| **CRITICAL** | < 5 minutes | Slack + PagerDuty | After 15 min unresolved |
| **HIGH** | < 30 minutes | Slack channel | After 2 hours |
| **MEDIUM** | < 4 hours | Dashboard + email digest | Weekly review |
| **LOW** | Next business day | Dashboard only | Monthly review |

---

## 4. AI Capabilities

### What AI Detects (That Rules Can't)

| Capability | Description | Technique |
|------------|-------------|-----------|
| **Pattern Mining** | Recurring collision patterns by time/product/team | Process mining on event sequences |
| **Drift Detection** | Model confidence degrading over time | Statistical monitoring of confidence scores |
| **Anomaly Detection** | Unusual collision spikes | Time-series anomaly detection |
| **Root Cause Inference** | Which upstream change caused collisions | Causal inference on event chains |
| **Prediction** | "If Recs deploys v3.3, expect 12% collision increase with Search" | Regression on historical patterns |

### AI Processing Modes

| Mode | Latency | Use Case |
|------|---------|----------|
| **Real-time (streaming)** | < 500ms | Simple rule-based conflict detection |
| **Near real-time (micro-batch)** | 1-5 min | Aggregated anomaly detection |
| **Batch (hourly)** | 1 hour | Pattern mining, process discovery |
| **Batch (daily)** | Overnight | Model retraining, weekly reports |

### Example AI Insights

```
Weekly Pattern Report:

1. RECURRING CONFLICT: Magic Apron + Inventory
   - Every Tuesday 2-4pm, inventory sync delay causes 15% collision spike
   - Root cause: Batch job overlaps with promotional pricing updates
   - Recommendation: Stagger batch jobs by 30 minutes

2. MODEL DRIFT DETECTED: Recommendations Engine
   - Confidence scores down 8% over past 2 weeks
   - Correlated with new seasonal inventory
   - Recommendation: Retrain with Q1 data

3. PREDICTION: Sponsored Ads Campaign Launch
   - New campaign starting Monday targets 500 SKUs
   - Historical pattern: 23% collision rate with Recs for same SKUs
   - Recommendation: Coordinate with Recs team before launch
```

---

## 5. Integration Points by Team

### Magic Apron (Chatbot)

| Integration Point | Method | Effort |
|-------------------|--------|--------|
| Publish `product_surfaced` | Add event emission after recommendation response | 2-3 days |
| Publish `inventory_claimed` | Emit when chatbot asserts availability | 1-2 days |
| Consume conflict alerts | Subscribe to Slack channel or webhook | 1 day |

**Code Change (Pseudocode):**
```python
def recommend_product(user_query, session_id):
    product = get_recommendation(user_query)

    # NEW: Publish to visibility layer
    visibility_layer.publish({
        "event_type": "product_surfaced",
        "sku": product.sku,
        "price_shown": product.price,
        "availability_claimed": product.availability,
        "store_id": user.preferred_store,
        "source": {"team": "magic_apron", "service": "chatbot-v2.1"}
    })

    return product
```

### Recommendations Engine

| Integration Point | Method | Effort |
|-------------------|--------|--------|
| Publish `recommendation_made` | Emit on carousel render | 2-3 days |
| Consume collision feedback | API to query conflicts involving Recs | 3-5 days |

### Inventory System (Ground Truth)

| Integration Point | Method | Effort |
|-------------------|--------|--------|
| Publish `inventory_actual` | Periodic sync every 5 minutes | 3-5 days |
| Real-time updates | Change data capture (CDC) on inventory DB | 1-2 weeks |

### Sponsored Ads

| Integration Point | Method | Effort |
|-------------------|--------|--------|
| Publish `ad_impression` | Emit on ad serve | 2-3 days |
| Pre-flight check (optional) | Query visibility layer before serving ad | 1 week |

---

## 6. Volume & Scale

### Clarifying Event Volume

The visibility layer handles a **subset** of all digital events — only customer-facing product decisions:

| Event Category | Daily Volume | In Scope? | Notes |
|----------------|-------------:|-----------|-------|
| Total web events | 72M+ | No | Raw clickstream, not needed |
| Product recommendations served | 50M | **Yes** | Core collision detection |
| Search results shown | 5M | **Yes** | Product surfacing events |
| Chatbot interactions | ~500K-1M | **Yes** | Magic Apron focus |
| Inventory ground truth | 5M | **Yes** | Sync events |
| **Total in-scope events** | **~60-65M/day** | — | — |

### Infrastructure Sizing

| Metric | Value |
|--------|-------|
| Events per second (peak) | ~1,500/sec |
| Events per second (average) | ~750/sec |
| Daily data volume | ~18-20 GB |
| Monthly data volume | ~550-600 GB |
| Retention period | 7 days |
| Storage required | ~140 GB (7 days × 20 GB) |

### Platform Recommendation

**Primary: Google Cloud Pub/Sub** (HD's existing cloud partner)

| Component | Specification |
|-----------|---------------|
| Pub/Sub topics | 4 (product_surfaced, price_shown, inventory_actual, conflicts) |
| Subscriptions | 6 (one per consumer service) |
| Message retention | 7 days |
| Dead letter queue | Yes, for failed processing |

**Alternative: Apache Kafka (self-managed or Confluent)**
- Better for complex stream processing
- Higher operational overhead
- Consider if Pub/Sub latency becomes an issue

---

## 7. MVP Technical Scope

### Phase 1: Instrument (Weeks 1-4)

:::timeline
**Week 1**: Define event schema, set up Pub/Sub topics, create conflict detector skeleton
**Week 2**: Instrument Magic Apron to publish events (3 event types)
**Week 3**: Connect Inventory system as ground truth source
**Week 4**: Implement DC-001 (price mismatch) and DC-002 (inventory contradiction) rules
:::

**Deliverables:**
- [ ] Event schema finalized and documented
- [ ] Pub/Sub infrastructure deployed
- [ ] Magic Apron publishing events to stream
- [ ] Inventory system publishing ground truth
- [ ] 2 collision detection rules active

### Phase 2: Visibility (Weeks 5-8)

:::timeline
**Week 5**: Build dashboard showing real-time conflict rate
**Week 6**: Implement alert system (Slack integration)
**Week 7**: Add historical conflict viewer (7-day lookback)
**Week 8**: Create "Accuracy to Reality" OKR metrics API
:::

**Deliverables:**
- [ ] Dashboard with real-time conflict visualization
- [ ] Slack alerts for CRITICAL and HIGH severity
- [ ] Conflict drill-down by team, product, time
- [ ] API endpoint for OKR tracking

### Phase 3: AI Analysis (Weeks 9-12)

:::timeline
**Week 9**: Implement batch pattern mining job
**Week 10**: Build anomaly detection for collision spikes
**Week 11**: Create weekly pattern report generator
**Week 12**: Test, iterate, prepare for expansion
:::

**Deliverables:**
- [ ] Weekly automated pattern report
- [ ] Anomaly alerts for unusual collision spikes
- [ ] Root cause suggestions for recurring conflicts

### Phase 4: Expand (Months 4-6)

- Add Recommendations engine to event stream
- Add Search to event stream
- Add Sponsored Ads with pre-flight conflict check
- Implement logic collision rules (LC-001 through LC-004)
- Expand AI to predictive capabilities

---

## 8. Security & Privacy

### Data Handling

| Concern | Approach |
|---------|----------|
| **PII** | No customer PII in events; session_id is hashed |
| **Pricing data** | Internal only; not exposed externally |
| **Access control** | Teams can only query conflicts involving their events |
| **Retention** | 7 days max; automatic expiration |
| **Audit logging** | All queries logged for compliance |

### Network Security

- Events flow within HD's VPC (no public internet)
- Pub/Sub IAM controls per topic
- Encryption in transit (TLS) and at rest

---

## 9. Success Metrics

### Technical Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Event ingestion latency | < 100ms (p99) | Pub/Sub metrics |
| Conflict detection latency | < 500ms (p99) | Custom instrumentation |
| System availability | 99.9% | Uptime monitoring |
| False positive rate | < 5% | Manual review sample |

### Business Metrics

| Metric | Baseline | Target (6 months) |
|--------|----------|-------------------|
| Conflict rate (Magic Apron + Inventory) | Unknown (establish in Month 1) | -50% from baseline |
| Mean time to detect conflict | N/A (currently post-hoc) | < 5 minutes |
| Redundancy rate | 35-45% | -20% (relative) |

---

## 10. Open Technical Questions

- [ ] **Real-time blocking vs. logging-only?** Start with logging; add optional blocking for CRITICAL conflicts after validation period
- [ ] **Schema versioning strategy?** Use schema registry (Confluent or custom) to manage evolution
- [ ] **Backfill historical data?** Probably not — start fresh, establish baseline going forward
- [ ] **Multi-region deployment?** Start single-region; expand if latency becomes an issue
- [ ] **Integration with existing observability?** Emit metrics to existing DataDog/Grafana stack

---

## Appendix: Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Event streaming | Google Cloud Pub/Sub | HD's cloud partner; managed service |
| Stream processing | Cloud Dataflow (Apache Beam) | Serverless, auto-scaling |
| Conflict rules engine | Custom Python service | Flexibility for complex rules |
| AI/ML | Vertex AI | Integrated with GCP; managed training |
| Dashboard | Looker or custom React | HD likely has existing BI tools |
| Alerting | Slack + PagerDuty | Standard enterprise tooling |
| Storage (if needed) | BigQuery | For historical analysis beyond 7 days |
