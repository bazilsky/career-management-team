#!/usr/bin/env python3
"""Render a filed path to a local PDF.

Usage:
  python3 scripts/render_pdf.py grant
  python3 scripts/render_pdf.py paper --week 2026-09-28

Reads runs/<week>/<path>.md, checks that every http(s) URL answers,
prints with the local Google Chrome, and writes runs/<week>/<path>.pdf.
The temporary HTML is deleted. Nothing is published.
"""

import argparse
import html
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
PATHS = ("grant", "paper", "idea")
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
WEEK = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL = re.compile(r"https?://[^\s)>\]]+")

STYLE = """
@page { size: A4; margin: 18mm 16mm 20mm; }
* { box-sizing: border-box; }
html { font-size: 11pt; }
body {
  margin: 0;
  color: #1c1915;
  font-family: "Source Sans 3", "Segoe UI", sans-serif;
  line-height: 1.45;
}
h1, h2, h3 { font-family: Georgia, "Iowan Old Style", serif; font-weight: 500; line-height: 1.15; }
h1 { font-size: 22pt; margin: 0 0 0.4rem; }
.kicker { margin: 0 0 0.2rem; color: #8a6a2f; font-size: 9pt; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; }
h2 { font-size: 15pt; margin: 1.4rem 0 0.5rem; break-after: avoid; }
h3 { font-size: 12.5pt; margin: 0 0 0.35rem; break-after: avoid; }
p { margin: 0.35rem 0; }
a { color: #9a3b24; word-break: break-all; }
ul { margin: 0.2rem 0 0.4rem; padding-left: 1.1rem; }
li { margin: 0.15rem 0; }
article {
  break-inside: avoid;
  margin: 0 0 0.8rem;
  padding: 0.55rem 0 0.7rem;
  border-top: 1px solid #e2d8c8;
}
.signoff { margin-top: 1.4rem; color: #5c564c; }
"""


def latest_week(path_name):
    weeks = sorted(
        p.parent.name
        for p in RUNS.glob(f"*/{path_name}.md")
        if WEEK.match(p.parent.name)
    )
    if not weeks:
        sys.exit(f"No filed {path_name}.md under runs/. File the week, then render.")
    return weeks[-1]


def inline(text):
    escaped = html.escape(text.strip())
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(https?://[^\s&]+)", r'<a href="\1">\1</a>', escaped)
    return escaped


def markdown_to_body(source):
    lines = source.replace("\r\n", "\n").split("\n")
    parts = []
    paragraph = []
    items = []
    in_article = False
    title_done = False

    def flush_paragraph():
        if paragraph:
            parts.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_items():
        if items:
            lis = "".join(f"<li>{inline(item)}</li>" for item in items)
            parts.append(f"<ul>{lis}</ul>")
            items.clear()

    def close_article():
        nonlocal in_article
        flush_paragraph()
        flush_items()
        if in_article:
            parts.append("</article>")
            in_article = False

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_paragraph()
            flush_items()
            continue
        if line.startswith("### "):
            close_article()
            in_article = True
            parts.append(f"<article><h3>{inline(line[4:])}</h3>")
            continue
        if line.startswith("## "):
            close_article()
            parts.append(f"<h2>{inline(line[3:])}</h2>")
            continue
        if line.startswith("# "):
            close_article()
            if not title_done:
                parts.append(f"<h1>{inline(line[2:])}</h1>")
                title_done = True
            else:
                parts.append(f'<p class="kicker">{inline(line[2:])}</p>')
            continue
        if line.startswith("- "):
            flush_paragraph()
            items.append(line[2:])
            continue
        flush_items()
        paragraph.append(line)
    close_article()
    return "\n".join(parts).replace(
        "<p>Mrs. Vanguard</p>", '<p class="signoff">Mrs. Vanguard</p>'
    )


def urls_in(source):
    found = []
    for match in URL.findall(source):
        cleaned = match.rstrip(".,;")
        if cleaned not in found:
            found.append(cleaned)
    return found


def resolves(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "career-management-pdf/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return response.status < 400, response.status
    except urllib.error.HTTPError as error:
        return error.code < 400, error.code
    except Exception as error:
        return False, error.__class__.__name__


def write_html(title, body, destination):
    document = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>{STYLE}</style>
</head>
<body>
{body}
</body>
</html>
"""
    destination.write_text(document, encoding="utf-8")


def print_pdf(html_path, pdf_path):
    if not CHROME.is_file():
        sys.exit(f"Google Chrome not found at {CHROME}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path.as_uri(),
    ]
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode != 0 or not pdf_path.is_file() or pdf_path.stat().st_size < 1000:
        sys.stderr.write(completed.stderr)
        sys.exit(f"Chrome did not write {pdf_path}")


def main():
    parser = argparse.ArgumentParser(description="Render a filed path to PDF.")
    parser.add_argument("path", choices=PATHS)
    parser.add_argument("--week", help="Run date, YYYY-MM-DD. Defaults to the latest filed week.")
    args = parser.parse_args()

    week = args.week or latest_week(args.path)
    if not WEEK.match(week):
        sys.exit("--week must be YYYY-MM-DD")
    source_path = RUNS / week / f"{args.path}.md"
    if not source_path.is_file():
        sys.exit(f"Missing {source_path}. File that markdown, then render.")

    source = source_path.read_text(encoding="utf-8")
    failed = []
    for url in urls_in(source):
        ok, detail = resolves(url)
        if not ok:
            failed.append(f"{url} ({detail})")
    if failed:
        sys.exit("URL check failed:\n" + "\n".join(failed))

    title = f"{args.path} path — {week}"
    with tempfile.TemporaryDirectory(prefix="pdf-") as temporary:
        html_path = Path(temporary) / f"{args.path}.html"
        write_html(title, markdown_to_body(source), html_path)
        pdf_path = source_path.with_suffix(".pdf")
        print_pdf(html_path, pdf_path)
    print(pdf_path)


if __name__ == "__main__":
    main()
