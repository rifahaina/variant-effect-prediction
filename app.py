# app.py
# AI VARIANT PREDICTOR — Streamlit prototype (Grantham added)
import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
import os

sns.set(style="whitegrid")

# ---------------- Config ----------------
st.set_page_config(page_title="AI VARIANT PREDICTOR", layout="wide")
MODEL_POSIX = Path("/mnt/c/Users/MYG-D02/variant-effect-prediction/results/xgboost.pkl")
MODEL_WIN   = Path(r"C:\Users\MYG-D02\variant-effect-prediction\results\xgboost.pkl")
# uploaded CSV path (local)
CSV_UPLOADED = Path("/mnt/data/clinvar_features_engineered.csv")
CSV_POSIX   = Path("/mnt/c/Users/MYG-D02/variant-effect-prediction/data/processed/clinvar_features_engineered.csv")

# pick whichever exists for the runtime environment
if MODEL_POSIX.exists():
    MODEL_PATH = MODEL_POSIX
else:
    MODEL_PATH = MODEL_WIN

CSV_PATH = CSV_POSIX if CSV_POSIX.exists() else CSV_UPLOADED

# FEATURES now includes grantham
FEATURES = ["blosum62_raw","hydropathy_diff","is_stop","grantham","af_filled","log_af"]

# ---------------- Styling ----------------
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{max-width:1400px; padding-left:2rem; padding-right:2rem;}
    .result-card { background: linear-gradient(90deg, rgba(39,40,34,1), rgba(27,28,26,1)); border-radius:10px; padding:14px; color:#fff; }
    .big-prob { font-size:34px; font-weight:700; margin:0; }
    .small-label { font-size:13px; color:#d3dbe6; margin:0; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Helpers ----------------
@st.cache_resource
def load_model(path):
    p = Path(path)
    if not p.exists():
        return None
    try:
        return joblib.load(p)
    except Exception:
        return None

@st.cache_data
def load_feature_csv(path, nrows=200000):
    p = Path(path)
    if not p.exists():
        return None
    return pd.read_csv(p, nrows=nrows)

def prepare_features_from_lookup(row):
    X = {}
    for f in FEATURES:
        if f in row and pd.notna(row[f]):
            X[f] = float(row[f])
    # ensure default presence
    for f in FEATURES:
        X.setdefault(f, 0.0)
    return X

def compute_prediction(model, X_df):
    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba(X_df)[:,1][0])
    else:
        pred = model.predict(X_df)[0]
        prob = float(pred)
    label = "pathogenic" if prob >= 0.5 else "benign"
    return label, prob

def plot_gauge(prob, label):
    fig, ax = plt.subplots(figsize=(8,1), dpi=120)
    color = "#e63946" if label=="pathogenic" else "#2ca25f"
    ax.barh([0], [prob], color=color)
    ax.set_xlim(0,1)
    ax.set_yticks([])
    ax.set_xticks([0,0.25,0.5,0.75,1.0])
    ax.set_xlabel("Predicted probability (pathogenic)")
    sns.despine(left=True, bottom=True)
    st.pyplot(fig)
    plt.close(fig)

def plot_shap_bar_from_values(feature_names, shap_values):
    mean_abs = np.mean(np.abs(shap_values), axis=0)
    imp_df = pd.DataFrame({"feature": feature_names, "mean_abs_shap": mean_abs})
    imp_df = imp_df.sort_values("mean_abs_shap", ascending=True)
    fig, ax = plt.subplots(figsize=(7, max(2, 0.25*len(imp_df))), dpi=120)
    sns.barplot(x="mean_abs_shap", y="feature", data=imp_df, ax=ax, palette="viridis")
    ax.set_xlabel("mean(|SHAP|)")
    ax.set_title("Feature contributions (local)")
    for i, v in enumerate(imp_df["mean_abs_shap"].values):
        ax.text(v + imp_df["mean_abs_shap"].max()*0.01, i, f"{v:.4f}", va="center", fontsize=9)
    st.pyplot(fig)
    plt.close(fig)

# ---------------- Load resources ----------------
model = load_model(MODEL_PATH)
feature_df = load_feature_csv(CSV_PATH)

# ---------------- Page ----------------
st.title("🔬 AI VARIANT PREDICTOR")
st.markdown("Prototype decision-support for variant annotation — *for research use only.*")
st.write("Enter variant coordinates (chr, position, REF, ALT). Manual features are beside inputs.")
st.markdown("---")

# top area: inputs (left) and manual features (right)
col_input, col_manual = st.columns([1, 1])

with col_input:
    st.subheader("Variant coordinates")
    chr_in = st.text_input("Chromosome", value="1", key="chr_in_input")
    pos_in = st.text_input("Position", value="100000", key="pos_in_input")
    ref_in = st.text_input("Reference (REF)", value="A", key="ref_in_input")
    alt_in = st.text_input("Alternate (ALT)", value="G", key="alt_in_input")
    st.write("")  # spacing
    run = st.button("Run prediction")

with col_manual:
    st.subheader("Manual features (optional)")
    blosum_val = st.number_input("BLOSUM62 raw", value=-1.0, format="%.2f", key="blosum_input")
    hydro_val  = st.number_input("Hydropathy diff", value=0.0, format="%.3f", key="hydro_input")
    is_stop_val = st.selectbox("Is stop?", (0,1), index=0, key="isstop_input")
    grantham_val = st.number_input("Grantham distance", value=50.0, format="%.0f", key="grantham_input")
    af_val = st.number_input("Allele frequency (AF)", value=0.0, format="%.6f", key="af_input")
    # caption removed per request (no helper text)

# bottom: result area (full width)
st.markdown("---")
st.subheader("Result")

if not run:
    st.info("Populate variant (and optional manual features) then press **Run prediction**.")
else:
    # attempt to lookup in CSV sample
    lookup = None
    if feature_df is not None and all(c in feature_df.columns for c in ["chr","pos","ref","alt"]):
        try:
            chrom_q = str(chr_in).replace("chr","").strip()
            pos_q = int(str(pos_in).replace(",","").strip())
            matched = feature_df[
                (feature_df["chr"].astype(str).str.replace("chr","").str.strip()==chrom_q) &
                (pd.to_numeric(feature_df["pos"], errors="coerce").fillna(-1).astype(int)==pos_q) &
                (feature_df["ref"].astype(str).str.strip()==str(ref_in).strip()) &
                (feature_df["alt"].astype(str).str.strip()==str(alt_in).strip())
            ]
            if matched.shape[0] > 0:
                lookup = matched.iloc[0].to_dict()
        except Exception:
            lookup = None

    X = {}
    if lookup is not None:
        X.update(prepare_features_from_lookup(lookup))
        st.success("Found variant features in local CSV sample.")
    # override / apply manual values (grantham included)
    X["blosum62_raw"] = float(blosum_val)
    X["hydropathy_diff"] = float(hydro_val)
    X["is_stop"] = int(is_stop_val)
    X["grantham"] = float(grantham_val)
    X["af_filled"] = float(af_val)
    X["log_af"] = float(np.log10(X["af_filled"] + 1e-12))

    # ensure all FEATURES exist in right order
    X_row = {f: float(X.get(f, 0.0)) for f in FEATURES}
    X_df = pd.DataFrame([X_row], columns=FEATURES)

    if model is None:
        st.warning(f"No trained model found at `{MODEL_PATH}`. Falling back to heuristic.")
        is_path = (X_row["is_stop"] == 1) or (X_row["blosum62_raw"] <= -2.0)
        prob = 0.85 if is_path else 0.15
        label = "pathogenic" if is_path else "benign"
        st.markdown(f"<div class='result-card'><p class='small-label'>Heuristic</p><h2 class='big-prob'>{label.upper()}</h2><p>Probability (proxy): <strong>{prob:.2f}</strong></p></div>", unsafe_allow_html=True)
        plot_gauge(prob, label)
    else:
        label, prob = compute_prediction(model, X_df)
        st.markdown(f"<div class='result-card'><p class='small-label'>Model prediction</p><h2 class='big-prob'>{label.upper()}</h2><p>Probability (pathogenic): <strong>{prob:.3f}</strong></p></div>", unsafe_allow_html=True)
        plot_gauge(prob, label)

        # show model inputs
        with st.expander("View model inputs", expanded=False):
            st.write(X_df.T)

        # SHAP local explanation if available
        try:
            import shap
            expl = shap.TreeExplainer(model)
            raw = expl.shap_values(X_df)
            if isinstance(raw, list):
                shap_vals = raw[1] if len(raw) > 1 else raw[0]
            else:
                shap_vals = raw
            shap_arr = np.array(shap_vals)
            if shap_arr.ndim == 3 and shap_arr.shape[2] >= 2:
                shap_arr = shap_arr[:,:,1]
            plot_shap_bar_from_values(X_df.columns.tolist(), shap_arr)
            st.write("SHAP values (local):")
            df_shap = pd.DataFrame(shap_arr, columns=X_df.columns)
            st.dataframe(df_shap.T.rename(columns={0:"shap_value"}))
        except Exception:
            # silent fallback: show model importances (no warning text)
            try:
                fi = getattr(model, "feature_importances_", None)
                if fi is not None:
                    fi_df = pd.DataFrame({"feature": FEATURES, "importance": fi}).sort_values("importance", ascending=True)
                    fig, ax = plt.subplots(figsize=(7, max(2, 0.25*len(fi_df))), dpi=120)
                    sns.barplot(x="importance", y="feature", data=fi_df, ax=ax, palette="viridis")
                    ax.set_title("Model feature importance (fallback)")
                    st.pyplot(fig)
                    plt.close(fig)
            except Exception:
                pass

# Footer
st.markdown("---")
st.markdown(
    textwrap.dedent("""
    **About / Usage**  
    • Purpose: prototype decision-support for research variant annotation.  
    • Input: chromosome, position, ref, alt. Optionally provide features via the local CSV sample.  
    • Output: Predicted class (benign/pathogenic) and feature contributions (SHAP) where available.  

    **Caveat**: For research use only — not validated for clinical or diagnostic decisions.
    """)
)


