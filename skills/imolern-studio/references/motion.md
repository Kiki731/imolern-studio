# Motion

Motion is where AI-made sites most often look cheap: everything fades up, every card bounces on hover. Here, motion explains, answers the visitor, or carries the signature idea. Nothing else moves.

## Library

- **GSAP is the default** for any stack. All plugins (ScrollTrigger, SplitText, Flip, Draggable, DrawSVG, MorphSVG) are free. Use the GSAP skills.
- **Motion (motion.dev)** is fine for React UI that opens, closes and reorders (menus, panels, lists). Don't run it alongside GSAP for the same job.
- **anime.js** or a hand-written canvas is fine if the user asks or the references call for it.
- **Three.js / canvas / shaders** only for a signature piece that needs it, never for decoration.

Pick once in the direction doc. One library per job keeps the site light.

## Rules

1. **One orchestrated moment** per page (usually the hero) lands better than effects on every section.
2. **Respect reduced motion.** Under `prefers-reduced-motion: reduce`, show the final state or a still frame. Use `gsap.matchMedia()`. Support a `?still` query flag in mock-ups to check stills quickly.
3. **Durations:** UI feedback 150–250ms; reveals 400–700ms; signature pieces can run longer or loop slowly. Ease out for entrances, ease in-out for moves.
4. **Animate transform and opacity only** where possible. No layout properties in loops.
5. **Pause what isn't visible:** IntersectionObserver or ScrollTrigger `toggleActions`; stop canvas loops off-screen and when the tab is hidden.
6. **Clean up.** In React, `useGSAP` or `gsap.context()` and revert on unmount; listeners and observers are released when a page unmounts, so client-side navigation doesn't leak.
7. **Theme aware.** If motion changes with theme (e.g. a glow only in dark mode), listen for the theme change, don't reload.
8. **Answer people.** Hover, press, open, close and confirm all get quick, clear feedback.

## The signature piece

Decide it in the direction doc: what it is, where it appears, how it behaves in light and dark, and its still frame. Build it as one reusable module the pages mount by attribute (e.g. `data-signature="hero"`), so it can appear on other pages without copying code.

## Reviewing motion

After building, run the `review-animations` skill if installed, and Impeccable's `animate` guidance. Check at 1× and with CPU throttling; anything that stutters gets simplified.
