<p align="center">
  <img src="ec2dda7b-901c-4e12-b2f3-abba9c41d3ef.png" alt="MyGenome Logo" width="300"/>
</p>

<h1 align="center">Variant Effect Prediction using AI</h1>
<p align="center">
  <b>Aina Rif’ah — Bioinformatics Internship (Oct 2025 – Aug 2026)</b><br>
  <i>In collaboration with MyGenome — Ethical Life Science</i>
</p>

---

## 🧬 Project Goal

Develop and evaluate a machine learning model that predicts whether a genetic variant is **benign** or **pathogenic** using publicly available datasets such as **ClinVar**, **dbSNP**, and **gnomAD**.

---

## 📚 Table of Contents

* [Project Overview](#project-overview)
* [Week 1 — Summary (Completed)](#week-1---summary-completed)
* [Data & Files](#data--files)
* [How to Run (Local)](#how-to-run-local)
* [Next Steps (Week 2)](#next-steps-week-2)
* [Contact](#contact)

---

## 🧠 Project Overview

This repository documents the end-to-end process of building an AI model for **variant effect prediction**.
The project combines **bioinformatics** (variant interpretation, data curation) and **machine learning** (feature extraction, model training).
Focus areas include:

* Reproducible data handling
* Feature engineering (functional consequence, allele frequency, conservation)
* Baseline ML models (Random Forest / XGBoost)

---

## 🧩 Week 1 — Summary (Completed)

### 🎯 Objective

Train a machine learning model (e.g., Random Forest, XGBoost, or Deep Learning) to classify genetic variants (e.g., missense, nonsense) as **benign** or **pathogenic** using public datasets.

### 📘 What I Completed

* Installed **Miniconda** and created a Python environment `varpred`.
* Installed and launched **JupyterLab**.
* Created the notebook `01_literature_review.ipynb`.
* Wrote a comprehensive **literature review** covering:

  * Central Dogma (DNA → RNA → Protein)
  * Variant Types (SNVs, INDELs, synonymous, missense, nonsense, frameshift, in-frame)
  * Structural Variants (CNVs, inversions, translocations)
  * Variant Databases: **ClinVar**, **dbSNP**, **gnomAD**, **OMIM**
* Initialized a local **Git repository** and structured project folders.

### 📁 Deliverables

* `notebooks/01_literature_review.ipynb` — Markdown & setup notes
* `docs/chapter1_literature.md` — literature summary
* `README.md` — this documentation file

---

## 📂 Data & Files

| Folder                           | Description                                                 |
| -------------------------------- | ----------------------------------------------------------- |
| `data/`                          | Raw downloads (not uploaded to GitHub; add to `.gitignore`) |
| `notebooks/`                     | Jupyter notebooks (analysis + notes)                        |
| `docs/`                          | Documentation files (literature, reports, methods)          |

> ⚠️ **Note:** Keep large files (ClinVar, dbSNP, gnomAD) only in your local `data/` folder.

---

## 💻 How to Run (Local)

**1. Create Environment**

```bash
conda create -n varpred python=3.10 -y
conda activate varpred
pip install pandas biopython jupyterlab scikit-learn matplotlib
```

**2. Start JupyterLab**

```bash
jupyter lab
```

**3. Open Notebook**
Launch `notebooks/01_literature_review.ipynb` and explore Markdown + code cells.

---

## 🚀 Next Steps (Week 2)

* Learn **variant annotation** (Ensembl VEP) and functional consequence.
* Clean **ClinVar data** and create binary labels for benign/pathogenic.
* Integrate **gnomAD** allele frequency + dbSNP rsIDs.
* Train and evaluate a baseline **Random Forest model**.

---

## 📞 Contact

**Aina Rif’ah**
Bioinformatics Intern
📧 [aina.rifah13@gmail.com](mailto:aina.rifah13@gmail.com)

---

<p align="center">
  <i>Generated and maintained as part of the MyGenome Bioinformatics Internship — Week 1</i>
</p>


