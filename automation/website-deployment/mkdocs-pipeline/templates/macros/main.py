"""Custom macros for the Theophysics MkDocs deployments."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Mapping


def define_env(env):
    """Register macros used within the documentation set."""

    site_config = env.conf or {}
    extra: Mapping[str, Any] = site_config.get("extra", {}) if isinstance(site_config, Mapping) else {}

    def site_tagline(default: str = "") -> str:
        return extra.get("tagline") or default

    def render_timestamp(value: str | None = None, fmt: str = "%Y-%m-%d") -> str:
        if not value:
            return ""
        try:
            parsed = datetime.fromisoformat(value)
            return parsed.strftime(fmt)
        except ValueError:
            return value

    env.macro(site_tagline)
    env.macro(render_timestamp)

    env.variables.update(
        {
            "build_timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ"),
            "site_kind": extra.get("site_kind", "site"),
        }
    )
