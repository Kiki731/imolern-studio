# Checks

Two kinds: **design judgement** (Impeccable) and **things a machine can verify**. Do both; neither replaces the other.

## Impeccable — on everything

| When | Run | Then |
|---|---|---|
| First time in a project | `impeccable init` if there's no PRODUCT.md (use the brief) | Keep PRODUCT.md and DESIGN.md current as the direction settles |
| Style tile | `critique` | Fix, show the user |
| Each mock-up | `critique` | Fix, show the user |
| Built pages | `audit`, then `polish` | Fix, re-run the machine checks |
| Motion-heavy sections | `animate` guidance (and `review-animations` if installed) | Simplify anything that stutters or distracts |

Impeccable's bans and craft floor override taste. If it flags a generic pattern the user explicitly asked for, the user's brief wins; say so.

## Machine checks — before any page is called done

- [ ] **Accessibility:** run axe-core in the page, in light and dark. Zero violations, or each remaining one explained (e.g. a decorative element).
  ```js
  await import('https://cdn.jsdelivr.net/npm/axe-core@4.10.2/axe.min.js');
  const r = await axe.run(document, { resultTypes: ['violations'] });
  r.violations.map(v => ({ id: v.id, impact: v.impact, n: v.nodes.length, first: v.nodes[0]?.target }));
  ```
- [ ] **Widths:** 375, 768, 1440. No horizontal scroll: `document.documentElement.scrollWidth <= innerWidth`.
- [ ] **Themes:** light and dark both readable; theme switch works and is remembered.
- [ ] **Reduced motion:** still frames shown, nothing essential lost.
- [ ] **Keyboard:** every control reachable with Tab, visible focus, Escape closes menus, menus open with Enter/ArrowDown.
- [ ] **Console:** no errors or warnings on load, on interaction, and after navigating between pages.
- [ ] **Matches the mock-up:** `scripts/layout_compare.js` shows no unexplained differences.
- [ ] **Build:** production build passes; type check and lint clean of errors.
- [ ] **Performance:** images sized and compressed, fonts subset or limited, motion paused off-screen. Check the first-load size and say it in the handover.
- [ ] **Production basics:** page titles and descriptions, share image (Open Graph), favicon, sitemap, robots, 404 page, no placeholder links.

## Copy check

- Plain words, sentence case, active voice. Buttons say what happens ("Book my demo", not "Submit").
- No invented numbers, customers, quotes or logos. Everything unconfirmed is on the pending list.
- No filler words, no "AI-sounding" phrasing. Read each heading aloud.
