import streamlit as st
import requests

st.title("Weather Prediction")

temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
pressure = st.number_input("Pressure")
wind_speed = st.number_input("Wind Speed")
wind_deg = st.number_input("Wind Degree")

if st.button("Predict"):
    params = {
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'wind_deg': wind_deg
    }
    response = requests.get("http://localhost:5000/predict", params=params)
    prediction = response.json()['prediction']
    st.write(f"Prediction: {prediction}")
