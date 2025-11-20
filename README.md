<h1 align="center">🧬 Variant Effect Prediction using AI</h1>

<p align="center">
  <b>Aina Rif’ah — Bioinformatics Internship (Oct 2025 – Aug 2026)</b><br>
  <i>MyGenome — Ethical Life Science</i>
</p>

---

## 🎯 Project Goal

Build an end-to-end machine learning pipeline to predict whether a human genetic variant is **benign** or **pathogenic**, using engineered biological features derived from public datasets such as **ClinVar**.

This project integrates **bioinformatics preprocessing**, **feature engineering**, **machine learning**, **model explainability (SHAP)**, and a functional **Streamlit prototype** for variant interpretation.

---

## ✅ Key Outcomes

### ✔️ Final Models (saved in `/results/`)
- `logisticregression.pkl`
- `randomforest.pkl`
- `xgboost.pkl`
- `scaler.pkl`
- `imputer.pkl`

### ✔️ Final Dataset  
`clinvar_features_engineered.csv`  
Contains ~800k ClinVar variants with engineered biological features:
- BLOSUM62 substitution scores  
- Hydropathy differences  
- Stop-gain indicator  
- Grantham distance  
- Allele frequency & log(AF)  
- Cleaned ClinVar labels  

### ✔️ Evaluation Summary
- **Random Forest AUC:** ~0.70  
- **XGBoost AUC:** ~0.72  
- **Logistic Regression AUC:** lower baseline  
- Full evaluation includes:
  - Confusion matrices  
  - ROC curves  
  - Precision–Recall curves  
  - Feature importance  
  - SHAP explanations  

### ✔️ Streamlit App Prototype  
Interactive interface allowing:
- Input of genomic coordinates (chr, pos, REF, ALT)
- Optional manual override of biological features
- XGBoost prediction output with probability
- SHAP explanations for Random Forest and Logistic Regression  

---

# 🔬 Pipeline Overview
Raw → Clean → Feature Engineering → ML Training → Evaluation → SHAP → Streamlit App

---

## 🧪 1. Data Acquisition

Source: **ClinVar variant_summary.txt.gz**

Processed with:
- GRCh38 filtering  
- Extraction of REF/ALT, protein change  
- Benign/pathogenic label mapping  
- Result: ~812,000 SNVs retained  

---

## 🧹 2. Data Cleaning & Label Normalization

Steps included:
- Removal of conflicting / uncertain labels  
- Normalization → `label_numeric` (0 = benign, 1 = pathogenic)  
- Extraction of amino acid changes  
- Parsing allele frequency fields  

---

## 🧬 3. Feature Engineering

Generated the following ML features:

| Feature | Description |
|--------|-------------|
| `blosum62_raw` | BLOSUM62 score (ref_aa → alt_aa) |
| `hydropathy_diff` | Kyte-Doolittle difference |
| `is_stop` | Stop-gain indicator |
| `grantham` | Chemical distance between amino acids |
| `allele_freq` | Derived AF |
| `af_filled` | Imputed AF |
| `log_af` | log10(AF + 1e-12) |

Saved as: clinvar_features_engineered.csv


---

## 🤖 4. Machine Learning Models

Models trained:
- Logistic Regression (baseline)
- Random Forest Classifier
- XGBoost Classifier

### Input features
["blosum62_raw",
"hydropathy_diff",
"is_stop",
"grantham",
"af_filled",
"log_af"]

Generated:
- ROC–AUC curves  
- Precision–Recall curves  
- Confusion matrices  
- Feature importance (RF + XGB)  
- SHAP beeswarm, bar, and dependence plots (RF + LR)

---

## 📊 5. SHAP Explainability

SHAP used for Random Forest & Logistic Regression:
- Beeswarm plot  
- Mean |SHAP| importance  
- Dependence plots for:
  - blosum62_raw
  - hydropathy_diff
  - is_stop
  - grantham
  - af_filled
  - log_af

⚠️ Note: XGBoost model uses a base_score string `"[5E-1]"` causing TreeExplainer failure. SHAP is disabled for XGB in the Streamlit app.

---

## 🖥️ 6. Streamlit App Prototype

`app.py` allows users to:

- Input variant coordinates  
- Optionally input biological features  
- See:
  - Model prediction  
  - Probability  
  - SHAP explanations  
  - Feature importance fallback for XGBoost  

Structure:
Variant Input → Feature Override (optional) → Model Prediction → SHAP/Importance

---

# 📁 Repository Structure
variant-effect-prediction/
│
├── data/
│ ├── raw/
│ │ └── variant_summary.txt.gz
│ └── processed/
│ └── clinvar_features_engineered.csv
│
├── results/
│ ├── logisticregression.pkl
│ ├── randomforest.pkl
│ ├── xgboost.pkl
│ ├── scaler.pkl
│ ├── imputer.pkl
│ └── shap_outputs/
│
├── notebooks/
│ ├── 01_data_cleaning.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_ml_training.ipynb
│ └── 04_shap_analysis.ipynb
│
├── app.py
└── README.md

---

<p align="center">
  <i>Developed during the MyGenome Bioinformatics Internship.</i><br>
  <b>Supervised Machine Learning • Variant Interpretation • Bioinformatics</b>
</p>
