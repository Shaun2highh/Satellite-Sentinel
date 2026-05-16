import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp {

        background:
        linear-gradient(
            135deg,
            #020b14,
            #061d33
        );

        color: white;
    }

    h1, h2, h3 {

        color: #00e5ff;

        text-shadow:
        0 0 10px #00e5ff;
    }

    [data-testid="metric-container"] {

        background:
        rgba(0,0,0,0.35);

        border:
        1px solid #00e5ff;

        border-radius: 15px;

        padding: 15px;
    }

    </style>
    """, unsafe_allow_html=True)