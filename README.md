# Imolern Studio

A Claude Code skill for designing and building websites and web apps that look hand-made, not AI-generated: marketing sites, e-commerce, landing pages, dashboards, portals and admin tools.

It works like a design studio. It learns from the sites you love, agrees a direction with you, shows you a design system and mock-ups to approve, then builds them exactly, with real motion and proper checks.

## What it does

1. **Sets up** the design and motion skills it relies on: it asks before checking, and asks before installing anything missing.
2. **Takes your brief and stack**: site type, product, audience, pages, and the stack you want (with a suggested default).
3. **Connects integrations** for real assets: Brandfetch (logos), Unsplash (photos), Magnific (images).
4. **Studies your references** one by one (layout, type, colour, motion, interactions) and writes what to take and what to avoid from each, then drafts a design direction for your approval.
5. **Builds a style tile**: the design system on one HTML page, in light and dark, for you to audit.
6. **Makes HTML mock-ups** of each page for approval (skippable once you love the direction).
7. **Builds them exactly** into your stack, with GSAP motion, and proves the build matches the mock-ups.
8. **Checks everything**: Impeccable design review on every piece, accessibility, phone and desktop widths, reduced motion, console errors, production basics.
9. **Hands over** with progress notes, a list of what's still simulated, and what only you can supply.

It never invents prices, customers, logos or stats, never fakes a feature that isn't built, and never commits without asking.

## Install

Imolern Studio is a standard agent skill (`SKILL.md`), so it works in Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Windsurf, OpenCode and any other agent the [`skills`](https://www.npmjs.com/package/skills) installer supports. You need Node.js for `npx`.

Run this in a terminal and pick your agent when asked (or let it detect the one you're in):

```bash
npx skills add Kiki731/imolern-studio -g
```

Or name the agent directly:

| Agent | Command |
|---|---|
| Claude Code | `npx skills add Kiki731/imolern-studio -g -a claude-code` |
| Codex | `npx skills add Kiki731/imolern-studio -g -a codex` |
| Cursor | `npx skills add Kiki731/imolern-studio -g -a cursor` |
| Gemini CLI | `npx skills add Kiki731/imolern-studio -g -a gemini-cli` |
| GitHub Copilot | `npx skills add Kiki731/imolern-studio -g -a github-copilot` |
| Windsurf | `npx skills add Kiki731/imolern-studio -g -a windsurf` |
| Several at once | `npx skills add Kiki731/imolern-studio -g -a claude-code codex cursor` |

Leave out `-g` to install into the current project only.

**Without npx:** clone the repo and copy (or link) `skills/imolern-studio` into your agent's skills folder, for example `~/.claude/skills/` for Claude Code or `~/.agents/skills/` for Codex.

```bash
git clone https://github.com/Kiki731/imolern-studio.git
ln -s "$PWD/imolern-studio/skills/imolern-studio" ~/.agents/skills/imolern-studio
```

Then start your agent and say: **"Let's build a website with Imolern Studio."** On first run it checks the skills it depends on, in the folders *your* agent reads, and offers to install what's missing for that agent.

### What it needs from the agent

A shell, file editing, and ideally a browser the agent can drive (to study reference sites and check pages). Without a browser tool it asks you for screenshots of the references and tells you which checks it couldn't run. Image and logo services connect through MCP, which most agents support.

## Skills it uses

Required: [Impeccable](https://github.com/pbakaus/impeccable), [frontend-design](https://github.com/anthropics/skills), and the official [GSAP skills](https://github.com/greensock/gsap-skills).
Recommended: Emil Kowalski's [design and motion skills](https://github.com/emilkowalski/skill), Vercel's [web design and React guidelines](https://github.com/vercel-labs/agent-skills), [userinterface-wiki](https://github.com/raphaelsalaja/userinterface-wiki), [extract-design-system](https://github.com/arvindrk/extract-design-system), [shadcn](https://github.com/shadcn/ui).

The full list is in [`skills/imolern-studio/skills.json`](skills/imolern-studio/skills.json). The skill checks and installs them for you.

## Scope

Websites and web apps. Native mobile apps are not covered yet.

## Licence

MIT
