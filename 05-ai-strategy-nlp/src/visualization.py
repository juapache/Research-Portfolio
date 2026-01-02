"""Plot helpers for AI strategy comparisons."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, Optional

import matplotlib.pyplot as plt


def plot_term_scores(
    scores: Dict[str, float],
    title: str,
    ylabel: str = "TF-IDF score",
    save_path: Optional[Path | str] = None,
    rotation: int = 45,
) -> plt.Figure:
    """Bar plot for term scores; optionally save to disk."""
    terms = list(scores.keys())
    values = list(scores.values())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(terms, values, color="#3b82f6")
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(terms, rotation=rotation, ha="right")
    fig.tight_layout()

    if save_path:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300)
    return fig


def plot_cluster_comparison(
    north_terms: Dict[str, float],
    south_terms: Dict[str, float],
    title: str = "Safety/Ethics vs Development/Access",
    save_path: Optional[Path | str] = None,
) -> plt.Figure:
    """Side-by-side bars comparing two clusters of terms."""
    fig, ax = plt.subplots(figsize=(12, 6))

    north_items = list(north_terms.items())
    south_items = list(south_terms.items())

    north_labels, north_vals = zip(*north_items) if north_items else ([], [])
    south_labels, south_vals = zip(*south_items) if south_items else ([], [])

    x_north = range(len(north_labels))
    x_south = range(len(south_labels))

    ax.bar(x_north, north_vals, color="#0ea5e9", label="Safety/Ethics")
    ax.bar(x_south, south_vals, color="#f97316", label="Development/Access")

    ax.set_xticks(list(x_north) + list(x_south))
    ax.set_xticklabels(list(north_labels) + list(south_labels), rotation=45, ha="right")
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()

    if save_path:
        path = Path(save_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=300)
    return fig


def save_figure(fig: plt.Figure, path: Path | str) -> None:
    """Save a matplotlib figure ensuring parent dir exists."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=300)
