"""
Integrated Clinical Risk Stratification and Action Recommendation System

Purpose:
To aggregate disease-specific risk models for diabetes, chronic kidney disease,
and cardiovascular disease into a unified clinical decision-support tool.

Scope:
Supports early risk stratification, preventive care planning, and referral
prioritization in resource-constrained healthcare settings.

Note:
This system is intended for screening and decision support, not definitive diagnosis.
"""


import numpy as np
import pandas as pd
import joblib

# Diabetes
diabetes_model = joblib.load("diabetes_random_forest_model.pkl")
diabetes_scaler = joblib.load("diabetes_scaler.pkl")

# CKD (early risk model, NO GFR)
ckd_model = joblib.load("ckd_random_forest_model.pkl")
ckd_scaler = joblib.load("ckd_scaler.pkl")

# Heart disease (pipeline model)
heart_model = joblib.load("heart_random_forest_model.pkl")

patient_data = {
    # Diabetes features
    "Pregnancies": 2,
    "Glucose": 135,
    "BloodPressure": 82,
    "SkinThickness": 25,
    "Insulin": 120,
    "BMI": 29.5,
    "DiabetesPedigreeFunction": 0.6,
    "Age": 45,

    # CKD features (NO GFR)
    "Age": 45,
    "Creatinine_Level": 1.4,
    "BUN": 26,
    "Diabetes": 1,
    "Hypertension": 1,
    "Urine_Output": 900,
    
    # Heart disease features — STRING CATEGORIES
    "age": 45,
    "sex": "Male",
    "chest_pain_type": "Typical angina",
    "resting_blood_pressure": 135,
    "cholestoral": 240,
    "fasting_blood_sugar": "Yes",
    "rest_ecg": "Normal",
    "Max_heart_rate": 150,
    "exercise_induced_angina": "No",
    "oldpeak": 1.2,
    "slope": "Flat"
}

diabetes_features = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

diabetes_input = pd.DataFrame([[patient_data[f] for f in diabetes_features]],
                              columns=diabetes_features)

diabetes_input_scaled = diabetes_scaler.transform(diabetes_input)
diabetes_risk = diabetes_model.predict_proba(diabetes_input_scaled)[0][1]

ckd_features = [
   "Age", "Creatinine_Level", "BUN", "Diabetes", "Hypertension", "Urine_Output"
]

ckd_input = pd.DataFrame([[patient_data[f] for f in ckd_features]],
                              columns=ckd_features)

ckd_input_scaled = ckd_scaler.transform(ckd_input)
ckd_risk = ckd_model.predict_proba(ckd_input_scaled)[0][1]

heart_features = [
    "age", "sex", "chest_pain_type",
    "resting_blood_pressure", "cholestoral",
    "fasting_blood_sugar", "rest_ecg",
    "Max_heart_rate", "exercise_induced_angina",
    "oldpeak", "slope"
]

heart_input = pd.DataFrame([[patient_data[f] for f in heart_features]],
                           columns=heart_features)

heart_risk = heart_model.predict_proba(heart_input)[0][1]

risk_scores = {
    "Diabetes": diabetes_risk,
    "CKD": ckd_risk,
    "Heart Disease": heart_risk
}

overall_risk_score = np.mean(list(risk_scores.values()))

if overall_risk_score < 0.30:
    risk_category = "Low Risk"
elif overall_risk_score < 0.69:
    risk_category = "Moderate Risk"
else:
    risk_category = "High Risk"

if risk_category == "Low Risk":
    recommendation = (
        "Routine monitoring and lifestyle counseling. "
        "Encourage healthy diet, physical activity, and periodic screening."
    )

elif risk_category == "Moderate Risk":
    recommendation = (
        "Targeted screening and preventive intervention recommended. "
        "Order confirmatory laboratory tests and initiate risk factor management."
    )

else:
    recommendation = (
        "High priority referral recommended. "
        "Initiate comprehensive clinical evaluation, specialist referral, "
        "and aggressive risk reduction strategies."
    )

print("=== Integrated Clinical Risk Stratification Report ===\n")

for disease, score in risk_scores.items():
    print(f"{disease} Risk Score: {score:.2f}")

print(f"\nOverall Risk Score: {overall_risk_score:.2f}")
print(f"Risk Category: {risk_category}")

print("\nRecommended Clinical Action:")
print(recommendation)