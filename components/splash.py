import streamlit as st
import time

def startup_sequence():

    startup = st.empty()

    startup.markdown("""
    # 🛰 SATELLITE SENTINEL

    ### Initializing Orbital AI Systems...
    """)

    progress = st.progress(0)

    steps = [
        "Connecting to satellite...",
        "Loading AI systems...",
        "Calibrating thermal sensors...",
        "Activating wildfire scanner..."
    ]

    for i, step in enumerate(steps):

        st.info(step)

        progress.progress((i + 1) * 25)

        time.sleep(0.5)

    startup.empty()
    progress.empty()