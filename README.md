# Theophysics MkDocs Pipeline

This repository converts David Lowe's Obsidian vault into three
independent MkDocs sites that ship to the existing Cloudflare Pages
projects:

- `theophysics.pages.dev` – curated production research
- `theophysics-template.pages.dev` – full research vault
- `theophysics-blog.pages.dev` – AI collaboration template

The automation replaces the earlier static HTML exporter with a
frontmatter-driven pipeline that honours selective publishing, advanced
markdown extensions, and multimedia content.

## Quick Start

1. Place the Obsidian vault in `obsidian-vault/` (the sample content is a
   working reference).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Build the MkDocs projects:

   ```bash
   python automation/website-deployment/mkdocs-pipeline/build.py --verbose
   ```

4. Deploy using the existing scripts in
   `obsidian-vault/automation/website-deployment`.

## Frontmatter Schema

Every note may declare:

```yaml
---
publish_to:
  production: true
  research: true
  template: false
title: "Custom Title"
description: "Short SEO description"
author: "David Lowe"
date: "2025-01-15"
tags: [quantum, consciousness]
category: research
audio_file:
  - assets/audio/sample.mp3
video_file: assets/video/session.mp4
image_gallery:
  - assets/images/fig-1.png
  - assets/images/fig-2.png
toc_depth: 3
math: true
comments: true
---
```

Notes default to `research: true` when the `publish_to` block is absent.
Audio, video, and gallery entries automatically produce styled players
and copy the referenced media into the build output.

## Pipeline Highlights

- Lantana-inspired custom theme layered on MkDocs Material with Terminal
  UI elements.
- PyMdown extensions, KaTeX/MathJax, syntax highlighting, tags, macros,
  awesome-pages, git revision metadata, and HTML/CSS minification.
- `[[wikilinks]]` are converted to Markdown links using an index of vault
  documents and attachments.
- Built-in `tags` plugin (packaged locally) generates tag indexes and exposes
  tag metadata to templates.
- Generated navigation scaffold for `Home`, `Tags`, `Research`, `AI
  Collab`, `Data`, and `Tools` sections.
- Media referenced from outside the vault is copied into the build output
  and linked automatically, preventing accidental breakage when absolute
  filesystem paths are used in frontmatter.
- Audio playlist enhancer with download controls, plus responsive video
  and image galleries.

## Testing & Deployment

Run the included build script locally; the resulting MkDocs projects are
written to `obsidian-vault/published/<site>` and are ready for `mkdocs
build` or the Cloudflare deployment pipeline.

See `docs/index.md` for full usage notes and integration guidance.
