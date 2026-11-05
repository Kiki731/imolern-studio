# Building from the mock-ups

The approved mock-ups are the design. The build copies them exactly into the chosen stack; it does not reinterpret them. If something has to change during the build, change the mock-up first.

## The port, in any stack

1. **Tokens and shared CSS** move into the app's global styles. Shared assets (logos, portraits, fonts) live in one folder that every app in the project uses, copied in at build time rather than duplicated by hand.
2. **Scope every page's CSS** under its page class (`.pg-<slug>`), and shared frame CSS under a site class. Routers keep CSS loaded across client-side navigation, so unscoped rules leak between pages.
3. **Markup** converts mechanically (HTML → JSX for React: `class`→`className`, `for`→`htmlFor`, self-closing tags, `style` objects, `value`/`checked` → `defaultValue`/`defaultChecked`). Write a small script for this when there are more than two pages, so a mock-up change can be re-ported in one command.
4. **Behaviour** (the mock-up's scripts) becomes one module per page with an `init()` that returns a clean-up function. Every listener, observer, timer, animation frame and GSAP context registers its clean-up, and the page runs `init` on mount and the clean-up on unmount.
5. **Shared nav and footer** become components, with the current page marked from the route.
6. **Links:** replace mock-up file links (`03-pricing.html`) with routes (`/pricing/`). Fix every placeholder link; a link with nowhere to go is removed or listed as pending.
7. **Icons:** subset the icon font or inline only the icons used.

## Stack notes

- **Next.js (App Router):** route groups for shared layouts; client components only where behaviour runs; static export for marketing sites; `metadata` per page; `sitemap.ts` and `robots.ts`.
- **React + Vite:** React Router routes, pages lazy-loaded, TanStack Query for data with refetch only while the tab is visible; a clear "This page didn't load — Reload" state for failed chunks.
- **Other stacks** (Astro, SvelteKit, plain HTML): same principles — scoped CSS, one behaviour module per page with clean-up, shared assets in one place.

## Proving it matches

With both the mock-up and the built page running, use `scripts/layout_compare.js` in the browser at 1440px and 375px, in both themes. It records every visible element's position and size and reports differences between the two. The target is zero differences; any that remain are either fixed or explained to the user (for example, a removed dead link).

Also click through: nav, menus, phone menu, theme switch, forms, and navigate between pages without reloading to confirm motion and listeners are cleaned up and there are no console errors.

## Backend

Wire forms and actions to real endpoints where they exist. Where they don't, keep the mock-up's simulated success only on marketing forms and list it in progress notes as "simulated"; in portals, show the missing action plainly instead of faking it.
