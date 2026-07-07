# fabiooliveira.github.io

Personal website and blog of Fabio Oliveira, published at
[https://fbdo.github.io/](https://fbdo.github.io/).

Built with the [Hugo](https://gohugo.io/) static site generator (extended)
using the [hugo-coder](https://github.com/luizdepra/hugo-coder) theme.

## Prerequisites

- [Hugo extended](https://gohugo.io/installation/) (0.163.3 or later)
- [Go](https://go.dev/) — required because the theme is consumed as a
  [Hugo Module](https://gohugo.io/hugo-modules/)

```bash
brew install hugo go
```

## Local development

```bash
# Start the dev server with drafts; downloads the theme module on first run
hugo server -D
```

The site is then available at http://localhost:1313/.

## Building

```bash
# Production build; output goes to ./public
HUGO_ENVIRONMENT=production hugo --gc --minify
```

## Writing a post

```bash
# Creates content/posts/<name>.md from archetypes/default.md (draft = true)
hugo new posts/my-post-title.md
```

Set `draft = false` in the post's front matter to publish it. Posts use TOML
front matter (`+++` delimiters).

## Readability checks

A small Python tool in [`tools/readability`](tools/readability) scores a post's
prose against common readability metrics (Flesch Reading Ease, Flesch-Kincaid
Grade, Gunning Fog, SMOG, Coleman-Liau, ARI, Dale-Chall). It strips front
matter, code fences, tables, images, citation markers, link URLs, and the
References section before scoring, so the numbers reflect the prose only.

### One-time setup

```bash
# Creates a local virtualenv and installs dependencies (venv is gitignored)
python3 -m venv tools/readability/.venv
tools/readability/.venv/bin/pip install -r tools/readability/requirements.txt
```

### Scoring a post

```bash
# Score one or more posts
tools/readability/.venv/bin/python tools/readability/readability.py \
  content/posts/my-post.md

# Score every post at once
tools/readability/.venv/bin/python tools/readability/readability.py \
  content/posts/*.md
```

Each metric is flagged `ok` or `review` against a best-practice target. For a
technical audience, aim for Flesch Reading Ease of 50+ and grade-level metrics
around 10-12; Dale-Chall runs high for jargon-heavy topics and is mostly
useful for spotting relative changes between drafts.

## Updating the theme

```bash
hugo mod get -u github.com/luizdepra/hugo-coder   # pull the latest theme
hugo mod tidy                                      # prune go.mod / go.sum
```

## Deployment

Deployment is automated with GitHub Actions
([`.github/workflows/hugo.yml`](.github/workflows/hugo.yml)). Every push to
`master` builds the site and deploys it to GitHub Pages. The Pages source must
be set to **GitHub Actions** in the repository settings.
