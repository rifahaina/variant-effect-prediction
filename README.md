<p align="center">

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
# 🧬 Variant Effect Prediction using AI  
**Internship Project — 8 Weeks**  
*Predicting whether genetic variants are benign or pathogenic using public genomic datasets.*

---

## 🎯 Project Overview  
This project develops and evaluates a machine learning model to classify genetic variants (e.g., missense, nonsense, synonymous) as **benign** or **pathogenic**.  
Public datasets such as **ClinVar**, **dbSNP**, and **gnomAD** were used for training and testing.

### **Goal**
To build an interpretable and reproducible AI pipeline for variant effect prediction using biological and computational features.

### **Outcome**
- ✅ Trained baseline ML model (Random Forest & Logistic Regression)  
- ✅ Processed dataset (`clinvar_ml_ready.csv`) with 20,000 labeled variants  
- ✅ Prototype pipeline ready for advanced modeling and visualization dashboard  

---

## 🧠 Methodology

| Stage | Description | Output |
|--------|--------------|---------|
| **Week 1 – Setup & Background** | Environment setup, bioinformatics fundamentals, dataset familiarization. | Jupyter notebooks initialized. |
| **Week 2 – Data Cleaning** | Parsed ClinVar file, extracted 812k variants → 20k balanced subset (benign vs pathogenic). | `clinvar_subset_20000.csv` |
| **Week 3 – Feature Engineering** | Extracted biological features: BLOSUM62 substitution scores, hydropathy differences, stop-codon flags, and allele frequencies. | `clinvar_features_stage2_full.csv` |
| **Week 4 – Baseline ML** | Trained Random Forest & Logistic Regression on standardized data. Evaluated model metrics. | AUC ≈ 0.72 |
| **Next Steps (Week 5–8)** | Add advanced models (XGBoost, LightGBM, Neural Nets), integrate external scores, and deploy Streamlit app. | Under development |

---

## ⚙️ Pipeline Overview

```text
data/
│
├── raw/
│   └── variant_summary.txt.gz          ← Original ClinVar data
│
├── processed/
│   ├── clinvar_subset_20000.csv        ← Clean subset (benign/pathogenic)
│   ├── clinvar_features_stage2_full.csv← Feature-engineered dataset
│   └── clinvar_ml_ready.csv            ← Final ML-ready data
│
└── notebooks/
    ├── week2_prepare_subset.ipynb
    ├── week3_feature_engineering.ipynb
    └── week4_ml_baseline.ipynb


---

<p align="center">
  <i>Generated and maintained as part of the MyGenome Bioinformatics Internship — Week 1</i>
</p>


