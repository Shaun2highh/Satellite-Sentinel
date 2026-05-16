import streamlit as st
import time

def show_logs():

    st.subheader("🤖 AI Logs")

    logs = [
        "Scanning vegetation...",
        "Thermal anomaly detected...",
        "Satellite uplink stable...",
        "Orbital sweep complete..."
    ]

    for log in logs:

        st.code(log)

        time.sleep(0.1)