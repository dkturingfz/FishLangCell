"""AnnData loading placeholders for future preprocessing pipelines."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def read_anndata_placeholder(path: str | Path) -> Any:
    """Validate path and attempt to load an AnnData object when dependency is installed.

    TODO: Expand to support backed mode, mtx directories, and schema checks.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"AnnData path not found: {file_path}")

    try:
        import anndata as ad  # type: ignore
    except ImportError as exc:  # pragma: no cover - optional dependency path
        raise RuntimeError(
            "anndata is not installed. Install optional data dependencies before reading .h5ad files."
        ) from exc

    return ad.read_h5ad(file_path)
