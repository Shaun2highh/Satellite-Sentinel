import streamlit as st

def show_creator():

    st.divider()

    st.subheader("👨‍🚀 About The Creator")

    st.markdown("""
    <div style='
    background:rgba(0,0,0,0.35);
    padding:25px;
    border-radius:15px;
    border:1px solid #00e5ff;
    '>

    <h3 style='color:#00e5ff;'>
    Shaurya Ranjan
    </h3>

    <p>
    High-school AI developer passionate about
    AI, aerospace systems, and computer vision.
    </p>

    </div>
    """, unsafe_allow_html=True)