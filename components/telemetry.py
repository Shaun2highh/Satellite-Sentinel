import streamlit as st

def show_telemetry():

    st.subheader("🖥 System Telemetry")

    col1, col2 = st.columns(2)

    with col1:

        st.success("AI Vision Active")
        st.success("Infrared Sensors Online")

    with col2:

        st.info("Satellite: Sentinel-07")
        st.info("Mode: Thermal Scan")