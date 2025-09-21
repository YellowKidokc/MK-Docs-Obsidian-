#!/usr/bin/env python3
"""MkDocs pipeline for Theophysics Research Platform.

This script transforms an Obsidian vault into three themed MkDocs
projects (production, research, template).  Notes are filtered using the
``publish_to`` frontmatter flag described in the technical specification
and additional assets such as audio, video and image galleries are
materialised automatically.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import logging
import re
import shutil
import sys
import posixpath
from pathlib import Path, PurePosixPath
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

import yaml

LOGGER = logging.getLogger("mkdocs_pipeline")


PUBLISH_TARGETS = ("production", "research", "template")
DEFAULT_PUBLISH_TARGET = "research"
MARKDOWN_SUFFIXES = {".md", ".markdown"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
@dataclasses.dataclass
class Note:
    """Representation of an Obsidian markdown document."""

    source_path: Path
    relative_path: Path
    metadata: Mapping[str, object]
    body: str

    @property
    def stem(self) -> str:
        return self.source_path.stem


@dataclasses.dataclass
class SiteConfig:
    """Configuration for a single MkDocs site."""

    identifier: str
    site_name: str
    site_description: str
    site_url: str
    output_dir: Path
    palette_accent: str
    palette_primary: str
    extra: Mapping[str, object]


BASE_THEME_CONFIG: Mapping[str, object] = {
    "name": "material",
    "custom_dir": "theme/lantana-terminal",
    "language": "en",
    "palette": [
        {
            "scheme": "slate",
            "primary": "black",
            "accent": "cyan",
        }
    ],
    "features": [
        "navigation.tabs",
        "navigation.sections",
        "navigation.top",
        "search.highlight",
        "search.share",
        "toc.integrate",
    ],
}


MARKDOWN_EXTENSIONS: Sequence[object] = [
    "pymdownx.caret",
    "pymdownx.mark",
    "pymdownx.tilde",
    "pymdownx.snippets",
    "pymdownx.superfences",
    "pymdownx.highlight",
    "pymdownx.inlinehilite",
    {
        "pymdownx.blocks.details": {
            "types": [
                {
                    "name": "info",
                    "class": "terminal-alert",
                    "title": "Info",
                },
                {
                    "name": "warning",
                    "class": "terminal-alert terminal-alert-error",
                    "title": "Warning",
                },
                {
                    "name": "important",
                    "class": "terminal-alert terminal-alert-primary",
                    "title": "Important",
                },
            ]
        }
    },
    "def_list",
    "footnotes",
    "tables",
    "toc",
    "attr_list",
    "md_in_html",
    {"pymdownx.arithmatex": {"generic": True}},
]


PLUGINS: Sequence[object] = [
    'search',
    'tags',
    'awesome-pages',
    'git-revision-date',
    {'macros': {'include_dir': 'macros'}},
    {'minify': {'minify_html': True, 'minify_js': True, 'minify_css': True}},
]

NAVIGATION: Sequence[Mapping[str, object]] = [
    {"Home": "index.md"},
    {"Tags": "tags.md"},
    {"Research": "research/index.md"},
    {"AI Collab": "ai-collab/index.md"},
    {"Data": "data/index.md"},
    {"Tools": "tools/index.md"},
]

SITE_MATRIX: Mapping[str, SiteConfig] = {
    "production": SiteConfig(
        identifier="production",
        site_name="Theophysics Research Platform",
        site_description="Curated highlights from the Theophysics research archive",
        site_url="https://theophysics.pages.dev",
        output_dir=Path("production"),
        palette_accent="cyan",
        palette_primary="black",
        extra={
            "site_kind": "production",
            "tagline": "Curated publications for the Quantum-Consciousness community",
        },
    ),
    "research": SiteConfig(
        identifier="research",
        site_name="Theophysics Research Vault",
        site_description="Complete working vault for internal and collaborative studies",
        site_url="https://theophysics-template.pages.dev",
        output_dir=Path("research"),
        palette_accent="teal",
        palette_primary="black",
        extra={
            "site_kind": "research",
            "tagline": "Full-stack knowledge base for David Lowe and collaborators",
        },
    ),
    "template": SiteConfig(
        identifier="template",
        site_name="Theophysics Collaboration Lab",
        site_description="Template site showcasing AI collaboration workflows",
        site_url="https://theophysics-blog.pages.dev",
        output_dir=Path("template"),
        palette_accent="purple",
        palette_primary="black",
        extra={
            "site_kind": "template",
            "tagline": "Experimental frontier for AI-augmented research",
        },
    ),
}

EXCLUDED_DIRECTORIES = {
    "automation",
    "published",
    ".obsidian",
    "environment",
}

PAGE_FRONTMATTER_KEYS = (
    "title",
    "description",
    "author",
    "date",
    "tags",
    "category",
    "toc_depth",
    "math",
    "comments",
)

WIKILINK_PATTERN = re.compile(r"(!)?\[\[([^\]]+)\]\]")


class PipelineError(RuntimeError):
    """Domain specific error raised by the pipeline."""


@dataclasses.dataclass
class VaultIndex:
    """Index of documents and media used for wikilink resolution."""

    documents: Mapping[str, Path]
    assets: Mapping[str, Path]
    raw_documents: Mapping[str, Path]
    raw_assets: Mapping[str, Path]


@dataclasses.dataclass
class RenderContext:
    """Context for rendering a single markdown document."""

    site: SiteConfig
    vault_root: Path
    docs_dir: Path
    index: VaultIndex


def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build all MkDocs projects from the Obsidian vault")
    parser.add_argument(
        "--vault",
        type=Path,
        default=Path("obsidian-vault"),
        help="Path to the Obsidian vault root (default: obsidian-vault)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("obsidian-vault/published"),
        help="Directory where the MkDocs sites will be generated",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove previously generated files before building",
    )
    parser.add_argument(
        "--site",
        choices=PUBLISH_TARGETS,
        help="Build only the given site identifier",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    return parser.parse_args(argv)


def configure_logging(verbose: bool = False) -> None:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.DEBUG if verbose else logging.INFO)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_front_matter(text: str) -> Tuple[Mapping[str, object], str]:
    if not text.startswith("---"):
        return {}, text

    lines = text.splitlines()
    if len(lines) < 2:
        return {}, text

    closing_index: Optional[int] = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return {}, text

    frontmatter_block = "\n".join(lines[1:closing_index])
    body = "\n".join(lines[closing_index + 1 :])

    try:
        metadata = yaml.safe_load(frontmatter_block) or {}
    except yaml.YAMLError as exc:  # pragma: no cover - defensive logging
        LOGGER.warning("Failed to parse YAML front matter: %s", exc)
        metadata = {}

    if not isinstance(metadata, dict):
        LOGGER.debug("Front matter was not a mapping; ignoring")
        metadata = {}

    return metadata, body.lstrip("\n")


def normalise_component(value: str) -> str:
    slug = re.sub(r"[\s_]+", "-", value.strip().lower())
    slug = re.sub(r"[^a-z0-9\-\/]+", "", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")


def normalise_path(value: str) -> str:
    value = value.replace("\\", "/")
    parts = [normalise_component(part) for part in value.split("/") if part]
    return "/".join(part for part in parts if part)


def gather_vault(vault_root: Path) -> Tuple[List[Note], List[Tuple[Path, Path]]]:
    notes: List[Note] = []
    assets: List[Tuple[Path, Path]] = []

    for path in vault_root.rglob("*"):
        if path.is_dir():
            continue
        try:
            rel_path = path.relative_to(vault_root)
        except ValueError:
            continue
        if rel_path.parts and rel_path.parts[0] in EXCLUDED_DIRECTORIES:
            continue

        if path.suffix.lower() in MARKDOWN_SUFFIXES:
            metadata, body = parse_front_matter(read_text(path))
            notes.append(Note(path, rel_path.with_suffix(".md"), metadata, body))
        else:
            assets.append((path, rel_path))

    notes.sort(key=lambda note: note.relative_path.as_posix())
    assets.sort(key=lambda item: item[1].as_posix())
    return notes, assets


def build_index(notes: Sequence[Note], assets: Sequence[Tuple[Path, Path]]) -> VaultIndex:
    document_map: Dict[str, Path] = {}
    asset_map: Dict[str, Path] = {}
    raw_documents: Dict[str, Path] = {}
    raw_assets: Dict[str, Path] = {}

    for note in notes:
        relative_without_suffix = note.relative_path.with_suffix("")
        normalised_with_dirs = normalise_path(relative_without_suffix.as_posix())
        normalised_stem = normalise_component(note.stem)

        title = note.metadata.get("title") if isinstance(note.metadata, Mapping) else None
        if title:
            normalised_title = normalise_component(str(title))
        else:
            normalised_title = None

        for key in {normalised_with_dirs, normalised_stem, normalised_title}:

            if key and key not in document_map:
                document_map[key] = note.relative_path
                raw_documents[key] = note.relative_path

    for asset_path, rel_path in assets:
        relative_without_suffix = rel_path.with_suffix("")
        normalised_with_dirs = normalise_path(relative_without_suffix.as_posix())
        normalised_name = normalise_component(rel_path.name)
        normalised_filename = normalise_component(rel_path.stem)

        for key in {normalised_with_dirs, normalised_name, normalised_filename}:
            if key and key not in asset_map:
                asset_map[key] = rel_path
                raw_assets[key] = rel_path

    return VaultIndex(document_map, asset_map, raw_documents, raw_assets)


def as_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "on", "1"}
    return bool(value)


def determine_publish_targets(metadata: Mapping[str, object]) -> Mapping[str, bool]:
    publish_to = metadata.get("publish_to")
    results: Dict[str, bool] = {target: False for target in PUBLISH_TARGETS}

    if publish_to is None:
        results[DEFAULT_PUBLISH_TARGET] = True
        return results

    if isinstance(publish_to, Mapping):
        for key, value in publish_to.items():
            if key in results:
                results[key] = as_bool(value)
        return results

    if isinstance(publish_to, Sequence) and not isinstance(publish_to, (str, bytes)):
        for item in publish_to:
            if isinstance(item, str) and item in results:
                results[item] = True
        return results

    if as_bool(publish_to):
        results[DEFAULT_PUBLISH_TARGET] = True
        return results

    return results


def resolve_wikilink(
    target: str,
    doc_map: Mapping[str, Path],
    asset_map: Mapping[str, Path],
) -> Optional[Tuple[Path, bool]]:
    anchor = ""
    if "#" in target:
        base, _, anchor = target.partition("#")
    else:
        base = target

    base = base.strip()
    normalised_target = normalise_path(base)
    normalised_with_suffix = normalise_path(base.rstrip(".md"))

    for key in filter(None, [normalised_target, normalised_with_suffix]):
        if key in doc_map:
            path = doc_map[key]
            return (path.with_suffix(".md"), True)

    for key in filter(None, [normalised_target, normalised_with_suffix]):
        if key in asset_map:
            return (asset_map[key], False)

    return None


def format_wikilink(
    match: re.Match[str],
    context: RenderContext,
    note: Note,
) -> str:
    is_embed = bool(match.group(1))
    raw_target = match.group(2)
    alias = None
    target = raw_target
    anchor = ""

    if "|" in raw_target:
        target, alias = raw_target.split("|", 1)
    if "#" in target:
        target, _, anchor = target.partition("#")
    target = target.strip()

    resolved = resolve_wikilink(target, context.index.documents, context.index.assets)
    if not resolved:
        LOGGER.debug("Unresolved wikilink '%s' in %s", raw_target, note.relative_path)
        return match.group(0)

    relative_path, is_document = resolved
    note_dir = PurePosixPath(note.relative_path).parent
    start = note_dir.as_posix() if str(note_dir) not in {"", "."} else "."
    href = posixpath.relpath(relative_path.as_posix(), start=start)
    if href == ".":
        href = relative_path.name
    if anchor:
        href = f"{href}#{normalise_component(anchor)}"

    link_text = alias or target

    if is_embed:
        suffix = relative_path.suffix.lower()
        if suffix in IMAGE_EXTENSIONS:
            return f"![{link_text}]({href})"
        return f"[{link_text}]({href})"

    return f"[{link_text}]({href})"


def convert_wikilinks(text: str, context: RenderContext, note: Note) -> str:
    return WIKILINK_PATTERN.sub(lambda match: format_wikilink(match, context, note), text)


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def render_frontmatter(metadata: Mapping[str, object]) -> str:
    page_meta: Dict[str, object] = {}
    for key in PAGE_FRONTMATTER_KEYS:
        if key in metadata and metadata[key] is not None:
            page_meta[key] = metadata[key]

    if not page_meta:
        return ""

    dumped = yaml.safe_dump(page_meta, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{dumped}\n---\n\n"


def coerce_list(value: object) -> List[object]:
    if value is None:
        return []
    if isinstance(value, (str, Path)):
        return [value]
    if isinstance(value, Sequence):
        return list(value)
    return [value]


def mime_type_for(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".mp3":
        return "audio/mpeg"
    if suffix == ".wav":
        return "audio/wav"
    if suffix == ".m4a":
        return "audio/mp4"
    if suffix == ".ogg":
        return "audio/ogg"
    if suffix == ".mp4":
        return "video/mp4"
    if suffix == ".webm":
        return "video/webm"
    if suffix == ".mov":
        return "video/quicktime"
    if suffix == ".mkv":
        return "video/x-matroska"
    if suffix == ".m4v":
        return "video/x-m4v"
    return "application/octet-stream"


def copy_asset(vault_root: Path, docs_dir: Path, relative_path: Path) -> Path:
    destination = docs_dir / relative_path
    ensure_directory(destination.parent)
    shutil.copy2(vault_root / relative_path, destination)
    return relative_path


def render_audio_blocks(
    metadata: Mapping[str, object],
    note: Note,
    context: RenderContext,
) -> Tuple[str, List[Path]]:
    audio_value = metadata.get("audio_file")
    if not audio_value:
        return "", []

    entries: List[Dict[str, object]] = []
    for raw_item in coerce_list(audio_value):
        if isinstance(raw_item, Mapping):
            sources = [Path(str(v)) for v in coerce_list(raw_item.get("sources") or raw_item.values())]
            title = raw_item.get("title") or raw_item.get("name") or note.stem
        else:
            sources = [Path(str(raw_item))]
            title = Path(str(raw_item)).stem
        entries.append({"title": str(title), "sources": sources})

    rendered_blocks: List[str] = []
    copied_assets: List[Path] = []
    playlist_items: List[str] = []

    for index, entry in enumerate(entries, start=1):
        sources_markup: List[str] = []
        download_href: Optional[str] = None
        for source in entry["sources"]:
            resolved = resolve_media_path(source, note, context)
            if resolved is None:
                LOGGER.warning("Audio source %s not found for %s", source, note.relative_path)
                continue
            copied_assets.append(resolved)
            mime = mime_type_for(resolved)
            href = resolved.as_posix()
            sources_markup.append(f'    <source src="{href}" type="{mime}">')
            if download_href is None:
                download_href = href

        if not sources_markup:
            continue

        title = entry["title"] or f"Track {index}"
        playlist_items.append(f'<li data-track="{index}">{title}</li>')

        controls = ""
        if download_href:
            controls = (
                "<div class=\"audio-controls\">"
                f"<a class=\"audio-download\" href=\"{download_href}\" download>Download</a>"
                f"<span class=\"audio-info\">{title}</span>"
                "</div>"
            )

        block = (
            "<div class=\"audio-player\">\n"
            "  <audio controls preload=\"metadata\">\n"
            + "\n".join(sources_markup)
            + "\n    Your browser does not support the audio element.\n  </audio>\n"
            + f"  {controls}\n"
            + "</div>\n"
        )
        rendered_blocks.append(block)

    if not rendered_blocks:
        return "", copied_assets

    playlist_markup = ""
    if len(rendered_blocks) > 1:
        playlist_markup = (
            "<div class=\"audio-playlist\">\n"
            "  <h3>Playlist</h3>\n  <ol>\n"
            + "\n".join(f"    {item}" for item in playlist_items)
            + "\n  </ol>\n</div>\n"
        )

    wrapper = (
        "<section class=\"audio-player-group\">\n"
        + playlist_markup
        + "\n".join(rendered_blocks)
        + "</section>\n\n"
    )

    return wrapper, copied_assets


def resolve_media_path(path: Path, note: Note, context: RenderContext) -> Optional[Path]:
    absolute_candidate = None
    if path.is_absolute():
        absolute_candidate = path
    else:
        relative_to_note = (note.source_path.parent / path).resolve()
        if relative_to_note.exists():
            absolute_candidate = relative_to_note
        else:
            vault_candidate = (context.vault_root / path).resolve()
            if vault_candidate.exists():
                absolute_candidate = vault_candidate

    if absolute_candidate is None or not absolute_candidate.exists():
        return None

    relative_path = absolute_candidate.relative_to(context.vault_root)
    copy_asset(context.vault_root, context.docs_dir, relative_path)
    return relative_path


def render_video_block(
    metadata: Mapping[str, object],
    note: Note,
    context: RenderContext,
) -> Tuple[str, List[Path]]:
    video_value = metadata.get("video_file")
    if not video_value:
        return "", []

    rendered: List[str] = []
    copied: List[Path] = []

    for raw_path in coerce_list(video_value):
        resolved = resolve_media_path(Path(str(raw_path)), note, context)
        if resolved is None:
            LOGGER.warning("Video source %s not found for %s", raw_path, note.relative_path)
            continue
        mime = mime_type_for(resolved)
        copied.append(resolved)
        rendered.append(
            "<div class=\"video-player\">\n"
            "  <video controls preload=\"metadata\">\n"
            f"    <source src=\"{resolved.as_posix()}\" type=\"{mime}\">\n"
            "    Your browser does not support the video tag.\n  </video>\n"
            "</div>\n"
        )

    if not rendered:
        return "", copied

    return "<section class=\"video-gallery\">\n" + "\n".join(rendered) + "</section>\n\n", copied


def render_image_gallery(
    metadata: Mapping[str, object],
    note: Note,
    context: RenderContext,
) -> Tuple[str, List[Path]]:
    gallery_value = metadata.get("image_gallery")
    if not gallery_value:
        return "", []

    items: List[str] = []
    copied: List[Path] = []

    for raw_path in coerce_list(gallery_value):
        resolved = resolve_media_path(Path(str(raw_path)), note, context)
        if resolved is None:
            LOGGER.warning("Gallery image %s not found for %s", raw_path, note.relative_path)
            continue
        copied.append(resolved)
        alt_text = Path(str(raw_path)).stem.replace("-", " ").replace("_", " ")
        items.append(
            "  <figure class=\"gallery-item\">\n"
            f"    <img src=\"{resolved.as_posix()}\" alt=\"{alt_text}\">\n"
            f"    <figcaption>{alt_text.title()}</figcaption>\n  </figure>"
        )

    if not items:
        return "", copied

    return "<section class=\"image-gallery\">\n" + "\n".join(items) + "\n</section>\n\n", copied


def render_note(note: Note, context: RenderContext) -> str:
    metadata = note.metadata or {}
    frontmatter = render_frontmatter(metadata)
    wiki_converted = convert_wikilinks(note.body, context, note)

    audio_html, _ = render_audio_blocks(metadata, note, context)
    video_html, _ = render_video_block(metadata, note, context)
    gallery_html, _ = render_image_gallery(metadata, note, context)

    body_parts = [audio_html, video_html, gallery_html, wiki_converted]
    body = "".join(part for part in body_parts if part)
    return frontmatter + body


def copy_theme_assets(site_dir: Path) -> None:
    theme_source = Path(__file__).resolve().parent / "theme" / "lantana-terminal"
    destination = site_dir / "theme" / "lantana-terminal"
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(theme_source, destination)


def copy_static_assets(site_dir: Path) -> None:
    assets_source = Path(__file__).resolve().parent / "assets"
    docs_dir = site_dir / "docs"
    ensure_directory(docs_dir)

    for asset in assets_source.rglob("*"):
        if asset.is_dir():
            continue
        relative = asset.relative_to(assets_source)
        destination = docs_dir / relative
        ensure_directory(destination.parent)
        shutil.copy2(asset, destination)


def write_site_metadata_script(site_dir: Path, site: SiteConfig) -> None:
    docs_dir = site_dir / "docs"
    js_dir = docs_dir / "javascripts"
    ensure_directory(js_dir)
    if isinstance(site.extra, Mapping):
        site_kind = site.extra.get('site_kind', site.identifier)
        tagline = site.extra.get('tagline', site.site_description)
    else:
        site_kind = site.identifier
        tagline = site.site_description
    script = (
        "(function(){\n"
        "  document.addEventListener('DOMContentLoaded', function () {\n"
        "    var body = document.body;\n"
        f"    body.setAttribute('data-site-kind', {json.dumps(site_kind)});\n"
        f"    body.setAttribute('data-site-tagline', {json.dumps(tagline)});\n"
        "  });\n"
        "})();\n"
    )
    (js_dir / 'site-meta.js').write_text(script, encoding='utf-8')


def copy_macros(site_dir: Path) -> None:
    macros_source = Path(__file__).resolve().parent / "templates" / "macros"
    macros_destination = site_dir / "macros"
    if macros_destination.exists():
        shutil.rmtree(macros_destination)
    shutil.copytree(macros_source, macros_destination)


def ensure_navigation_scaffolding(site_dir: Path) -> None:
    docs_dir = site_dir / "docs"
    placeholders = {
        Path("research/index.md"): "# Research Library\n\nCurated research collections appear here.",
        Path("ai-collab/index.md"): "# AI Collaboration\n\nDocument experiments and AI-assisted workflows.",
        Path("data/index.md"): "# Data Archives\n\nDatasets and analysis artefacts live in this section.",
        Path("tools/index.md"): "# Tools\n\nScripts, automations, and helpers for research teams.",
        Path("tags.md"): "# Tags\n\n{% raw %}{{ tags }}{% endraw %}",
    }

    for relative_path, contents in placeholders.items():
        destination = docs_dir / relative_path
        if destination.exists():
            continue
        ensure_directory(destination.parent)
        destination.write_text(contents + "\n", encoding="utf-8")

    index_path = docs_dir / "index.md"
    if not index_path.exists():
        index_contents = (
            "# Welcome to the Theophysics Research Platform\n\n"
            "This site was generated automatically from the Obsidian vault. "
            "Replace this file with your own introduction by adding an `index.md` "
            "note to the vault root.\n"
        )
        index_path.write_text(index_contents, encoding="utf-8")


def build_mkdocs_config(site: SiteConfig) -> Mapping[str, object]:
    palette = [{"scheme": "slate", "primary": site.palette_primary, "accent": site.palette_accent}]
    theme_config = dict(BASE_THEME_CONFIG)
    theme_config["palette"] = palette

    config: Dict[str, object] = {
        "site_name": site.site_name,
        "site_description": site.site_description,
        "site_author": "David Lowe",
        "site_url": site.site_url,
        "theme": theme_config,
        "markdown_extensions": MARKDOWN_EXTENSIONS,
        "plugins": list(PLUGINS),
        "nav": list(NAVIGATION),
        "extra": dict(site.extra),
        "extra_css": [
            "stylesheets/custom.css",
            "stylesheets/audio-player.css",
            "stylesheets/terminal-overrides.css",
        ],
        "extra_javascript": [
            "javascripts/site-meta.js",
            "javascripts/mathjax.js",
            "javascripts/audio-controls.js",
            "javascripts/terminal-effects.js",
        ],
    }

    return config


def write_mkdocs_config(site_dir: Path, config: Mapping[str, object]) -> None:
    mkdocs_yml = site_dir / "mkdocs.yml"
    with mkdocs_yml.open("w", encoding="utf-8") as stream:
        yaml.safe_dump(config, stream, sort_keys=False, allow_unicode=True)


def write_note(note: Note, site_dir: Path, context: RenderContext) -> None:
    docs_dir = site_dir / "docs"
    destination = docs_dir / note.relative_path
    ensure_directory(destination.parent)
    rendered = render_note(note, context)
    destination.write_text(rendered, encoding="utf-8")


def copy_remaining_assets(site_dir: Path, assets: Sequence[Tuple[Path, Path]]) -> None:
    docs_dir = site_dir / "docs"
    for source, relative in assets:
        destination = docs_dir / relative
        ensure_directory(destination.parent)
        shutil.copy2(source, destination)


def build_site(
    site: SiteConfig,
    vault_root: Path,
    output_root: Path,
    notes: Sequence[Note],
    assets: Sequence[Tuple[Path, Path]],
    index: VaultIndex,
) -> None:
    site_dir = output_root / site.output_dir
    LOGGER.info("Building site '%s' in %s", site.identifier, site_dir)
    ensure_directory(site_dir)
    docs_dir = site_dir / "docs"
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    ensure_directory(docs_dir)

    copy_theme_assets(site_dir)
    copy_static_assets(site_dir)
    write_site_metadata_script(site_dir, site)
    copy_macros(site_dir)

    context = RenderContext(site, vault_root, docs_dir, index)

    for note in notes:
        publish_flags = determine_publish_targets(note.metadata)
        if not publish_flags.get(site.identifier, False):
            continue
        write_note(note, site_dir, context)

    copy_remaining_assets(site_dir, assets)
    ensure_navigation_scaffolding(site_dir)
    mkdocs_config = build_mkdocs_config(site)
    write_mkdocs_config(site_dir, mkdocs_config)


def clean_output(output_root: Path, site: Optional[str]) -> None:
    targets = [SITE_MATRIX[site]] if site else SITE_MATRIX.values()
    for config in targets:
        site_dir = output_root / config.output_dir
        if site_dir.exists():
            LOGGER.info("Cleaning %s", site_dir)
            shutil.rmtree(site_dir)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_arguments(argv)
    configure_logging(args.verbose)

    vault_root = args.vault.resolve()
    output_root = args.output.resolve()

    if not vault_root.exists():
        raise PipelineError(f"Vault path {vault_root} does not exist")

    ensure_directory(output_root)

    if args.clean:
        clean_output(output_root, args.site)

    notes, assets = gather_vault(vault_root)
    if not notes:
        LOGGER.warning("No markdown notes found in %s", vault_root)

    index = build_index(notes, assets)

    targets = [SITE_MATRIX[args.site]] if args.site else SITE_MATRIX.values()

    for site in targets:
        build_site(site, vault_root, output_root, notes, assets, index)

    LOGGER.info("MkDocs build configuration generated successfully")
    LOGGER.info("Output available in %s", output_root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
