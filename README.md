# Variant Effect Prediction using AI

**Aina Rif’ah — Bioinformatics Internship (Oct 2025 - Aug 2026)**

**Project goal:**
Develop and evaluate a machine learning model that predicts whether a genetic variant is **benign** or **pathogenic** using publicly available datasets (ClinVar, dbSNP, gnomAD).

---

## Table of Contents

* [Project Overview](#project-overview)
* [Week 1 — Summary (Completed)](#week-1---summary-completed)
* [Data & Files](#data--files)
* [How to run (local)](#how-to-run-local)
* [Next steps (Week 2)](#next-steps-week-2)
* [Contact](#contact)

---

## Project Overview

This repository contains notes, notebooks, and starter data for a project that explores AI-based classification of genetic variant pathogenicity. The focus is on reproducible data handling, careful feature engineering (annotation, allele frequency, conservation), and baseline ML models (Random Forest / XGBoost).

---

## Week 1 — Summary (Completed)

**Objective:** Train a machine learning model (e.g., Random Forest, XGBoost, or deep learning) to classify genetic variants (e.g., missense, nonsense) as benign or pathogenic using public datasets (ClinVar, dbSNP, gnomAD).

**What I completed:**

* Installed Miniconda and created a Python environment `varpred`.
* Installed and launched **JupyterLab**; created `01_literature_review.ipynb`.
* Wrote a literature review covering:

  * Central dogma (DNA → RNA → Protein)
  * Variant types (SNVs, indels, synonymous, missense, nonsense, frameshift, in-frame)
  * Structural variants and CNVs
  * Variant resources: **ClinVar**, **dbSNP**, **gnomAD**, **OMIM**
* Initialized a local Git repository and prepared files for upload.

**Deliverables:**

* `notebooks/01_literature_review.ipynb` (Markdown + small environment check)
* `docs/chapter1_literature.md` (same content, plain Markdown)
* `README.md` (this file)

---

## Data & Files

* `data/` — place raw downloads here (large files; do not commit large raw files to GitHub)
* `data/clinvar_labeled_small.csv` — *example small dataset* for quick experiments (generate from `variant_summary.txt`)
* `notebooks/` — Jupyter notebooks (analysis + notes)
* `docs/` — readable Markdown documentation (literature, methods, project notes)

> **Note:** Raw ClinVar/gnomAD/dbSNP files are large; keep them locally under `data/` and add `data/` to `.gitignore` if pushing to GitHub.

---

## How to run (local)

1. Create environment:

```bash
conda create -n varpred python=3.10 -y
conda activate varpred
pip install pandas biopython jupyterlab scikit-learn matplotlib
```

2. Start JupyterLab:

```bash
jupyter lab
```

3. Open `notebooks/01_literature_review.ipynb` and browse the Markdown cells.

---

## Next steps (Week 2)

* Learn variant annotation (VEP / Ensembl) and functional consequence fields.
* Clean ClinVar data (map clinical significance → binary labels).
* Add gnomAD allele frequency and dbSNP rsIDs as features.
* Train a baseline Random Forest model and evaluate.

---

## Contact

**Aina Rif’ah** — Bioinformatics Intern
Email: aina.rifah13@gmail.com

---

*(Generated and maintained as part of my internship project — Week 1)*

