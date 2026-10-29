# OpenTina Website

Official website of the [OpenTina](https://github.com/opentina-org) project — **https://opentina.org**

Built with [Hugo](https://gohugo.io) (extended), deployed to **GitHub Pages** via **GitHub Actions** (static mode).

## Highlights

- **Responsive** — works on phones, tablets and desktops.
- **Light & dark themes** — follows the system preference by default, with a manual toggle (choice is remembered).
- **9 languages** — English (default), 简体中文, 繁體中文, 日本語, Русский, 한국어, Deutsch, Français, Español.
- **Clean URLs** — `/`, `/about/`, `/docs/`, and `/{lang}/…` for translations (no query strings, no hashes).
- **Localized 404 page**.

## URL design

| URL | Content |
| :--- | :--- |
| `/` | English home page (default language, no prefix) |
| `/about/`, `/docs/` | English content pages |
| `/zh/…` | Simplified Chinese (`/zh/`, `/zh/about/`, `/zh/docs/`) |
| `/zh-tw/…` | Traditional Chinese |
| `/ja/…`, `/ru/…`, `/ko/…`, `/de/…`, `/fr/…`, `/es/…` | Other languages |
| `/index.xml` | RSS feed |
| `/sitemap.xml` | Sitemap (hreflang-aware) |

## Local development

```bash
# Hugo >= 0.146 (extended) is required
hugo server -D
```

Production build:

```bash
hugo --gc --minify
```

## Project layout

```
hugo.toml               # site config, languages
assets/css/main.css     # single stylesheet, CSS variables for themes
layouts/                # templates (baseof, header/footer partials, home, aliases, redirects)
i18n/*.toml             # UI strings for all 9 languages
content/<lang>/         # _index.md + about.md + docs.md per language
.github/workflows/      # GitHub Pages deployment
```

## Deploying

The site is built and published automatically by the `Deploy website` workflow
(`.github/workflows/hugo.yml`) on every push to `main`.

One-time repository setup:

1. **Settings → Pages → Build and deployment → Source**: select **GitHub Actions**.
2. **Settings → Pages → Custom domain**: enter `opentina.org`, then enable **Enforce HTTPS**
   once the DNS records (`opentina.org` and `www.opentina.org` CNAME → `<org>.github.io`)
   have propagated.
3. Optionally set the domain in a `CNAME` file under `static/` if you prefer committing it.

## License

Website content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
