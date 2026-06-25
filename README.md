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
