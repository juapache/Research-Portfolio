# Data Layout
- raw/: source PDFs; keep immutable and record provenance (country, source, date).
- processed/: cleaned text outputs (regex cleanup + spaCy lemmatization) ready for TF-IDF.
- external/: metadata such as region mappings (Global North/South) or document catalogues.
