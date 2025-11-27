#conda activate iris_env
#python -m streamlit run app.py


import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# -------------------------------
# Load Preprocessing Objects
# -------------------------------
with open("label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# -------------------------------
# Load ANN Model
# -------------------------------
model = load_model("ann_model.keras")

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🌸 Iris Flower Classification (ANN)")

st.write("Enter the flower measurements below:")

# User Inputs
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Predict Button
if st.button("🔮 Predict"):
    # Prepare input
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    features_scaled = scaler.transform(features)

    # Model Prediction
    prediction = model.predict(features_scaled)
    predicted_class = np.argmax(prediction, axis=1)
    flower_name = encoder.inverse_transform(predicted_class)[0]

    st.success(f"🌼 Predicted Species: **{flower_name}**")

