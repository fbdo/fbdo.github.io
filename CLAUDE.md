# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal website / blog built with the [Hugo](https://gohugo.io/) static site generator (extended, currently 0.163.3) using the `hugo-coder` theme. The site is published via GitHub Pages at [https://fbdo.github.io/](https://fbdo.github.io/) (a user site served from the root).

The theme is consumed as a **Hugo Module** (`github.com/luizdepra/hugo-coder`), declared in `config.toml` under `[module]` and pinned in `go.mod` / `go.sum`. There is no `themes/` directory and no git submodule. Resolving the theme requires **Go** to be installed (`hugo mod` shells out to it).

## Commands

```bash
# Local preview (includes drafts); downloads the theme module on first run
hugo server -D

# Production build (output goes to ./public)
HUGO_ENVIRONMENT=production hugo --gc --minify

# Create a new post (uses archetypes/default.md, starts as draft = true)
hugo new posts/my-post-title.md

# Theme module maintenance
hugo mod get -u github.com/luizdepra/hugo-coder   # update theme to latest
hugo mod tidy                                      # prune go.mod/go.sum
```

## Architecture

- `config.toml` — site-wide config. Key points:
  - `[module].imports` pulls in the theme (replaces the old `theme =` key).
  - `uglyURLs = true`, so individual posts render to `.html` paths (e.g. `/posts/belonging-clues.html`). This preserves the URLs indexed under the previous site. **Section list pages still render to a directory index** (`/posts/`, not `/posts.html`) — menu links to lists must use the trailing-slash form.
  - Config uses modern Hugo keys: `[pagination].pagerSize`, `[services.disqus]`, `[markup.highlight]`, `[markup.goldmark.renderer]`, `locale`, and `languages.en.label`. Avoid reintroducing the pre-0.158 keys (`paginate`, `pygments*`, `languageCode`, `languageName`, top-level `disqusShortname`/`googleAnalytics`).
- `content/posts/` — blog posts in Markdown. Front matter is TOML (`+++` delimiters), unlike the archetype which uses YAML (`---`). Set `draft = false` to publish.
- `static/` — assets copied verbatim to the site root: images (under `static/images/<post-slug>/`), GPG key, CSS, and the Google Search Console verification file (`googlefd8941a18ee7339d.html` — keep it; it must remain reachable at the root).
- `archetypes/default.md` — template for `hugo new`.

## Deployment

CI/CD is GitHub Actions (`.github/workflows/hugo.yml`). On push to `master` (or manual `workflow_dispatch`) it installs Hugo extended + Go, builds with `--gc --minify`, and deploys to GitHub Pages via `actions/upload-pages-artifact` + `actions/deploy-pages`. The workflow injects `--baseURL` from the Pages config at build time. GitHub Pages must be set to the "GitHub Actions" source in repo Settings → Pages.
