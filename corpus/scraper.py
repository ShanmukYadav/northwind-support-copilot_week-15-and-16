# scraper.py
# Run from project root: python scraper.py
# Requirements: pip install requests beautifulsoup4 markdownify

import os
import time
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ── CONFIG ──────────────────────────────────────────────────────────────────
OUTPUT_DIR = "corpus"
HEADERS = {"User-Agent": "Mozilla/5.0 (research scraper; northwind-support-copilot project)"}
DELAY = 1.2  # seconds between requests — be polite

# Curated list: 20 Linear docs pages + 8 changelog entries = 28 docs total
# Covers: core concepts, projects, cycles, issues, integrations → good variety
# for easy / multi-hop / adversarial questions later

DOCS_PAGES = [
    ("conceptual-model",       "https://linear.app/docs/conceptual-model"),
    ("what-is-linear",         "https://linear.app/docs/what-is-linear"),
    ("start-guide",            "https://linear.app/docs/start-guide"),
    ("issues",                 "https://linear.app/docs/issues"),
    ("projects",               "https://linear.app/docs/projects"),
    ("project-overview",       "https://linear.app/docs/project-overview"),
    ("project-documents",      "https://linear.app/docs/project-documents"),
    ("cycles",                 "https://linear.app/docs/cycles"),
    ("teams",                  "https://linear.app/docs/teams"),
    ("workspaces",             "https://linear.app/docs/workspace"),
    ("members",                "https://linear.app/docs/members"),
    ("views",                  "https://linear.app/docs/views"),
    ("filters",                "https://linear.app/docs/filters"),
    ("roadmaps",               "https://linear.app/docs/roadmaps"),
    ("triage",                 "https://linear.app/docs/triage"),
    ("labels",                 "https://linear.app/docs/labels"),
    ("priorities",             "https://linear.app/docs/priorities"),
    ("notifications",          "https://linear.app/docs/notifications"),
    ("keyboard-shortcuts",     "https://linear.app/docs/keyboard-shortcuts"),
    ("api-and-integrations",   "https://linear.app/docs/api-and-integrations"),
]

# Changelog entries — gives you recency / multi-hop / time-based questions
CHANGELOG_PAGES = [
    ("changelog-2024-q4",      "https://linear.app/changelog/2024-q4"),
    ("changelog-2024-q3",      "https://linear.app/changelog/2024-q3"),
    ("changelog-2024-q2",      "https://linear.app/changelog/2024-q2"),
    ("changelog-2024-q1",      "https://linear.app/changelog/2024-q1"),
    ("changelog-2023-q4",      "https://linear.app/changelog/2023-q4"),
    ("changelog-2023-q3",      "https://linear.app/changelog/2023-q3"),
    ("changelog-2023-q2",      "https://linear.app/changelog/2023-q2"),
    ("changelog-2023-q1",      "https://linear.app/changelog/2023-q1"),
]

ALL_PAGES = DOCS_PAGES + CHANGELOG_PAGES

# ── HELPERS ──────────────────────────────────────────────────────────────────

def clean_markdown(text: str) -> str:
    """Strip nav/footer noise, collapse blank lines."""
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove lines that are just navigation-style short phrases
    lines = [l for l in text.splitlines() if len(l.strip()) > 1 or l.strip() == ""]
    return "\n".join(lines).strip()


def extract_main_content(soup: BeautifulSoup) -> str:
    """
    Pull the main article body — skip nav, sidebar, footer.
    Linear's docs site uses <main> or <article> tags; fall back to <body>.
    """
    # Try in order of specificity
    for selector in ["main", "article", "[role='main']", "div.docs-content", "body"]:
        tag = soup.select_one(selector)
        if tag:
            # Remove nav, header, footer, aside, script, style noise
            for noise in tag.select("nav, header, footer, aside, script, style, [aria-hidden='true']"):
                noise.decompose()
            return md(str(tag), heading_style="ATX", bullets="-")
    return ""


def scrape_page(slug: str, url: str) -> bool:
    """Fetch one page, convert to markdown, save to corpus/."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code == 404:
            print(f"  [SKIP] 404 → {url}")
            return False
        resp.raise_for_status()
    except Exception as e:
        print(f"  [ERROR] {url} → {e}")
        return False

    soup = BeautifulSoup(resp.text, "html.parser")

    # Page title for the top of the markdown file
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else slug

    content = extract_main_content(soup)
    content = clean_markdown(content)

    if len(content) < 200:
        print(f"  [WARN] Very short content ({len(content)} chars) for {url} — may be gated/JS-rendered")

    # Relabel as "Northwind" in the header (per PRD framing)
    header = f"""# {title}

> **Source:** Northwind Support Copilot corpus  
> **Original URL:** {url}  
> **Document ID:** {slug}

---

"""
    filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + content)

    print(f"  [OK] {slug}.md ({len(content)} chars)")
    return True


# ── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Scraping {len(ALL_PAGES)} pages into ./{OUTPUT_DIR}/\n")

    ok, skip = 0, 0
    for slug, url in ALL_PAGES:
        print(f"→ {slug}")
        success = scrape_page(slug, url)
        if success:
            ok += 1
        else:
            skip += 1
        time.sleep(DELAY)

    print(f"\nDone. {ok} saved, {skip} skipped/failed.")
    print(f"Corpus lives in ./{OUTPUT_DIR}/")

    # Sanity check: list what we got
    files = sorted(os.listdir(OUTPUT_DIR))
    print(f"\nFiles in corpus/ ({len(files)} total):")
    for f in files:
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}  ({size:,} bytes)")


if __name__ == "__main__":
    main()