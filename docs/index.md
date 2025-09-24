# Theophysics MkDocs Pipeline

This repository provides a complete automation stack for generating three
independent MkDocs sites from a single Obsidian vault.  The solution is
optimised for David Lowe's research workflow and mirrors the live
Cloudflare Pages deployment (`theophysics.pages.dev`,
`theophysics-template.pages.dev`, `theophysics-blog.pages.dev`).

## Key Features

- YAML frontmatter controls which notes are published to each site.
- Lantana-inspired dark theme blended with Terminal UI accents.
- Advanced markdown support including PyMdown extensions and callouts.
- HTML5 audio/video embedding with playlists and download links.
- Automatic conversion of `[[wikilinks]]` and attachment management.
- Absolute media references are ingested safely by copying them into each
  MkDocs build, so external audio or video files remain playable.
- Macros, search, tags, and minified output for every generated site.

## Repository Structure

```text
obsidian-vault/
├── research-notes/           # Source markdown notes from Obsidian
├── templates/                # Optional Obsidian templates
├── automation/               # Existing deployment logic
└── published/                # MkDocs build targets (generated)
```

Automation assets live under
`automation/website-deployment/mkdocs-pipeline` and include the builder,
custom theme overrides, and static assets.

## Usage

```bash
python automation/website-deployment/mkdocs-pipeline/build.py --verbose
```

The command scans the vault, materialises three MkDocs projects inside
`obsidian-vault/published/`, and preserves the directory layout expected
by the Cloudflare Pages deployments.

Pass `--site production`, `--site research`, or `--site template` to
build a single site.  Add `--clean` to remove previous builds.

## Next Steps

1. Copy your live Obsidian vault into `obsidian-vault/`.
2. Adjust the site metadata in `build.py` if URLs or palettes change.
3. Run the build script and then the existing deployment workflow under
   `obsidian-vault/automation/website-deployment`.
4. Customise CSS/JS in `automation/website-deployment/mkdocs-pipeline` as
   needed for further branding.
