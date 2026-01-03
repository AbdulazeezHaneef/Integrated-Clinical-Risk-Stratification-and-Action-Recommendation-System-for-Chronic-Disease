## Overview

This project designs a support system [integrated Clinical Risk Stratification and Decision Support System] which aims to convert results of machine learning predictions into recomendations and
action plan. The model was designed to show or reflect how clinical informatics tool are used in real life settings rather than just only focusing on better or higher machine learning predictions.

The model incorperates already designed models for Chronc Kidney Disease, Diabetes and Heart Disease to generate a single risk level score and recommendations (action plans). The primary aim is to
show how multiple models of machine language predictors can be incorperated into a single decision support system.

## Aim

Risk prevention in clinical practice incoperates more than just treating a single disease as most patiens are often are present with overlapping complications of either Diabetic and renal, or
renal and heart e.t.c. This requires clinical staffs to asses overall risk instead of just focusing on one.
The project was motivated by:
- the need for risk stratification and not just diagnosis.
- Adding value by converting ML prediction scores into decision support and action systems.
- Using informatics to draw links tat we might not notice or undermine.

## Design Model

The model is composed of four main layers or parts.

First is the input layer which is composed of patients clinical datasuch as demographic data, Labouratory results and physiological measurements.

The second layer is the disease specific prediction layer. which consist of already trained machine learning models which analyse and predict the probability of
1, Chronic Kidney Disease
2, Diabetes
3, Heart Disease

The third layer is where the risk stratification is done. machine learning model results of predicting a disease is converted into clinically interpretable risk categories such as
1, Low
2, Moderat
3, High

the fourth and last layer is the Action or decision support layer. each disease specific risk are combined to generate a single overall patient risk level and recommend clinical actions.

## Risk Logic

Disease Level Risk Categories
Each disease model of machine learnig gives a prediction which is categorized as 
1, [0.00 - 0.30] Low Risk
2, [0.30 - 0.69] this range is considered as Moderate risk
3, [0.70 - 1.00] this range is considered as High risk
these ranges where intentionally made conservative in order to support early detection.

Integraded Patient Risk Logic
The merging of each disease prediction result into one overall output follows the following rules
1, High Overall Risk
 - When at least one disease is classsified as High risk
 - Two or more are classified as Moderate risk
2, Moderate Overall risk
 - when one disease is calssified as moderate risk
3, Low ovweall risk
 - When all disease are classified as low risk
These approach mirrors real world clinical decision making.

## Output

The sysproduces a structured clinical summary which includes the following:
1, Disease specific risk predction scores
2, Overall integrated patient risk
3, Text based clinical recommendations

Example output :
INTEGRATED CLINICAL RISK SUMMARY

Heart Disease Risk: High (0.82)
Chronic Kidney Disease Risk: Moderate (0.46)
Diabetes Risk: Low (0.18)

Overall Patient Risk: HIGH

Recommended Clinical Actions:
- Immediate referral to cardiology
- Regular renal function monitoring
- Lifestyle and dietary intervention
- Cardiometabolic risk counseling

## Models Used

This system integrates three previously developed and validated models

1, Chronic Kidney Disease
 - Logistics Regression
 - Random Forest Model [early risk model without GFR]
2, Diabetes
 - Logistics Regression
 - Random Forest Model
3, Heart Disease
 - Logistics Regression
 - Random Forest Model
Feature importance analysis was done for all models in order to ensure clinical credibility.

## Important Note on Model Files
This repository does not include trained model (.pkl) files.

The following files are expected to be generated locally from the corresponding training
repositories before running this system:

- diabetes_random_forest_model.pkl
- diabetes__logistics_model.pkl
- diabetes_scaler.pkl
- ckd_random_forest_model.pkl
- ckd_logistics_model.pkl
- ckd_scaler.pkl
- heart_random_forest_model.pkl
- heart_logistics_model.pkl

## Files
- Integrated_clinical_risk_system.py : Integrated risk aggregation and recommendation logic
- README.md : System documentation

## Intended Use
This system is intended for **clinical screening and decision support only. It is not a diagnostic tool and does not replace clinical judgment.

## Conclusions

This integrated decision system shows how predictive models used beyond just prediction to support patient management and cli ical reasoning. By focusing on risk stratificaton and action
recommendations,the projectaligns with real world clinical decision making and it also shows the role of informatics in improving clinical outcomes.
