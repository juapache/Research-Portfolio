"""Text cleaning helpers for AI strategy NLP pipeline.

Keep functions deterministic and pure so notebooks stay orchestration-only.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Optional, Sequence

import pdfplumber

try:
    import spacy
    from spacy.language import Language
except ImportError:  # spaCy is optional until installed
    spacy = None
    Language = None


def load_pdf_text(pdf_path: Path | str) -> str:
    """Extract text from a PDF using pdfplumber; returns a single string."""
    path = Path(pdf_path)
    with pdfplumber.open(path) as pdf:
        pages = [page.extract_text() or "" for page in pdf.pages]
    return "\n".join(pages)


def strip_artifacts(text: str, patterns: Optional[Sequence[str]] = None) -> str:
    """Remove common PDF artifacts like page numbers or repeated headers."""
    patterns = patterns or [r"\n\s*\d+\s*\n"]
    cleaned = text
    for pat in patterns:
        cleaned = re.sub(pat, "\n", cleaned)
    return cleaned


def normalize_whitespace(text: str) -> str:
    """Collapse multiple spaces/newlines and trim."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _ensure_nlp(model: str | None = None) -> Language:
    if spacy is None:
        raise ImportError("spaCy is required for lemmatization; install it first.")
    return spacy.load(model or "en_core_web_sm", disable=["ner", "parser"])


def lemmatize_tokens(
    text: str,
    stopwords: Optional[Iterable[str]] = None,
    model: str | None = None,
) -> List[str]:
    """Lemmatize and lowercase tokens, dropping stopwords and non-alpha tokens."""
    nlp = _ensure_nlp(model)
    doc = nlp(text)
    stop = set(stopwords or nlp.Defaults.stop_words)
    return [t.lemma_.lower() for t in doc if t.is_alpha and t.lemma_.lower() not in stop]


def write_text(text: str, out_path: Path | str) -> None:
    """Write text to disk, creating parent directories if needed."""
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def pipeline_clean_and_save(
    pdf_path: Path | str,
    out_path: Path | str,
    artifact_patterns: Optional[Sequence[str]] = None,
    model: str | None = None,
) -> Path:
    """Full PDF -> cleaned text -> save path; returns the output path."""
    raw = load_pdf_text(pdf_path)
    stripped = strip_artifacts(raw, artifact_patterns)
    normalized = normalize_whitespace(stripped)
    tokens = lemmatize_tokens(normalized, model=model)
    cleaned_text = " ".join(tokens)
    write_text(cleaned_text, out_path)
    return Path(out_path)
