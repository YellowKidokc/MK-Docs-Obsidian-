"""Custom MkDocs plugin for generating tag indexes."""
from __future__ import annotations

import posixpath
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Dict, Iterable, List, Mapping

import yaml
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


def _parse_front_matter(path: Path) -> Mapping[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    if len(lines) < 2:
        return {}
    closing_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        return {}
    block = "\n".join(lines[1:closing_index])
    try:
        metadata = yaml.safe_load(block) or {}
    except yaml.YAMLError:
        return {}
    return metadata if isinstance(metadata, Mapping) else {}


def _as_list(value: object) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Iterable):
        return [str(item) for item in value]
    return [str(value)]


def _page_title(metadata: Mapping[str, object], fallback: str) -> str:
    title = metadata.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    return fallback


def _relative_path(path: Path, root: Path) -> PurePosixPath:
    return PurePosixPath(path.relative_to(root).as_posix())


def _relpath(target: PurePosixPath, origin: PurePosixPath) -> str:
    start = origin.as_posix() if origin.as_posix() not in {"", "."} else "."
    return posixpath.relpath(target.as_posix(), start=start)


class TagsPlugin(BasePlugin):
    """Lightweight tag index generator."""

    config_scheme = (
        ("tags_page", config_options.Type(str, default="tags.md")),
        ("title", config_options.Type(str, default="Tags")),
    )

    def on_config(self, config):
        docs_dir = Path(config["docs_dir"]).resolve()
        tag_map: Dict[str, List[Dict[str, object]]] = defaultdict(list)
        for path in docs_dir.rglob("*.md"):
            metadata = _parse_front_matter(path)
            tags = _as_list(metadata.get("tags"))
            if not tags:
                continue
            relative = _relative_path(path, docs_dir)
            title = _page_title(metadata, relative.stem.replace("-", " ").title())
            entry = {"title": title, "relative": relative}
            for tag in tags:
                name = str(tag).strip()
                if name:
                    tag_map[name].append(entry)

        for entries in tag_map.values():
            entries.sort(key=lambda item: item["title"].lower())

        self._tag_index = dict(sorted(tag_map.items(), key=lambda item: item[0].lower()))
        config["extra"].setdefault("tag_index", self._tag_index)
        return config

    def on_page_markdown(self, markdown, page, config, files):
        if page.file.src_path != self.config["tags_page"]:
            return markdown

        source = PurePosixPath(page.file.src_path)
        lines = [f"# {self.config['title']}"]
        if not self._tag_index:
            lines.append("No tags available yet. Add `tags` to your note frontmatter.")
            return "\n\n".join(lines) + "\n"

        for tag, entries in self._tag_index.items():
            lines.append(f"## {tag}")
            for entry in entries:
                href = _relpath(entry["relative"], source.parent)
                lines.append(f"- [{entry['title']}]({href})")
            lines.append("")

        return "\n".join(lines).rstrip() + "\n"
