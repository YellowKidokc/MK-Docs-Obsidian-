# MkDocs Deployment Integration

The MkDocs pipeline outputs three ready-to-build projects into
`../published/<site>`.  Existing Cloudflare Pages automation can invoke
`mkdocs build` (or `mkdocs gh-deploy`) within each of these directories
before uploading the generated `site/` folder.

1. `../published/production`
2. `../published/research`
3. `../published/template`

Each directory contains:

- `mkdocs.yml` configured with the Lantana + Terminal theme.
- `docs/` populated with filtered markdown and media assets.
- `macros/` and theme overrides required for the custom look and feel.

Invoke the build script prior to deployment to keep the published sites
in sync with the Obsidian vault.
