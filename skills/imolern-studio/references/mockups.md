# Style tile and mock-ups

Mock-ups are plain HTML, CSS and JS, served locally. They are fast to change, easy to review in any browser, and they become the source of truth that the build copies exactly.

## Folder layout

```
design/mockups/
  01-style-tile.html      the design system on one page
  _tokens.css             colours, type, spacing, radii (light + dark)
  _site.css               shared layout, nav, footer, components
  _site.js                shared behaviour: theme switch, nav, menus
  _signature.js           the signature piece, mounted by attribute
  _nav.html  _foot.html   shared partials
  src/
    _head.html            shared <head>; {TITLE} is replaced per page
    02-home.html          page sources with <!--HEAD-->, <!--NAV-->, <!--FOOT-->
    03-pricing.html
  02-home.html …          built pages (generated, don't edit)
```

Copy `scripts/build_mockups.py` into `design/mockups/` and run `python3 _build.py` after any change to a partial or source. Each source starts with `<!--TITLE: Page title-->`.

Serve with `python3 -m http.server 8790` from the project root and give the user `http://localhost:8790/design/mockups/02-home.html`. If the session has a preview/launch config, add the server there.

## The style tile (`01-style-tile.html`)

Show, in light and dark side by side or with a working switch:
- **Colour:** each token with its name, hex and use. Check text contrast (4.5:1 body, 3:1 large).
- **Type:** the scale from display to small, with real sentences from the brief, not lorem ipsum.
- **Components:** buttons (all states), inputs, select, checkbox, card, badge, nav item, link, toast. Focus rings visible.
- **Icons:** the chosen set (e.g. Phosphor) at the sizes used.
- **Spacing and radii:** the scale, with a note on which radius goes where (hierarchy, not one radius for everything).
- **A sample section** built with all of the above.
- **The signature idea** running.

## Page mock-ups

- Real copy from the brief, written plainly from the visitor's side. Unknowns are marked and listed in pending items.
- Real assets from the integrations; generated people labelled as examples.
- Every interactive part works: nav and dropdowns (labels that are also links), phone menu, tabs, carousels, theme switch, forms with validation and success states (mark simulated ones in progress notes).
- Dashboards and portals: a version for each state (empty, loading, error, full) and the phone layout.
- Scope page-specific CSS under a page class (`.pg-pricing`) from the start; it makes the port straightforward.
- No horizontal scroll at 375px. Motion follows [motion.md](motion.md).

## Before showing the user

Run Impeccable `critique` on the page and fix what it finds. Look at it yourself at 1440px and 375px, light and dark. Then share the links and ask for approval page by page.
