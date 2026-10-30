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
| `/en/…` | Redirect stubs to the default-language URLs (`/en/` → `/`, `/en/docs/` → `/docs/`) |
| `/404.html` | Branded 404 page (GitHub Pages serves it for unknown paths) |
| `/index.xml` | RSS feed |
| `/sitemap.xml` | Sitemap (hreflang-aware) |

Every language is declared with its own `contentDir` (`content/<lang>`) in `hugo.toml`.
This is what keeps the default language at the site root: without it the `content/<lang>/`
directories are published as ordinary sections (that is how `/about/` and `/docs/` used to 404
while `/en/about/`, `/zh/about/` worked).

## Local development

```bash
# Hugo >= 0.146 (extended) is required — CI pins 0.147.9
hugo server -D
```

Production build (same flags as CI):

```bash
hugo --gc --minify --baseURL "https://opentina.org/"
```

## Checks

Two scripts make link rot and half-finished translations visible before pushing:

```bash
python3 scripts/check_links.py public          # 站内链接：把每个 href/src 映射到构建产物，列出不可达目标
python3 scripts/check_links.py public --live   # 再对 https://opentina.org 逐条实测 HTTP 状态
python3 scripts/check_i18n_links.py public     # 语言切换器与 hreflang：每页 × 9 种语言的目标都必须存在
python3 scripts/audit_i18n.py                  # i18n 键覆盖：缺键、多余键、与英文完全相同的疑似未译条目
python3 scripts/audit_content.py               # 内容层：各语言 about/docs 的标题数、链接数、仓库清单是否与英文一致
```

## Project layout

```
hugo.toml               # site config, languages (each with its own contentDir) and per-language params
assets/css/main.css     # single stylesheet, CSS variables for themes
layouts/                # templates (baseof, header/footer partials, home, 404)
i18n/*.toml             # UI strings for all 9 languages
content/<lang>/         # _index.md + about.md + docs.md per language
scripts/                # link and translation checks (see above)
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
