import gradio
import numpy as np
import joblib
from xgboost import XGBClassifier

# Replace 'path/to/model.pkl' with the actual path to your saved model
model = joblib.load('xgboost-model.pkl')

# Function for prediction
def predict_death_event(age, anaemia, high_blood_pressure, cpk, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time):
    # Assuming your loaded XGBClassifier model is stored in a variable called 'model'
    # Replace 'model' with the actual variable name if different
    features = np.array([[age, anaemia, high_blood_pressure, cpk, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time]])
    
    # Convert categorical features (sex) to numerical representation if needed for your model
    # This might involve using one-hot encoding or other techniques

    # Make predictions using the model
    predictions = model.predict_proba(features)[:, 1]  # Select probability for death event
    predicted_probability = predictions[0]
    threshold = 0.5  # You can adjust the threshold as needed
    classification = predicted_probability > threshold

    return int(predicted_probability*100), classification

# Inputs from user
# age, anaemia, high_blood_pressure, cpk, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time
inputs = [
    gradio.Slider(minimum=40, maximum=100, value=50, label="Age", step=1),
    gradio.Radio(choices=[('Yes',1), ('No',0)], label="Anaemia", show_label=True),
    gradio.Radio(choices=[('Yes',1), ('No',0)], label="High Blood Pressure"),
    "number",
    gradio.Radio(choices=[('Yes',1), ('No',0)], label="Diabetes"),
    "number",
    "number",
    gradio.Radio(choices=[("Female", 0), ("Male", 1)], label="Sex"),
    "number",
    "number",
    gradio.Radio(choices=[('Yes',1), ('No',0)], label="Smoking"),
    "number",
]
# Output response
# outputs = gradio.Text(label="Predicted Probability of Death Event")
outputs = [
  gradio.Text(label="Predicted Probability"),
  gradio.Text(label="High Risk (Yes/No)"),
]


title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

# Gradio interface to generate UI link
iface = gradio.Interface(fn = predict_death_event,
                         inputs = inputs,
                         outputs = outputs,
                         title = title,
                         description = description,
                         allow_flagging='never')

iface.launch(share = True) 