import streamlit as st
import pandas as pd
import random
import time

# Page Config
st.set_page_config(page_title="Live Healthcare Monitoring", layout="wide")

st.title("🏥 Real-Time Healthcare Monitoring Dashboard")

# Create placeholders
heart_rate_plot = st.empty()
temp_plot = st.empty()
spo2_plot = st.empty()
bp_col1, bp_col2 = st.columns(2)
ecg_plot = st.empty()
motion_plot = st.empty()

# Live data loop
data_points = []

while True:
    # Simulated Data
    data = {
        "Time": time.strftime("%H:%M:%S"),
        "Heart Rate": random.randint(60, 100),
        "Temperature": round(random.uniform(36.5, 37.5), 1),
        "SpO2": random.randint(95, 100),
        "Systolic BP": random.randint(110, 130),
        "Diastolic BP": random.randint(70, 85),
        "ECG": round(random.uniform(-1.0, 1.0), 3),
        "Accel_X": round(random.uniform(-2, 2), 2),
        "Accel_Y": round(random.uniform(-2, 2), 2),
        "Accel_Z": round(random.uniform(-2, 2), 2)
    }

    data_points.append(data)

    # Keep only the last 30 points
    if len(data_points) > 30:
        data_points = data_points[-30:]

    df = pd.DataFrame(data_points)

    # Display Charts
    heart_rate_plot.line_chart(df[["Time", "Heart Rate"]].set_index("Time"))
    temp_plot.line_chart(df[["Time", "Temperature"]].set_index("Time"))
    spo2_plot.line_chart(df[["Time", "SpO2"]].set_index("Time"))

    with bp_col1:
        st.metric(label="🩺 Systolic BP", value=f"{data['Systolic BP']} mmHg")
    with bp_col2:
        st.metric(label="🩺 Diastolic BP", value=f"{data['Diastolic BP']} mmHg")

    ecg_plot.line_chart(df[["Time", "ECG"]].set_index("Time"))

    motion_df = df[["Time", "Accel_X", "Accel_Y", "Accel_Z"]].set_index("Time")
    motion_plot.line_chart(motion_df)

    time.sleep(1)