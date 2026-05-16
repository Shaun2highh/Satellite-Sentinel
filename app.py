import streamlit as st
import cv2
import numpy as np
from PIL import Image

from assets.styles import load_css
from components.splash import startup_sequence
from components.radar import show_radar
from components.telemetry import show_telemetry
from components.creator import show_creator
from components.logs import show_logs
from utils.detection import detect_fire
from components.creator_page import show_creator_page

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Satellite Sentinel",
    page_icon="🛰",
    layout="wide"
)

# ==========================================
# LOAD CSS
# ==========================================

load_css()

# ==========================================
# STARTUP
# ==========================================

startup_sequence()

# ==========================================
# TITLE
# ==========================================

st.title("🛰 Satellite Sentinel")

st.markdown("""
### AI-Powered Orbital Wildfire Detection Platform
""")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🛰 Control Panel")

night_mode = st.sidebar.toggle(
    "Night Vision",
    value=True
)

sensitivity = st.sidebar.slider(
    "Detection Sensitivity",
    100,
    5000,
    1000
)

# ==========================================
# FILE UPLOADER
# ==========================================

uploaded_file = st.file_uploader(
    "Upload Satellite Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# MAIN PROCESSING
# ==========================================

if uploaded_file:

    image = Image.open(uploaded_file)

    img_array = np.array(image)

    st.image(
        image,
        caption="Satellite Input",
        width="stretch"
    )

    detected_rgb, overlay_rgb, risk = detect_fire(
        img_array,
        sensitivity
    )

    st.image(
        detected_rgb,
        caption="AI Detection",
        width="stretch"
    )

    st.image(
        overlay_rgb,
        caption="Thermal Overlay",
        width="stretch"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🔥 Wildfire Risk",
            f"{risk:.1f}%"
        )

    with col2:
        st.metric(
            "🛰 Satellite",
            "ONLINE"
        )

    with col3:
        st.metric(
            "🌍 Coverage",
            "94%"
        )

    show_telemetry()

    show_radar()

    show_logs()

show_creator_page()