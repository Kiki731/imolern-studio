---
name: imolern-studio
description: End-to-end studio method for designing and building websites and web apps that look hand-made, not AI-generated — marketing sites, e-commerce, landing pages, dashboards, portals and admin tools. Checks and installs the design and motion skills it needs, takes the brief and stack, studies the user's reference sites one by one, drafts a design direction, builds a style tile and HTML mock-ups for approval, then ports them exactly into the chosen stack with GSAP motion, running Impeccable on everything. Use when the user wants to design or build a website or web app, start a redesign, says "Imolern Studio", or asks to "build a site like these references". Not for native mobile apps.
---

# Imolern Studio

A design studio method in nine steps. Each step ends with something the user can see, and the steps marked **Stop** wait for the user's yes before moving on. The bar is the best-built product sites, not "good for AI".

Talk to the user in plain language, outcome first. Never invent facts about their business: prices, customers, logos, stats, legal text and domains come from the user or go on the pending list.

## Ground rules (apply in every step)

- **Ask before acting outside the project.** Checking installed skills, installing skills, opening reference sites, connecting services and committing all need the user's permission first. One clear question, then act.
- **Review the user's ideas before building them.** When the user suggests a change, judge it with design sense first and say whether it helps; then build what they choose.
- **Run Impeccable on everything you make.** Style tile, every mock-up, every built page. Fix what it flags before showing the user. See [references/checks.md](references/checks.md).
- **One signature idea per site.** One memorable element (a motion piece, an interaction, a type treatment) carries the identity; everything around it stays quiet and disciplined.
- **Light and dark from day one** for marketing sites, unless the user says otherwise.
- **Nothing is faked.** A form without a backend says so in the progress notes; a portal action without an endpoint says so on screen ("Coming soon"), never pretends to work.
- **No commits or pushes until the user asks.** Ask the user for their own working rules in step 2 and follow them.
- **Keep notes in the project** (`docs/`) so work survives across sessions: brief, references, direction, pending list, progress. Templates are in [templates/](templates/).

## Step 1 — Setup: skills

1. Ask: "Imolern Studio uses a set of design and motion skills. May I check which ones you already have installed?"
2. On yes, run `python3 <skill-dir>/scripts/check_skills.py`. It reads [skills.json](skills.json) and lists what is installed and missing, with the install commands.
3. Tell the user what's missing (required first, then recommended, each with one line on why). Ask permission to install.
4. On yes, run the printed commands (`npx skills add <repo> -g -a claude-code -s <skill> -y`). Install only what is missing.
5. Run the check again and confirm: "All set — N skills installed." If an install fails, say which and why, and continue only if the required set is complete.

New skills load in the next session. If a required skill was just installed and isn't available yet, tell the user to start a new session (or reload skills) and pick up from step 2; the notes in `docs/` carry the context.

## Step 2 — Brief and stack

If the user has already sent a brief, read it and ask only what's missing. Otherwise ask, in one message:

- **What kind of site?** Marketing, e-commerce, landing page, dashboard, portal, admin tool, other web app. This sets the whole approach — see [references/site-types.md](references/site-types.md).
- **The product**, who it's for, and the one job the site must do.
- **Pages or screens** needed.
- **Stack.** Ask; suggest the default for the site type from site-types.md so a beginner isn't stuck.
- **Brand assets** they already have (logo files, colours, fonts) and anything that must not change.
- **Working rules** (when to commit, branch, how they like updates).

Write `docs/brief.md` and start `docs/pending-items.md` (the things only the user can supply). Read back a three-line summary.

## Step 3 — Integrations

Images and logos are needed from the first mock-up, so set these up now. See [references/integrations.md](references/integrations.md).

- **Brandfetch** — real partner and customer logos.
- **Unsplash** — photography.
- **Magnific** — generated and upscaled images.

Check which are already connected; for each missing one, explain how to connect it and where the key goes. **API keys go into connector settings or a git-ignored `.env`, never into the chat.** Any can be skipped; note the gap in the pending list.

## Step 4 — References (the most important step)

Ask for the reference links: "Share the sites you'd like this to feel like — and for each, what you like about it if you know." If they have none, propose 4–6 strong references for their site type and ask them to pick.

Then **study each site one by one**, with the browser, following [references/reference-study.md](references/reference-study.md): layout and section rhythm, type, colour, imagery, motion (trigger, duration, easing), interactions, nav and footer, light/dark, phone layout. Read real values from the page, don't guess them.

For each site write **what to take** and **what to avoid**, into `docs/design-references.md`. Then draft `docs/design-direction.md`: the patterns worth reusing, a palette, type, layout concept, the motion approach, and the signature idea — each traced to a reference.

**Stop.** Show the draft and ask for approval or changes. Don't design until the user says yes.

## Step 5 — Style tile (always made)

One HTML page showing the design system: colours (light and dark), type scale, buttons, inputs, cards, icons, spacing, a sample section, and the signature idea working. See [references/mockups.md](references/mockups.md).

Run Impeccable (`critique`, then fix). Check it at phone and desktop width, both themes. Then show it.

**Stop.** The user audits it. Iterate until they like it. If they say the direction is right and want to go straight to the build, skip step 6.

## Step 6 — Mock-ups

HTML mock-ups of each page, sharing one head, nav, footer and stylesheet through the build script (`scripts/build_mockups.py`). Real copy, real assets, real states. Motion as it will ship.

For dashboards and portals, mock up every state: empty, loading, error, full, and the phone layout.

Run Impeccable on each page and fix before showing. Serve them locally and give the user the links.

**Stop.** The user approves each page (or asks for changes). Approved mock-ups become the source of truth.

## Step 7 — Build

Port the approved mock-ups into the chosen stack **exactly** — same markup, CSS and behaviour, scoped so pages can't clash. Follow [references/build-and-port.md](references/build-and-port.md) and [references/motion.md](references/motion.md) (GSAP by default).

Prove the build matches: measure element positions on mock-up and built page at desktop and phone width and compare (`scripts/layout_compare.js`). Any difference is either fixed or explained to the user.

## Step 8 — Checks

Run the full list in [references/checks.md](references/checks.md): Impeccable `audit` and `polish`, accessibility in both themes, phone and desktop widths, no sideways scroll, reduced motion, keyboard use, no console errors, production build passes, and the production basics (titles, descriptions, sitemap, robots, share image, favicon, icons).

## Step 9 — Handover

Update `docs/progress.md`: what's built, how to run it, how to update a page (edit mock-up → rebuild → port), what's simulated or waiting on a backend, and the pending list. Tell the user in a short message, outcome first. Commit only if asked.

## When things change later

- **Small change to an approved page:** edit the mock-up, rebuild, port, re-check that page.
- **New page or section:** reopen the matching reference first, mock it up, Stop for approval, then build.
- **User suggests a direction change:** review it against the direction doc, say what it helps and what it costs, then do what they decide and update the doc.
