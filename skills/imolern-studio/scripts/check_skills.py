#!/usr/bin/env python3
"""Check which skills Imolern Studio needs are installed, and print install commands for the rest.

Usage: python3 check_skills.py [--json]
Reads nothing but SKILL.md front matter in the usual skill folders. Installs nothing.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
MANIFEST = json.loads((HERE.parent / "skills.json").read_text())

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
ROOTS = [
    home / ".claude/skills",
    home / ".agents/skills",
    cwd / ".claude/skills",
    cwd / ".agents/skills",
]
PLUGIN_ROOT = home / ".claude/plugins"


def skill_name(md: pathlib.Path) -> str | None:
    try:
        head = md.read_text(errors="ignore")[:2000]
    except OSError:
        return None
    m = re.search(r"^name:\s*['\"]?([^'\"\n]+)", head, re.M)
    if not m:
        return None
    return m.group(1).strip().split(":")[-1]  # "ckm:design" -> "design"


def installed() -> dict[str, str]:
    found = {}
    for root in ROOTS:
        if not root.is_dir():
            continue
        for md in root.glob("*/SKILL.md"):
            for n in {md.parent.name, skill_name(md)}:
                if n:
                    found.setdefault(n, str(md.parent))
    if PLUGIN_ROOT.is_dir():
        for dirpath, dirnames, filenames in os.walk(PLUGIN_ROOT):
            if dirpath.count(os.sep) - str(PLUGIN_ROOT).count(os.sep) > 7:
                dirnames[:] = []
                continue
            if "SKILL.md" in filenames:
                md = pathlib.Path(dirpath) / "SKILL.md"
                for n in {md.parent.name, skill_name(md)}:
                    if n:
                        found.setdefault(n, str(md.parent))
    return found


def main():
    have = installed()
    report = {}
    for group in ("required", "recommended"):
        rows = []
        for s in MANIFEST[group]:
            rows.append({**s, "installed": s["skill"] in have, "path": have.get(s["skill"])})
        report[group] = rows

    def commands(rows):
        by_repo = {}
        for r in rows:
            if not r["installed"]:
                by_repo.setdefault(r["repo"], []).append(r["skill"])
        return [f"npx skills add {repo} -g -a claude-code -s {' '.join(skills)} -y" for repo, skills in by_repo.items()]

    report["install_required"] = commands(report["required"])
    report["install_recommended"] = commands(report["recommended"])

    if "--json" in sys.argv:
        print(json.dumps(report, indent=2))
        return

    for group in ("required", "recommended"):
        print(f"\n{group.capitalize()}:")
        for r in report[group]:
            mark = "installed" if r["installed"] else "MISSING  "
            print(f"  [{mark}] {r['skill']:<28} {r['why']}")
    for key, label in (("install_required", "required"), ("install_recommended", "recommended")):
        if report[key]:
            print(f"\nTo install the missing {label} skills:")
            for c in report[key]:
                print("  " + c)
    missing = sum(not r["installed"] for r in report["required"])
    print(f"\nRequired: {len(report['required']) - missing}/{len(report['required'])} installed.")


if __name__ == "__main__":
    main()
