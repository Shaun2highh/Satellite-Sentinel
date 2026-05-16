# components/radar.py

import streamlit as st

def show_radar():

    st.subheader("📡 Orbital Threat Radar")

    radar_html = """
    <style>

    .radar {
        position: relative;
        width: 420px;
        height: 420px;
        margin: auto;
        border-radius: 50%;
        overflow: hidden;

        background: radial-gradient(
            circle,
            rgba(0,229,255,0.1),
            #03111f 60%,
            black 100%
        );

        border: 2px solid #00e5ff;
        box-shadow: 0 0 25px #00e5ff;
    }

    .ring {
        position: absolute;
        border-radius: 50%;
        border: 1px solid rgba(0,229,255,0.25);
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .r1 { width: 100px; height: 100px; }
    .r2 { width: 200px; height: 200px; }
    .r3 { width: 300px; height: 300px; }
    .r4 { width: 400px; height: 400px; }

    /* SWEEP */
    .sweep {
        position: absolute;
        width: 50%;
        height: 3px;
        top: 50%;
        left: 50%;
        transform-origin: left center;

        background: linear-gradient(to right, transparent, #00e5ff);

        animation: spin 2.8s linear infinite;
        box-shadow: 0 0 20px #00e5ff;
    }

    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* BLIPS */
    .blip {
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: red;
        box-shadow: 0 0 12px red;
        animation: pulse 1.5s infinite;
    }

    .b1 { top: 30%; left: 60%; }
    .b2 { top: 55%; left: 35%; }
    .b3 { top: 70%; left: 75%; }

    @keyframes pulse {
        0% { transform: scale(0.8); opacity: 0.5; }
        50% { transform: scale(1.3); opacity: 1; }
        100% { transform: scale(0.8); opacity: 0.5; }
    }

    .center {
        position: absolute;
        width: 14px;
        height: 14px;
        background: #00e5ff;
        border-radius: 50%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        box-shadow: 0 0 20px #00e5ff;
    }

    </style>

    <div class="radar">

        <div class="ring r1"></div>
        <div class="ring r2"></div>
        <div class="ring r3"></div>
        <div class="ring r4"></div>

        <div class="sweep"></div>

        <div class="blip b1"></div>
        <div class="blip b2"></div>
        <div class="blip b3"></div>

        <div class="center"></div>

    </div>
    """

    st.html(radar_html)