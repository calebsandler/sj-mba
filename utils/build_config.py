"""
Configuration for which files to convert to HTML.

Only files that make sense to read in a browser should be listed here.
Working notes, prompts, and reference materials can be skipped.
"""

# Files to convert to HTML (relative to project root)
# These are the "deliverable" documents worth reading in browser
FILES_TO_CONVERT = [
    # 1. Source materials (the case)
    "1-source/home-depot-case.md",
    "1-source/case-breakdown.md",

    # 2. Analysis (our analysis of the problem)
    "2-analysis/summary.md",
    "2-analysis/root-cause.md",

    # 3. Research (supporting data)
    "3-research/findings.md",
    "3-research/data-benchmarks.md",

    # 4. Solution (main deliverables)
    "4-solution/proposal.md",
    "4-solution/strategic-framing.md",
    "4-solution/financial-analysis.md",
    "4-solution/technical-approach.md",

    # Skip these (working notes, prompts, not for reading):
    # - 3-research/deep-research-prompt.md (instructions for agents)
    # - 3-research/gap-analysis.md (working checklist)
    # - 4-solution/group-position/* (separate group's work)
    # - brand/brand-guidelines.md (reference, not a deliverable)
]
