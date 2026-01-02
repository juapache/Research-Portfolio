# Decoding the Divide: Computational Analysis of Global North vs. South AI Strategies

## Executive Summary
This project applies Natural Language Processing (NLP) to analyze National AI Strategies from the OECD Policy Observatory. It investigates the divergence in normative priorities between the Global North and Global South. While dominant narratives focus on AI safety and ethics, this analysis reveals a distinct prioritization of economic development and infrastructure access in emerging economies.

## Hypothesis
**The "Safety" vs. "Development" Divide**
* **Theory:** International Human Rights Law often frames AI risks as civil liberty violations (privacy, bias). However, the "Right to Development" suggests that for emerging economies, the primary risk is exclusion from the economic benefits of AI.
* **Hypothesis:** Global North strategies will exhibit statistically higher frequencies of "Safety/Ethics" terms, while Global South strategies will prioritize "Development/Access" terms.

## Methodology
To operationalize the legal distinction between "Safety" and "Development," this project treats legal texts as unstructured data. The pipeline follows three stages:

1.  **Data Curation & Cleaning (ETL):**
    * **Source:** National AI Strategies extracted from the OECD AI Policy Observatory.
    * **Preprocessing:** Custom Python scripts (`re`) remove PDF artifacts (headers, footers, page numbers). Text is normalized using `spaCy` to perform lemmatization (e.g., reducing "regulating" -> "regulate") and stopword removal, ensuring the analysis focuses on substantive legal concepts rather than syntax.

2.  **Feature Extraction:**
    * **TF-IDF (Term Frequency-Inverse Document Frequency):** Used to identify keywords that are statistically unique to specific regions (Global North vs. South), filtering out generic policy terms common to all documents.

3.  **Visual Analysis:**
    * Results are visualized using `matplotlib` to compare the relative frequency of normative clusters ("Rights/Safety" vs. "Infrastructure/Access").

## Directory Structure
The repository is organized to separate raw legal texts from the analysis pipeline, ensuring reproducibility.

├── data/
│   ├── raw/                   # Original PDFs (e.g., "US_National_AI_Strategy.pdf")
│   ├── processed/             # Cleaned text files ready for NLP
│   └── external/              # Metadata (Region mapping: Global North/South)
│
├── notebooks/
│   ├── 01_data_extraction.ipynb   # PDF -> Text conversion
│   ├── 02_nlp_analysis.ipynb      # Hybrid Theory+Code analysis
│   └── 03_visualization.ipynb     # Policy brief figure generation
│
├── src/
│   ├── text_processing.py     # Custom cleaning and tokenization functions
│   └── visualization.py       # Plotting helpers
│
├── results/                   # Final charts and Policy Brief summary
├── requirements.txt           # Python dependencies (spaCy, scikit-learn, etc.)
└── README.md