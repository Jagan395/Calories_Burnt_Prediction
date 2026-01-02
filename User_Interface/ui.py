import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Calories Burnt Prediction", layout="centered")

st.title("Calories Burnt Prediction")
st.write("Enter the details below to predict calories burnt")



gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=25,key="age")
height = st.number_input("Height (cm)", min_value=40.0, max_value=250.0, value=154.0,key="height")
weight = st.number_input("Weight (kgs)", min_value=1.0, max_value=300.0, value=65.0,key="weight")
duration = st.number_input("Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0,key="duration")
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40.0, max_value=200.0, value=80.0,key="heart_rate")
body_temp = st.number_input("Body Temperature (°C)", min_value=37.0, max_value=42.0, value=37.0,key="body_temp")


if st.button("Predict Calories Burnt"):
    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 203:
            result = response.json()
            st.success(result["response"])
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error("Unable to connect to FastAPI server")
        st.write(e)
