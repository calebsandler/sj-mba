#!/usr/bin/env python3
"""
Home Depot Case Study - Markdown to Branded HTML Builder

Usage:
    python utils/build_html.py                    # Build all markdown files
    python utils/build_html.py solution/proposal.md  # Build specific file
    python utils/build_html.py --watch            # Watch for changes (requires watchdog)

Special markdown syntax supported:
    :::metrics
    65% | Magic Apron Delivery Rate
    45% | Recommendations Redundancy
    :::

    :::card-grid
    ### Card Title
    Card content here
    ---
    ### Another Card
    More content
    :::

    :::quote author="Sam, EVP Digital"
    Quote text here
    :::

    :::flow
    Step 1 -> Step 2 -> Step 3 -> [Result]
    :::

    :::tldr
    Quick summary content
    :::

    :::highlight
    Important highlighted text
    :::
"""

import re
import sys
import os
from pathlib import Path
from datetime import datetime

# Try to import markdown, fall back to basic conversion
try:
    import markdown
    from markdown.extensions import tables, toc, fenced_code
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    print("Warning: 'markdown' package not installed. Using basic conversion.")
    print("Install with: uv add markdown")


# ============================================================================
# HTML TEMPLATE WITH HOME DEPOT BRANDING
# ============================================================================

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Home Depot Case Study</title>
    <style>
        /* Home Depot FY25 Official Brand Colors */
        :root {{
            --hd-orange: #F96302;
            --hd-black: #000000;
            --hd-white: #FFFFFF;
            --hd-gray-dark: #747474;
            --hd-gray-medium: #C4C4C4;
            --hd-gray-light: #F5F5F5;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Helvetica Neue LT Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background: var(--hd-white);
            color: var(--hd-black);
            line-height: 1.6;
            padding: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }}

        /* Headlines - Bold, ALL CAPS for major sections */
        h1 {{
            font-weight: 700;
            letter-spacing: 0.02em;
            text-transform: uppercase;
            color: var(--hd-black);
            padding-bottom: 12px;
            margin-bottom: 24px;
            border-bottom: 4px solid var(--hd-orange);
            font-size: 1.8em;
        }}

        h2 {{
            font-weight: 700;
            letter-spacing: 0.01em;
            text-transform: uppercase;
            color: var(--hd-black);
            margin: 32px 0 16px;
            padding-bottom: 8px;
            border-bottom: 2px solid var(--hd-orange);
            font-size: 1.3em;
        }}

        h3 {{
            font-weight: 700;
            color: var(--hd-black);
            margin: 24px 0 12px;
            font-size: 1.1em;
        }}

        h4 {{
            font-weight: 700;
            color: var(--hd-black);
            margin: 16px 0 8px;
            font-size: 1em;
        }}

        p {{
            color: var(--hd-gray-dark);
            line-height: 1.7;
            margin-bottom: 16px;
        }}

        strong {{
            color: var(--hd-black);
        }}

        a {{
            color: var(--hd-orange);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        ul, ol {{
            margin: 16px 0;
            padding-left: 24px;
            color: var(--hd-gray-dark);
        }}

        li {{
            margin-bottom: 8px;
        }}

        li::marker {{
            color: var(--hd-orange);
        }}

        /* Hero Section */
        .hero {{
            background: var(--hd-gray-light);
            color: var(--hd-black);
            padding: 48px 32px;
            margin: -24px -24px 32px -24px;
            text-align: center;
            border-bottom: 4px solid var(--hd-orange);
        }}

        .hero h1 {{
            border-bottom: none;
            font-size: 2em;
            margin-bottom: 8px;
            padding-bottom: 0;
        }}

        .hero-subtitle {{
            font-size: 1em;
            color: var(--hd-gray-dark);
            margin-bottom: 16px;
        }}

        .hero-date {{
            font-size: 0.85em;
            color: var(--hd-gray-dark);
        }}

        /* Navigation */
        .nav {{
            position: sticky;
            top: 0;
            background: var(--hd-white);
            padding: 12px 0;
            margin-bottom: 24px;
            z-index: 100;
            border-bottom: 2px solid var(--hd-gray-medium);
        }}

        .nav-links {{
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }}

        .nav-links a {{
            color: var(--hd-black);
            padding: 6px 12px;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.8em;
            letter-spacing: 0.02em;
            border: 1px solid transparent;
        }}

        .nav-links a:hover {{
            background: var(--hd-orange);
            color: var(--hd-white);
            text-decoration: none;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}

        th, td {{
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid var(--hd-gray-medium);
        }}

        th {{
            background: var(--hd-black);
            color: var(--hd-white);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 0.02em;
        }}

        td {{
            color: var(--hd-gray-dark);
        }}

        tr:hover {{
            background: var(--hd-gray-light);
        }}

        /* Code blocks */
        code {{
            background: var(--hd-gray-light);
            padding: 2px 6px;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 0.9em;
            border: 1px solid var(--hd-gray-medium);
        }}

        pre {{
            background: var(--hd-black);
            color: var(--hd-white);
            padding: 20px;
            overflow-x: auto;
            margin: 20px 0;
            border-left: 4px solid var(--hd-orange);
        }}

        pre code {{
            background: none;
            border: none;
            padding: 0;
            color: var(--hd-white);
        }}

        /* TL;DR Box */
        .tldr {{
            background: var(--hd-black);
            color: var(--hd-white);
            padding: 24px;
            margin: 24px 0;
        }}

        .tldr h3 {{
            color: var(--hd-orange);
            margin-top: 0;
            margin-bottom: 16px;
        }}

        .tldr p {{
            color: var(--hd-white);
            margin-bottom: 8px;
        }}

        .tldr strong {{
            color: var(--hd-orange);
        }}

        /* Quote Box */
        .quote {{
            background: var(--hd-gray-light);
            border-left: 4px solid var(--hd-orange);
            padding: 20px 24px;
            margin: 24px 0;
            font-style: italic;
            color: var(--hd-gray-dark);
        }}

        .quote-author {{
            font-style: normal;
            font-weight: 700;
            color: var(--hd-black);
            margin-top: 12px;
            font-size: 0.9em;
        }}

        /* Highlight Box */
        .highlight-box {{
            font-size: 1.15em;
            text-align: center;
            padding: 24px;
            background: var(--hd-gray-light);
            border-left: 4px solid var(--hd-orange);
            margin: 24px 0;
        }}

        /* Metrics Display */
        .metrics {{
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            margin: 24px 0;
        }}

        .metric {{
            background: var(--hd-white);
            padding: 24px 32px;
            text-align: center;
            border: 2px solid var(--hd-gray-medium);
            min-width: 140px;
            flex: 1;
        }}

        .metric-value {{
            font-size: 2.4em;
            font-weight: 700;
            color: var(--hd-orange);
        }}

        .metric-label {{
            font-size: 0.8em;
            color: var(--hd-gray-dark);
            text-transform: uppercase;
            letter-spacing: 0.02em;
            margin-top: 4px;
        }}

        /* Card Grid */
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 24px 0;
        }}

        .card {{
            background: var(--hd-white);
            border-left: 4px solid var(--hd-orange);
            padding: 20px 24px;
            border-top: 1px solid var(--hd-gray-medium);
            border-right: 1px solid var(--hd-gray-medium);
            border-bottom: 1px solid var(--hd-gray-medium);
        }}

        .card h4 {{
            color: var(--hd-black);
            text-transform: uppercase;
            font-size: 0.9em;
            letter-spacing: 0.02em;
            margin-top: 0;
        }}

        .card p {{
            margin-bottom: 0;
        }}

        .card.problem {{
            border-left-color: var(--hd-black);
            background: var(--hd-gray-light);
        }}

        .card.solution {{
            border-left-color: var(--hd-orange);
        }}

        /* Flow Diagram */
        .flow-diagram {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
            padding: 24px;
            background: var(--hd-gray-light);
            margin: 24px 0;
        }}

        .flow-box {{
            background: var(--hd-white);
            border: 2px solid var(--hd-gray-medium);
            padding: 12px 16px;
            text-align: center;
            min-width: 120px;
            font-size: 0.9em;
            color: var(--hd-black);
        }}

        .flow-arrow {{
            font-size: 1.5em;
            color: var(--hd-orange);
            font-weight: 700;
        }}

        .flow-result {{
            background: var(--hd-black);
            color: var(--hd-white);
            border-color: var(--hd-black);
        }}

        /* Timeline */
        .timeline {{
            position: relative;
            padding-left: 32px;
            margin: 24px 0;
        }}

        .timeline::before {{
            content: "";
            position: absolute;
            left: 10px;
            top: 0;
            bottom: 0;
            width: 3px;
            background: var(--hd-orange);
        }}

        .timeline-item {{
            position: relative;
            padding: 16px 0;
        }}

        .timeline-item::before {{
            content: "";
            position: absolute;
            left: -26px;
            top: 22px;
            width: 14px;
            height: 14px;
            background: var(--hd-orange);
        }}

        .timeline-item strong {{
            display: block;
            text-transform: uppercase;
            font-size: 0.9em;
            letter-spacing: 0.02em;
            margin-bottom: 4px;
            color: var(--hd-black);
        }}

        .timeline-item p {{
            margin: 0;
        }}

        /* Badges */
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            font-size: 0.8em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.02em;
        }}

        .badge-critical {{
            background: var(--hd-orange);
            color: var(--hd-white);
        }}

        .badge-high {{
            background: var(--hd-black);
            color: var(--hd-white);
        }}

        .badge-medium {{
            background: var(--hd-gray-light);
            color: var(--hd-black);
            border: 1px solid var(--hd-gray-dark);
        }}

        .badge-low {{
            background: var(--hd-gray-light);
            color: var(--hd-gray-dark);
            border: 1px solid var(--hd-gray-medium);
        }}

        /* Checklist */
        .checklist {{
            list-style: none;
            padding: 0;
        }}

        .checklist li {{
            padding: 12px 0;
            border-bottom: 1px solid var(--hd-gray-medium);
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }}

        .checklist li::before {{
            content: "";
            display: block;
            width: 16px;
            height: 16px;
            border: 2px solid var(--hd-orange);
            flex-shrink: 0;
            margin-top: 4px;
        }}

        /* Constraints/Pills */
        .constraints {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin: 20px 0;
        }}

        .constraint {{
            background: var(--hd-black);
            color: var(--hd-white);
            padding: 10px 20px;
            font-weight: 700;
            font-size: 0.85em;
            text-transform: uppercase;
            letter-spacing: 0.02em;
        }}

        /* Collapsible Sections */
        .section {{
            margin: 24px 0;
            border: 1px solid var(--hd-gray-medium);
        }}

        .section-header {{
            background: var(--hd-black);
            color: var(--hd-white);
            padding: 16px 24px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
        }}

        .section-header:hover {{
            background: #1a1a1a;
        }}

        .section-header h2 {{
            margin: 0;
            color: var(--hd-white);
            font-size: 1em;
            border: none;
            padding: 0;
        }}

        .section-header .toggle {{
            font-size: 1.5em;
            font-weight: 700;
            transition: transform 0.3s;
        }}

        .section-header.active .toggle {{
            transform: rotate(45deg);
        }}

        .section-content {{
            padding: 24px;
            display: none;
            background: var(--hd-white);
        }}

        .section-content.active {{
            display: block;
        }}

        /* Footer */
        .footer {{
            margin-top: 48px;
            padding-top: 24px;
            border-top: 2px solid var(--hd-gray-medium);
            text-align: center;
            color: var(--hd-gray-dark);
            font-size: 0.85em;
        }}

        /* Print styles */
        @media print {{
            body {{
                padding: 0;
            }}
            .nav, .section-header .toggle {{
                display: none;
            }}
            .section-content {{
                display: block !important;
            }}
            .hero {{
                margin: 0 0 24px 0;
            }}
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            body {{
                padding: 16px;
            }}

            .hero {{
                padding: 32px 16px;
                margin: -16px -16px 24px -16px;
            }}

            .flow-diagram {{
                flex-direction: column;
            }}

            .flow-arrow {{
                transform: rotate(90deg);
            }}

            .metrics {{
                flex-direction: column;
            }}

            .metric {{
                min-width: 100%;
            }}
        }}
    </style>
</head>
<body>

<div class="hero">
    <h1>{title}</h1>
    <p class="hero-subtitle">{subtitle}</p>
    <p class="hero-date">Generated: {date}</p>
</div>

{nav}

<main>
{content}
</main>

<div class="footer">
    Home Depot Case Study | UGA Terry College Case Competition 2026<br>
    <small>Generated from <code>{source_file}</code></small>
</div>

<script>
    function toggleSection(header) {{
        header.classList.toggle('active');
        const content = header.nextElementSibling;
        content.classList.toggle('active');
    }}

    // Open all sections by default
    document.addEventListener('DOMContentLoaded', function() {{
        document.querySelectorAll('.section-header').forEach(function(header) {{
            header.classList.add('active');
            header.nextElementSibling.classList.add('active');
        }});
    }});
</script>

</body>
</html>
'''


# ============================================================================
# CUSTOM BLOCK PROCESSORS
# ============================================================================

def process_metrics_block(content):
    """
    Convert:
    :::metrics
    65% | Magic Apron Delivery Rate
    $1.5M | Annual Investment
    :::
    """
    lines = content.strip().split('\n')
    metrics_html = ['<div class="metrics">']
    for line in lines:
        if '|' in line:
            parts = line.split('|', 1)
            value = parts[0].strip()
            label = parts[1].strip() if len(parts) > 1 else ''
            metrics_html.append(f'''
            <div class="metric">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>''')
    metrics_html.append('</div>')
    return '\n'.join(metrics_html)


def process_quote_block(content, author=None):
    """
    Convert:
    :::quote author="Sam, EVP Digital"
    Quote text here
    :::
    """
    author_html = f'<div class="quote-author">— {author}</div>' if author else ''
    return f'''<div class="quote">
    {content}
    {author_html}
</div>'''


def process_tldr_block(content):
    """
    Convert:
    :::tldr
    Quick summary
    :::
    """
    return f'''<div class="tldr">
    <h3>TL;DR</h3>
    {content}
</div>'''


def process_highlight_block(content):
    """
    Convert:
    :::highlight
    Important text
    :::
    """
    return f'<div class="highlight-box"><strong>{content}</strong></div>'


def process_flow_block(content):
    """
    Convert:
    :::flow
    Step 1 -> Step 2 -> Step 3 -> [Result]
    :::
    """
    line = content.strip()
    steps = [s.strip() for s in line.split('->')]
    flow_html = ['<div class="flow-diagram">']
    for i, step in enumerate(steps):
        # Check if it's a result (wrapped in brackets)
        is_result = step.startswith('[') and step.endswith(']')
        if is_result:
            step = step[1:-1]
            flow_html.append(f'<div class="flow-box flow-result">{step}</div>')
        else:
            flow_html.append(f'<div class="flow-box">{step}</div>')

        if i < len(steps) - 1:
            flow_html.append('<span class="flow-arrow">→</span>')

    flow_html.append('</div>')
    return '\n'.join(flow_html)


def process_card_grid_block(content):
    """
    Convert:
    :::card-grid
    ### Card Title {.problem}
    Card content
    ---
    ### Another Card {.solution}
    Content
    :::
    """
    cards = content.split('---')
    cards_html = ['<div class="card-grid">']

    for card in cards:
        card = card.strip()
        if not card:
            continue

        # Extract card class if present
        card_class = 'card'
        if '{.problem}' in card:
            card_class = 'card problem'
            card = card.replace('{.problem}', '')
        elif '{.solution}' in card:
            card_class = 'card solution'
            card = card.replace('{.solution}', '')

        # Parse title and content
        lines = card.strip().split('\n')
        title = ''
        body_lines = []

        for line in lines:
            if line.startswith('###'):
                title = line.replace('###', '').strip()
            elif line.startswith('####'):
                title = line.replace('####', '').strip()
            else:
                body_lines.append(line)

        body = '\n'.join(body_lines).strip()

        cards_html.append(f'''<div class="{card_class}">
    <h4>{title}</h4>
    <p>{body}</p>
</div>''')

    cards_html.append('</div>')
    return '\n'.join(cards_html)


def process_timeline_block(content):
    """
    Convert:
    :::timeline
    **Phase 1 (Weeks 1-4)**: Description here
    **Phase 2 (Weeks 5-8)**: More description
    :::
    """
    lines = content.strip().split('\n')
    timeline_html = ['<div class="timeline">']

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Parse **Title**: Description format
        match = re.match(r'\*\*(.+?)\*\*:?\s*(.*)', line)
        if match:
            title = match.group(1)
            desc = match.group(2)
            timeline_html.append(f'''<div class="timeline-item">
    <strong>{title}</strong>
    <p>{desc}</p>
</div>''')
        else:
            timeline_html.append(f'''<div class="timeline-item">
    <p>{line}</p>
</div>''')

    timeline_html.append('</div>')
    return '\n'.join(timeline_html)


def process_constraints_block(content):
    """
    Convert:
    :::constraints
    No Centralization
    No Bureaucracy
    Preserve Speed
    :::
    """
    items = [item.strip() for item in content.strip().split('\n') if item.strip()]
    constraints_html = ['<div class="constraints">']
    for item in items:
        constraints_html.append(f'<span class="constraint">{item}</span>')
    constraints_html.append('</div>')
    return '\n'.join(constraints_html)


# ============================================================================
# MAIN PROCESSOR
# ============================================================================

def process_custom_blocks(text):
    """Process all custom ::: blocks in the markdown"""

    # Process :::metrics blocks
    text = re.sub(
        r':::metrics\n(.*?)\n:::',
        lambda m: process_metrics_block(m.group(1)),
        text,
        flags=re.DOTALL
    )

    # Process :::quote blocks with optional author
    def quote_replacer(m):
        attrs = m.group(1) or ''
        content = m.group(2)
        author_match = re.search(r'author="([^"]+)"', attrs)
        author = author_match.group(1) if author_match else None
        return process_quote_block(content.strip(), author)

    text = re.sub(
        r':::quote\s*([^\n]*)\n(.*?)\n:::',
        quote_replacer,
        text,
        flags=re.DOTALL
    )

    # Process :::tldr blocks
    text = re.sub(
        r':::tldr\n(.*?)\n:::',
        lambda m: process_tldr_block(m.group(1).strip()),
        text,
        flags=re.DOTALL
    )

    # Process :::highlight blocks
    text = re.sub(
        r':::highlight\n(.*?)\n:::',
        lambda m: process_highlight_block(m.group(1).strip()),
        text,
        flags=re.DOTALL
    )

    # Process :::flow blocks
    text = re.sub(
        r':::flow\n(.*?)\n:::',
        lambda m: process_flow_block(m.group(1)),
        text,
        flags=re.DOTALL
    )

    # Process :::card-grid blocks
    text = re.sub(
        r':::card-grid\n(.*?)\n:::',
        lambda m: process_card_grid_block(m.group(1)),
        text,
        flags=re.DOTALL
    )

    # Process :::timeline blocks
    text = re.sub(
        r':::timeline\n(.*?)\n:::',
        lambda m: process_timeline_block(m.group(1)),
        text,
        flags=re.DOTALL
    )

    # Process :::constraints blocks
    text = re.sub(
        r':::constraints\n(.*?)\n:::',
        lambda m: process_constraints_block(m.group(1)),
        text,
        flags=re.DOTALL
    )

    return text


def extract_title_and_subtitle(text):
    """Extract title from first H1 and subtitle from first paragraph"""
    title = "Document"
    subtitle = "Home Depot MBA Case Study"

    # Look for first H1
    h1_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()

    # Look for subtitle in format: > Subtitle text
    subtitle_match = re.search(r'^>\s*\*?\*?(.+?)\*?\*?\s*$', text, re.MULTILINE)
    if subtitle_match:
        subtitle = subtitle_match.group(1).strip()

    return title, subtitle


def generate_nav(text):
    """Generate navigation from H2 headings"""
    headings = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
    if len(headings) < 2:
        return ''

    nav_links = []
    for heading in headings[:10]:  # Limit to 10 nav items
        slug = re.sub(r'[^a-z0-9]+', '-', heading.lower()).strip('-')
        nav_links.append(f'<a href="#{slug}">{heading}</a>')

    return f'''<nav class="nav">
    <div class="nav-links">
        {chr(10).join(nav_links)}
    </div>
</nav>'''


def add_heading_ids(html):
    """Add IDs to h2 elements for navigation"""
    def add_id(match):
        tag = match.group(1)
        content = match.group(2)
        slug = re.sub(r'[^a-z0-9]+', '-', content.lower()).strip('-')
        return f'<{tag} id="{slug}">{content}</{tag}>'

    return re.sub(r'<(h2)>(.+?)</\1>', add_id, html)


def convert_markdown_to_html(md_text):
    """Convert markdown to HTML"""
    if HAS_MARKDOWN:
        md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
        return md.convert(md_text)
    else:
        # Basic fallback conversion
        html = md_text

        # Headers
        html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

        # Bold and italic
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

        # Code
        html = re.sub(r'`(.+?)`', r'<code>\1</code>', html)

        # Lists
        html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

        # Paragraphs (simple)
        paragraphs = html.split('\n\n')
        processed = []
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith('<'):
                p = f'<p>{p}</p>'
            processed.append(p)
        html = '\n\n'.join(processed)

        return html


def build_html(md_path, output_path=None, use_subfolder=True):
    """Build HTML from a markdown file

    Args:
        md_path: Path to markdown file
        output_path: Optional explicit output path
        use_subfolder: If True, output to html/ subfolder (default)
    """
    md_path = Path(md_path)

    if not md_path.exists():
        print(f"Error: File not found: {md_path}")
        return False

    # Determine output path
    if output_path is None:
        if use_subfolder:
            # Place HTML in reading/ subfolder within same directory
            reading_dir = md_path.parent / 'reading'
            reading_dir.mkdir(exist_ok=True)
            output_path = reading_dir / md_path.with_suffix('.html').name
        else:
            # Place HTML next to markdown file
            output_path = md_path.with_suffix('.html')
    else:
        output_path = Path(output_path)

    print(f"Building: {md_path} -> {output_path}")

    # Read markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Extract metadata
    title, subtitle = extract_title_and_subtitle(md_text)

    # Generate navigation
    nav = generate_nav(md_text)

    # Process custom blocks first
    md_text = process_custom_blocks(md_text)

    # Convert markdown to HTML
    content_html = convert_markdown_to_html(md_text)

    # Add heading IDs
    content_html = add_heading_ids(content_html)

    # Build final HTML
    html = HTML_TEMPLATE.format(
        title=title,
        subtitle=subtitle,
        date=datetime.now().strftime('%B %d, %Y'),
        nav=nav,
        content=content_html,
        source_file=md_path.name
    )

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  ✓ Generated: {output_path}")
    return True


def find_markdown_files(root_dir):
    """Find all markdown files to build"""
    root = Path(root_dir)

    # Skip these directories
    skip_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'utils'}

    md_files = []
    for md_file in root.rglob('*.md'):
        # Skip if in excluded directory
        if any(skip in md_file.parts for skip in skip_dirs):
            continue
        # Skip README and other non-content files
        if md_file.name.lower() in ['readme.md', 'changelog.md', 'license.md']:
            continue
        md_files.append(md_file)

    return sorted(md_files)


def main():
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    args = sys.argv[1:]

    if not args:
        # Build files from config
        try:
            from build_config import FILES_TO_CONVERT
            print("Building configured files...\n")
            md_files = [project_root / f for f in FILES_TO_CONVERT]
        except ImportError:
            print("No build_config.py found, building all markdown files...\n")
            md_files = find_markdown_files(project_root)

        if not md_files:
            print("No markdown files to build.")
            return

        success_count = 0
        for md_file in md_files:
            if build_html(md_file):
                success_count += 1

        print(f"\n✓ Built {success_count}/{len(md_files)} files")
        print("HTMLs are in reading/ subfolders within each directory.")

    elif args[0] == '--all':
        # Build ALL markdown files (ignore config)
        print("Building ALL markdown files...\n")
        md_files = find_markdown_files(project_root)

        success_count = 0
        for md_file in md_files:
            if build_html(md_file):
                success_count += 1

        print(f"\n✓ Built {success_count}/{len(md_files)} files")

    elif args[0] == '--watch':
        print("Watch mode requires 'watchdog' package.")
        print("Install with: uv add watchdog")
        print("\nFor now, run manually after editing markdown files.")

    elif args[0] == '--clean':
        # Remove all generated HTML files
        print("Cleaning generated HTML files...\n")
        for reading_dir in project_root.rglob('reading'):
            if reading_dir.is_dir() and reading_dir.parent != project_root:
                for html_file in reading_dir.glob('*.html'):
                    print(f"  Removing: {html_file}")
                    html_file.unlink()
        # Also clean any stray .html files next to .md files
        for html_file in project_root.rglob('*.html'):
            if 'utils' not in html_file.parts and html_file.parent.name != 'reading':
                md_file = html_file.with_suffix('.md')
                if md_file.exists():
                    print(f"  Removing: {html_file}")
                    html_file.unlink()
        print("\n✓ Clean complete")

    else:
        # Build specific file(s)
        for arg in args:
            path = Path(arg)
            if not path.is_absolute():
                path = project_root / path
            build_html(path)


if __name__ == '__main__':
    main()
