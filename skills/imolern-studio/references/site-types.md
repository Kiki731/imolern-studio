# Site types

The kind of site decides the approach. Ask in step 2, then use the matching column.

| | Marketing / landing | E-commerce | Dashboard / portal / admin |
|---|---|---|---|
| **Visitor's success** | Understands and acts (sign up, book, buy) | Finds, trusts, buys | Finishes a task quickly |
| **Impeccable mode** | Persuade | Persuade (product pages lean Operate) | Operate |
| **Ambition** | Bold. One signature idea, real imagery, orchestrated motion | Product imagery leads; trust and clarity over spectacle | Precision and restraint; brand lives in details |
| **Motion** | One hero moment, scroll reveals where they explain, motion in dark mode | Quick, useful: add-to-cart feedback, image zoom, filters | Only to show what changed: panels, toasts, state changes. 150–250ms |
| **Must design** | Hero, proof, product shown in use, pricing, closing call to action, footer | Listing, filters, product page, cart, checkout, empty cart, order confirmation | Every state: empty, loading, error, full, no permission; phone layout; keyboard use |
| **Default stack to suggest** | Next.js (App Router, static export) | Next.js | React + Vite, React Router, TanStack Query |
| **Components** | Hand-built from the mock-ups | Hand-built; consider shadcn for forms | shadcn/ui as a base, restyled to the style tile |

## Notes by type

**Marketing / landing**
- Show the real product in the hero (a product frame, a live demo), not an abstract illustration.
- Every claim is something the user can stand behind. Stats, logos and quotes come from the user or wait on the pending list.
- Theme switch (light / dark / system) in the footer works well; dark mode can reveal the signature motion.

**E-commerce**
- Judge the platform from the user's references and brief (hosted store, payments provider or custom); don't ask unless it's unclear and blocks the build.
- Prices, stock, shipping and returns copy are pending-list items until the user supplies them.
- Checkout is Operate mode even on a Persuade site: plain, fast, no decoration.

**Dashboard / portal / admin**
- Every action uses a real endpoint. If there isn't one, the screen says so ("Coming soon", "Reply in Slack") rather than faking success. List these gaps in progress notes.
- Data refreshes only while the tab is visible. Pages load on demand.
- Density and scanability over spectacle: label/value lists, status dots, light borders, a thin icon rail.

## Other web apps
Pick the closest column. A tool's landing page is Persuade; the tool itself is Operate.
