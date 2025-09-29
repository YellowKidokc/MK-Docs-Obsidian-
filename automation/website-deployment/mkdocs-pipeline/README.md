# Theophysics MkDocs Pipeline Package

This package exposes the custom `tags` plugin used by the multi-site
MkDocs deployment as well as helper utilities that are bundled with the
repository.  Install it locally via:

```bash
pip install -e automation/website-deployment/mkdocs-pipeline
```

The plugin is registered under the `mkdocs.plugins` entry point so it can
be referenced simply as `tags` within `mkdocs.yml`.
