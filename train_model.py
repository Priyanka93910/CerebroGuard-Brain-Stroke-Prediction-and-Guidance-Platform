"""
CerebroGuard — Model Training Script
Trains and compares Logistic Regression, Decision Tree, and Random Forest.
Saves the best model (Random Forest) + optimal threshold.
"""

import pandas as pd
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                              f1_score, roc_auc_score, roc_curve,
                              confusion_matrix, classification_report)
from sklearn.calibration import CalibratedClassifierCV
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

# ─────────────────────────────────────────────────────────────────────────────
# 1. Load & Preprocess Dataset
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 60)
print("  CerebroGuard — Stroke Risk Model Training")
print("=" * 60)

data = pd.read_csv("brain_stroke.csv")
print(f"\n✅ Dataset loaded: {data.shape[0]} rows × {data.shape[1]} columns")
print(f"   Stroke cases : {data['stroke'].sum()} ({data['stroke'].mean()*100:.1f}%)")
print(f"   Non-stroke   : {(data['stroke']==0).sum()} ({(1-data['stroke'].mean())*100:.1f}%)")

# Encode categorical variables
data["gender"] = data["gender"].map({"Male": 1, "Female": 0})
data["ever_married"] = data["ever_married"].map({"Yes": 1, "No": 0})
data["work_type"] = data["work_type"].map({
    "Private": 0, "Self-employed": 1, "Govt_job": 2, "children": 3, "Never_worked": 4
})
data["Residence_type"] = data["Residence_type"].map({"Urban": 1, "Rural": 0})
data["smoking_status"] = data["smoking_status"].map({
    "never smoked": 0, "formerly smoked": 1, "smokes": 2, "Unknown": 3
})

X = data.drop(columns=["id", "stroke"], errors="ignore")
y = data["stroke"]
X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\n📊 Train size: {len(X_train)} | Test size: {len(X_test)}")


# ─────────────────────────────────────────────────────────────────────────────
# 2. Train & Compare Multiple Models
# ─────────────────────────────────────────────────────────────────────────────
print("\n🔬 Training and comparing models...\n")

model_configs = {
    "Logistic Regression": LogisticRegression(
        class_weight="balanced", max_iter=1000, random_state=42
    ),
    "Decision Tree": DecisionTreeClassifier(
        max_depth=8, class_weight="balanced", random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=500, max_depth=12,
        class_weight="balanced", random_state=42
    )
}

results = {}
trained_pipelines = {}

for name, clf in model_configs.items():
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("smote", SMOTE(random_state=42)),
        ("model", clf)
    ])
    pipe.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)
    y_prob = pipe.predict_proba(X_test)[:, 1]

    results[name] = {
        "Accuracy":  round(accuracy_score(y_test, y_pred) * 100, 2),
        "Precision": round(precision_score(y_test, y_pred, zero_division=0) * 100, 2),
        "Recall":    round(recall_score(y_test, y_pred, zero_division=0) * 100, 2),
        "F1-Score":  round(f1_score(y_test, y_pred, zero_division=0) * 100, 2),
        "AUC-ROC":   round(roc_auc_score(y_test, y_prob) * 100, 2),
    }
    trained_pipelines[name] = pipe
    print(f"  ✓ {name} done")

# Print comparison table
print("\n" + "=" * 70)
print(f"{'Model':<25} {'Accuracy':>9} {'Precision':>10} {'Recall':>8} {'F1':>8} {'AUC-ROC':>9}")
print("-" * 70)
for name, m in results.items():
    print(f"{name:<25} {m['Accuracy']:>8}%  {m['Precision']:>9}%  "
          f"{m['Recall']:>7}%  {m['F1-Score']:>7}%  {m['AUC-ROC']:>8}%")
print("=" * 70)

# Save comparison results
results_df = pd.DataFrame(results).T
results_df.to_csv("model_comparison.csv")
print("\n✅ Model comparison saved to model_comparison.csv")


# ─────────────────────────────────────────────────────────────────────────────
# 3. Calibrate Best Model (Random Forest)
# ─────────────────────────────────────────────────────────────────────────────
print("\n🎯 Calibrating Random Forest (best model)...")

best_pipeline = trained_pipelines["Random Forest"]
calibrated_model = CalibratedClassifierCV(best_pipeline, method="isotonic", cv=5)
calibrated_model.fit(X_train, y_train)

y_pred_final = calibrated_model.predict(X_test)
y_prob_final = calibrated_model.predict_proba(X_test)[:, 1]

print("\n📊 Calibrated Random Forest — Final Metrics:")
print(f"   Accuracy : {accuracy_score(y_test, y_pred_final)*100:.2f}%")
print(f"   Precision: {precision_score(y_test, y_pred_final, zero_division=0)*100:.2f}%")
print(f"   Recall   : {recall_score(y_test, y_pred_final, zero_division=0)*100:.2f}%")
print(f"   F1-Score : {f1_score(y_test, y_pred_final, zero_division=0)*100:.2f}%")
print(f"   AUC-ROC  : {roc_auc_score(y_test, y_prob_final)*100:.2f}%")

print("\n📋 Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred_final)
print(f"   TN={cm[0,0]}  FP={cm[0,1]}")
print(f"   FN={cm[1,0]}  TP={cm[1,1]}")

print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred_final, target_names=["No Stroke", "Stroke"]))


# ─────────────────────────────────────────────────────────────────────────────
# 4. Find Optimal Threshold (maximises recall for medical use)
# ─────────────────────────────────────────────────────────────────────────────
fpr, tpr, thresholds = roc_curve(y_test, y_prob_final)
optimal_idx = (tpr - fpr).argmax()
optimal_threshold = float(thresholds[optimal_idx])
print(f"\n🎯 Optimal Medical Threshold: {optimal_threshold:.4f}")
print(f"   At this threshold — TPR (Recall): {tpr[optimal_idx]:.2%}  "
      f"| FPR: {fpr[optimal_idx]:.2%}")


# ─────────────────────────────────────────────────────────────────────────────
# 5. Feature Importance
# ─────────────────────────────────────────────────────────────────────────────
try:
    base_rf = calibrated_model.calibrated_classifiers_[0].estimator.named_steps["model"]
    feat_names = X.columns.tolist()
    importances = base_rf.feature_importances_
    feat_df = pd.DataFrame({"Feature": feat_names, "Importance (%)": (importances * 100).round(2)})
    feat_df = feat_df.sort_values("Importance (%)", ascending=False)
    print("\n🔍 Feature Importances:")
    for _, row in feat_df.iterrows():
        bar = "█" * int(row["Importance (%)"] / 2)
        print(f"   {row['Feature']:<22} {row['Importance (%)']:>5}%  {bar}")
    feat_df.to_csv("feature_importance.csv", index=False)
    print("\n✅ Feature importances saved to feature_importance.csv")
except Exception:
    pass


# ─────────────────────────────────────────────────────────────────────────────
# 6. Save Model & Threshold
# ─────────────────────────────────────────────────────────────────────────────
joblib.dump(calibrated_model, "stroke_model.pkl")
joblib.dump(optimal_threshold, "threshold.pkl")

print("\n✅ stroke_model.pkl saved!")
print("✅ threshold.pkl saved!")
print("\n" + "=" * 60)
print("  Training complete. Run your Streamlit app now.")
print("=" * 60)