#!/usr/bin/env python3
"""Check which skills Imolern Studio needs are installed, and print install commands for the rest.

Usage: python3 check_skills.py [--agent <name>] [--json]

--agent   the agent running this (claude-code, codex, cursor, gemini-cli, github-copilot,
          windsurf, opencode, amp, cline, goose, ...). Guessed from the environment if left out.
          Skills only count as installed if this agent can see them.
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
config = pathlib.Path(os.environ.get("XDG_CONFIG_HOME") or home / ".config")
claude_home = pathlib.Path(os.environ.get("CLAUDE_CONFIG_DIR") or home / ".claude")
codex_home = pathlib.Path(os.environ.get("CODEX_HOME") or home / ".codex")

# Where each agent looks for skills: global folders, then project folders.
# Matches the `skills` installer (npx skills). ".agents/skills" is the shared standard folder.
AGENTS = {
    "claude-code":    [claude_home / "skills", cwd / ".claude/skills"],
    "codex":          [home / ".agents/skills", codex_home / "skills", cwd / ".agents/skills"],
    "cursor":         [home / ".cursor/skills", home / ".agents/skills", cwd / ".agents/skills", cwd / ".cursor/skills"],
    "gemini-cli":     [home / ".gemini/skills", home / ".agents/skills", cwd / ".agents/skills", cwd / ".gemini/skills"],
    "github-copilot": [home / ".copilot/skills", home / ".agents/skills", cwd / ".agents/skills", cwd / ".github/skills"],
    "windsurf":       [home / ".codeium/windsurf/skills", cwd / ".windsurf/skills"],
    "opencode":       [config / "opencode/skills", home / ".agents/skills", cwd / ".agents/skills", cwd / ".opencode/skills"],
    "amp":            [config / "agents/skills", home / ".agents/skills", cwd / ".agents/skills"],
    "cline":          [home / ".agents/skills", cwd / ".agents/skills"],
    "goose":          [config / "goose/skills", cwd / ".goose/skills"],
}
# Used when the agent isn't known: every folder above, plus the shared standard ones.
ANY = [config / "agents/skills", home / ".agents/skills", cwd / ".agents/skills"]


def detect_agent() -> str | None:
    env = os.environ
    if env.get("CLAUDECODE") or env.get("CLAUDE_CODE_ENTRYPOINT"):
        return "claude-code"
    if any(k.startswith("CODEX_") for k in env if k != "CODEX_HOME"):
        return "codex"
    if env.get("CURSOR_TRACE_ID") or env.get("CURSOR_AGENT"):
        return "cursor"
    if env.get("GEMINI_CLI"):
        return "gemini-cli"
    return None


def skill_name(md: pathlib.Path) -> str | None:
    try:
        head = md.read_text(errors="ignore")[:2000]
    except OSError:
        return None
    m = re.search(r"^name:\s*['\"]?([^'\"\n]+)", head, re.M)
    return m.group(1).strip().split(":")[-1] if m else None  # "ckm:design" -> "design"


def scan(folders) -> dict[str, str]:
    found = {}
    for root in folders:
        if not root.is_dir():
            continue
        for md in root.glob("*/SKILL.md"):
            for n in {md.parent.name, skill_name(md)}:
                if n:
                    found.setdefault(n, str(md.parent))
    return found


def scan_claude_plugins() -> dict[str, str]:
    found, root = {}, claude_home / "plugins"
    if not root.is_dir():
        return found
    base = str(root).count(os.sep)
    for dirpath, dirnames, filenames in os.walk(root):
        if dirpath.count(os.sep) - base > 7:
            dirnames[:] = []
            continue
        if "SKILL.md" in filenames:
            md = pathlib.Path(dirpath) / "SKILL.md"
            for n in {md.parent.name, skill_name(md)}:
                if n:
                    found.setdefault(n, str(md.parent))
    return found


def main():
    args = sys.argv[1:]
    agent = args[args.index("--agent") + 1] if "--agent" in args and args.index("--agent") + 1 < len(args) else None
    detected = False
    if not agent:
        agent, detected = detect_agent(), True

    if agent in AGENTS:
        folders = AGENTS[agent]
    else:
        folders = ANY + [p for ps in AGENTS.values() for p in ps]
    have = scan(folders)
    if agent == "claude-code":
        for k, v in scan_claude_plugins().items():
            have.setdefault(k, v)

    report = {"agent": agent or "unknown", "agent_detected": detected and bool(agent),
              "folders": [str(p) for p in folders]}
    for group in ("required", "recommended"):
        report[group] = [{**s, "installed": s["skill"] in have, "path": have.get(s["skill"])}
                         for s in MANIFEST[group]]

    flag = f" -a {agent}" if agent else ""

    def commands(rows):
        by_repo = {}
        for r in rows:
            if not r["installed"]:
                by_repo.setdefault(r["repo"], []).append(r["skill"])
        return [f"npx skills add {repo} -g{flag} -s {' '.join(s)} -y" for repo, s in by_repo.items()]

    report["install_required"] = commands(report["required"])
    report["install_recommended"] = commands(report["recommended"])

    if "--json" in args:
        print(json.dumps(report, indent=2))
        return

    if agent:
        how = "detected" if detected else "given"
        print(f"Agent: {agent} ({how}). Checking the folders it reads.")
    else:
        print("Agent: unknown. Checking every common skills folder. Pass --agent <name> to be precise;")
        print("without it, the install commands let the skills installer ask or detect the agent.")
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
