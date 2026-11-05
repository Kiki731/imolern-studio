#!/usr/bin/env python3
"""Assemble mock-up pages from src/ with the shared head, nav and footer.

Copy this file into design/mockups/ as _build.py, then run: python3 _build.py
Each src/<page>.html starts with <!--TITLE: Page title--> and may contain
<!--HEAD-->, <!--NAV--> and <!--FOOT-->. src/_head.html may use {TITLE}.
Built pages are written next to this file; never edit them by hand.
"""
import pathlib
import re
import sys

here = pathlib.Path(__file__).resolve().parent
src_dir = here / "src"


def part(name: str) -> str:
    for p in (src_dir / name, here / name):
        if p.exists():
            return p.read_text()
    return ""


head, nav, foot = part("_head.html"), part("_nav.html"), part("_foot.html")
pages = [p for p in sorted(src_dir.glob("*.html")) if not p.name.startswith("_")]
if not pages:
    sys.exit(f"No pages in {src_dir}")

for src in pages:
    s = src.read_text()
    m = re.search(r"<!--TITLE:(.*?)-->", s)
    title = m.group(1).strip() if m else src.stem
    s = (s.replace("<!--HEAD-->", head.replace("{TITLE}", title))
          .replace("<!--NAV-->", nav)
          .replace("<!--FOOT-->", foot))
    (here / src.name).write_text(s)
    print("built", src.name)
