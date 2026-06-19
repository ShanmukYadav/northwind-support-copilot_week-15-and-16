import os
import time
import requests

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin

BASE = "https://linear.app"
START = "https://linear.app/docs"

OUTPUT_DIR = "corpus"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_all_doc_links():
    print("Discovering docs...")

    html = requests.get(START, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")

    links = set()

    for a in soup.find_all("a", href=True):

        href = a["href"]

        if href.startswith("/docs/"):
            links.add(urljoin(BASE, href))

    return sorted(links)


def clean(text):

    lines = []

    for l in text.splitlines():

        l = l.strip()

        if len(l) < 2:
            continue

        lines.append(l)

    return "\n".join(lines)


def scrape(url):

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    main = soup.find("main")

    if main is None:
        main = soup.body

    title = soup.title.text.split("|")[0].strip()

    markdown = md(str(main))

    markdown = clean(markdown)

    slug = url.rstrip("/").split("/")[-1]

    return slug, title, markdown


def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    links = get_all_doc_links()

    print(f"Found {len(links)} docs\n")

    ok = 0

    for url in links:

        print(url)

        result = scrape(url)

        if result is None:
            continue

        slug, title, text = result

        with open(
            os.path.join(OUTPUT_DIR, slug + ".md"),
            "w",
            encoding="utf8"
        ) as f:

            f.write(f"# {title}\n\n")
            f.write(text)

        ok += 1

        time.sleep(0.7)

    print(f"\nSaved {ok} documents")


if __name__ == "__main__":
    main()