# Herbaferm Singapore website

Static website for Herbaferm Pte. Ltd. (Singapore): Shop, Learn, About and Partners, with a cart, site search and a chat assistant. No framework and no build step is needed to host it.

## What is in this repo

| Folder | What it is |
|---|---|
| `site/` | The finished website. Plain `index.html`, `css/`, `js/` and `assets/images/`. This is the folder you publish. |
| `generator/` | The source the site is generated from (page content in `src/pages.py` and `src/extra.py`, styles in `src/site.css`, behaviour in `src/site.js` and `src/chat.js`, original images in `assets/`). |
| `server/` | A small Cloudflare Worker that lets the chat assistant call a language-model API without exposing the key. |
| `.github/workflows/pages.yml` | Publishes `site/` to GitHub Pages on every push to `main`. |

## Search (SEO and AI search) additions

- Ten sourced blog articles and a microbial dysbiosis explainer live at real URLs, `site/learn/<slug>/index.html`, written in `generator/src/blog.py`. The Learn page has a Blog tab that lists them.
- `generator/src/seo.py` builds the JSON-LD (Organization, WebSite, Product, FAQPage on the home page; Article, FAQPage, BreadcrumbList, plus Book and Person on the dysbiosis page), `robots.txt` and `sitemap.xml`.
- Canonical URLs, the sitemap and the schema use the GitHub Pages address by default (`https://ernusho.github.io/herbaferm-sg-website/`). To use another domain, build with `HF_SITE_URL=https://example.com/ python3 generator/build.py --site site`.
- Everything marked To confirm or To supply (medical reviewer, review by Adam Bóday, ResearchGate link) still needs Herbaferm's input.

## Run it on your computer

```bash
python3 -m http.server 8000 -d site
# open http://localhost:8000
```

## Change the content

1. Edit the files in `generator/src/` (text lives in `pages.py` and `extra.py`).
2. Rebuild the site: `python3 generator/build.py --site site`
3. Commit both the `generator/` and `site/` changes, then push.

If you would rather edit HTML directly, delete `generator/` and treat `site/` as the source. Do not do both.

## Publish it

**GitHub Pages (simplest).** In the repo go to Settings, then Pages, and set Source to "GitHub Actions". Every push to `main` then publishes `site/`. For `herbafermsg.com`, add the custom domain under Pages and create the DNS records GitHub shows you.

**Netlify or Cloudflare Pages.** Connect this repo, leave the build command empty and set the publish directory to `site`.

The site uses `#` links for pages (for example `/#drops`), so no server rewrite rules are needed.

## Turn on the live chat assistant

The page ships with built-in answers, so the chat works with no server. For live AI answers:

1. Deploy `server/chat-worker.js` with `npx wrangler deploy` (run inside `server/`) and store the key with `npx wrangler secret put ANTHROPIC_API_KEY`.
2. Put your site's address in `ALLOWED_ORIGINS` in the worker.
3. In `site/index.html`, above the chat script, add: `<script>window.HF_CHAT_ENDPOINT = "https://<your-worker>.workers.dev/";</script>` (or add it to the shell in `generator/build.py`).

The assistant's fact sheet and rules are at the top of `generator/src/chat.js`. Keep them in step with the products.

## Before launch

- Everything tagged **To confirm** or **To supply** on the pages needs Herbaferm's input. Search the site for those tags.
- Checkout is not connected. The cart is a front-end only. Choose a store or payment provider (an IT person should set this up).
- Shipping, returns, privacy and terms text is still to be supplied.
- Test on real phones and tablets.
- Health wording: no medical claims, never "HSA approved". The leaflets state no health effects can be attributed to the products.
- The Design evidence page (`#insight`) is for the project review. Remove its footer link before launch.

## Notes

- Prices: Drops S$55, Fiber Elite S$55, Prefer HF400 S$45.
