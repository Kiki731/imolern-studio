# Integrations: logos, photos, images

Set these up in step 3, before mock-ups, because real assets change how a design reads. Each one is optional; a skipped one goes on the pending list.

**Never ask the user to paste an API key into the chat.** Keys go into the service's connector settings, or into a git-ignored `.env` file the user edits themselves. Check `.env` is listed in `.gitignore` before anything is committed.

## How to check what's connected

1. Look at the tools available in the session for names containing `brandfetch`, `unsplash` or `magnific`. A connected connector shows up as tools.
2. Look for keys in the project's `.env` (names below) without printing their values: `grep -c '^UNSPLASH_ACCESS_KEY=.\+' .env`.
3. Tell the user which are ready and which aren't.

## Brandfetch — logos

For partner, integration and customer logos, so the site never uses hand-drawn or guessed marks.

- **Connector:** if a Brandfetch connector or MCP server is available, use it.
- **API:** the user creates a free account at brandfetch.com, copies their **client ID** from the developer dashboard and adds `BRANDFETCH_CLIENT_ID=` to `.env`. Logos are then fetched by domain from the Logo API (`https://cdn.brandfetch.io/<domain>?c=<client id>`). Check Brandfetch's Logo API docs for the type, theme and size options (icon, symbol, full logo, dark variant).
- Download the files into the project (e.g. `assets/logos/<name>.svg`) rather than hot-linking, and record the source.
- Using a company's logo implies a relationship. Customer logos need the user's OK; integration logos are fine when the integration is real.

## Unsplash — photography

- **Connector:** use an Unsplash connector if available.
- **API:** the user creates an app at unsplash.com/developers, copies the **Access Key**, and adds `UNSPLASH_ACCESS_KEY=` to `.env`. Search with `GET https://api.unsplash.com/search/photos?query=…` and the header `Authorization: Client-ID <key>`.
- Follow Unsplash's guidelines: credit the photographer and trigger the download endpoint when a photo is used. Keep a credits list in `docs/`.
- Download at the size you need, then compress (WebP/AVIF). Never hot-link full-size originals.

## Magnific — generated and upscaled images

For images no photo library has: skies, textures, product scenes, portraits for examples, upscaling small assets.

- **Connector:** Magnific is available as a connector/MCP server. If it isn't connected, the user connects it in their Claude connector settings and signs in there.
- Check the account balance before a batch and tell the user the expected cost.
- Generated people are labelled as examples on the site ("Portraits are generated examples").
- Save outputs into the project with the prompt used, so they can be regenerated.

## If nothing is connected

Design with clearly marked placeholders (neutral blocks with a label like "Partner logo"), and list every placeholder in `docs/pending-items.md`. Don't fill gaps with made-up logos or stock clichés.
