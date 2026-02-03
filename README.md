# Home Depot MBA Case Study

> **UGA Terry College Case Competition 2026**
> "When Digital Capabilities Collide"

---

## Getting Started (New Contributors)

### Prerequisites

1. **Create a GitHub Account** at [github.com/signup](https://github.com/signup)

2. **Install Homebrew** (Mac package manager):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   > After installation, restart Terminal and run the two PATH commands it shows you.

### Install AI Coding Tools

```bash
# Google Antigravity (VS Code fork with Gemini)
brew install --cask antigravity

# Cursor (AI-powered IDE with Claude/GPT)
brew install --cask cursor

# GitHub CLI (for cloning repos)
brew install gh
```

| Tool            | What it does                                 |
| --------------- | -------------------------------------------- |
| **Antigravity** | Google's AI-powered IDE with Gemini built-in |
| **Cursor**      | AI-powered IDE with Claude/GPT integration   |
| **GitHub CLI**  | Interact with GitHub from your terminal      |

### Get Free Student Access

| Tool                | How to get it                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------ |
| **Cursor Pro**      | [cursor.com/students](https://cursor.com/students) — Free for 1 year with .edu email       |
| **Gemini Advanced** | [gemini.google/students](https://gemini.google/students/) — Free with student verification |

### Clone This Repo

```bash
# Authenticate with GitHub
gh auth login
# Choose: GitHub.com → HTTPS → Login with a web browser

# Clone the repo
gh repo clone YOUR_USERNAME/sj-mba
cd sj-mba

# Open in your IDE
cursor .       # or
antigravity .
```

### Troubleshooting

- Restart Terminal after installing Homebrew
- Run `brew doctor` to check for issues
- Text me if something doesn't work!

---

## Content Quick Start

**Best place to start:** Open [`1-source/case-interactive.html`](1-source/case-interactive.html) in your browser for a visual overview of the entire case.

**For the solution:** Read [`4-solution/proposal.md`](4-solution/proposal.md) or open [`4-solution/reading/proposal.html`](4-solution/reading/proposal.html).

---

## The Solution in 30 Seconds

**Problem:** Home Depot's digital teams (chatbot, recommendations, ads, search) each work great alone but conflict with each other — customers get contradictory information and defect to Lowe's.

**Constraint:** CEO forbids centralization. Must preserve team autonomy and speed.

**Our Solution:** A "visibility layer" — lightweight event stream where teams publish their customer-facing decisions. Enables real-time conflict detection without centralizing control.

| Metric         | Value                          |
| -------------- | ------------------------------ |
| **Investment** | $1.2M Year 1                   |
| **Returns**    | $6-8M net benefit over 3 years |
| **Payback**    | 5-7 months                     |

---

## Folder Structure

| Folder          | What's Inside               | Start Here                                                           |
| --------------- | --------------------------- | -------------------------------------------------------------------- |
| **1-source/**   | Original case materials     | `case-interactive.html` (visual) or `home-depot-case.md` (full text) |
| **2-analysis/** | Our analysis of the problem | `summary.md`                                                         |
| **3-research/** | Supporting research & data  | `findings.md`                                                        |
| **4-solution/** | Our proposed solution ⭐    | `proposal.md` (main deliverable)                                     |
| **brand/**      | Home Depot visual assets    | `brand-guidelines.md`, `logo.svg`                                    |
| **utils/**      | Build tools (technical)     | `build_html.py`                                                      |

---

## Key Documents

### The Case

- [`1-source/home-depot-case.md`](1-source/home-depot-case.md) — Full case text
- [`1-source/case-interactive.html`](1-source/case-interactive.html) — **Visual overview (start here)**
- [`1-source/case-breakdown.md`](1-source/case-breakdown.md) — Plain language glossary

### Our Analysis

- [`2-analysis/summary.md`](2-analysis/summary.md) — Executive summary of the problem
- [`2-analysis/root-cause.md`](2-analysis/root-cause.md) — Root cause framework

### Research

- [`3-research/findings.md`](3-research/findings.md) — Comprehensive research findings
- [`3-research/data-benchmarks.md`](3-research/data-benchmarks.md) — Quantitative data for financial modeling

### Our Solution (Deliverables)

- [`4-solution/proposal.md`](4-solution/proposal.md) — **Main solution proposal** ⭐
- [`4-solution/financial-analysis.md`](4-solution/financial-analysis.md) — Cost-benefit, ROI, 3-year projections
- [`4-solution/technical-approach.md`](4-solution/technical-approach.md) — Architecture, event schema, implementation
- [`4-solution/strategic-framing.md`](4-solution/strategic-framing.md) — Strategic thinking and framing

---

## Reading the Documents

Each folder has a `reading/` subfolder with browser-friendly versions:

```
4-solution/
├── proposal.md           ← Edit this (source)
└── reading/
    └── proposal.html     ← View this (generated)
```

**To regenerate HTMLs after editing markdown:**

```bash
cd utils && uv run python build_html.py
```

---
