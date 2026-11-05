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

```bash
npx skills add Kiki731/imolern-studio -g -a claude-code
```

Or clone and link it:

```bash
git clone https://github.com/Kiki731/imolern-studio.git
ln -s "$PWD/imolern-studio/skills/imolern-studio" ~/.claude/skills/imolern-studio
```

Then start Claude Code and say: **"Let's build a website with Imolern Studio."**

## Skills it uses

Required: [Impeccable](https://github.com/pbakaus/impeccable), [frontend-design](https://github.com/anthropics/skills), and the official [GSAP skills](https://github.com/greensock/gsap-skills).
Recommended: Emil Kowalski's [design and motion skills](https://github.com/emilkowalski/skill), Vercel's [web design and React guidelines](https://github.com/vercel-labs/agent-skills), [userinterface-wiki](https://github.com/raphaelsalaja/userinterface-wiki), [extract-design-system](https://github.com/arvindrk/extract-design-system), [shadcn](https://github.com/shadcn/ui).

The full list is in [`skills/imolern-studio/skills.json`](skills/imolern-studio/skills.json). The skill checks and installs them for you.

## Scope

Websites and web apps. Native mobile apps are not covered yet.

## Licence

MIT
