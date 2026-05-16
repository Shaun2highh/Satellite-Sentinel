# components/creator_page.py

import streamlit as st

def show_creator_page():

    st.title("🌍 Forest Fires & About the Creator")

    # ==================================================
    # 1. FOREST FIRE SECTION (≈300 words)
    # ==================================================

    st.markdown("""
### 🔥 Understanding Forest Fires

Forest fires, also known as wildfires, are uncontrolled fires that spread rapidly through vegetation such as forests, grasslands, and shrubs. They can be triggered by natural causes like lightning or by human activities such as unattended campfires, burning debris, or land clearing. Once ignited, they can spread quickly depending on weather conditions like wind, temperature, and dryness of vegetation.

These fires are especially dangerous because they consume everything in their path, including trees, wildlife habitats, and sometimes even human settlements near forest regions. In recent years, forest fires have become more frequent and intense due to climate change, rising global temperatures, and prolonged dry seasons.

Despite their destructive nature, forest fires also play a natural ecological role in some ecosystems. Certain forests depend on periodic fires to clear dead vegetation, recycle nutrients back into the soil through ash, and allow new plant species to grow. Some tree species even require fire for their seeds to germinate.

However, uncontrolled or excessive fires cause severe environmental damage. They release large amounts of carbon dioxide and smoke into the atmosphere, contributing to air pollution and climate change. They also destroy biodiversity by killing animals and destroying their habitats. In many regions, human expansion into forest areas has increased the risk of fires becoming disasters rather than natural ecological events.

Because of these risks, modern technology such as satellite monitoring, AI-based detection systems, and early warning models are being developed to detect fires early and reduce damage. These systems help identify heat signatures and abnormal vegetation changes before fires spread widely.
""")

    st.divider()

    # ==================================================
    # 2. ABOUT CREATOR (≈200 words)
    # ==================================================

    st.markdown("""
### 👨‍🚀 About the Shaurya
Satellite Sentinel was built by me as a personal exploration into how far AI and computer vision can be pushed to solve real-world environmental problems. I am a high school student deeply interested in artificial intelligence, aerospace systems, and the idea that technology can actively protect our planet rather than just analyze it.
When I started this project, my goal wasn’t just to build another dashboard or detection model—it was to understand how satellite imagery, data processing, and AI-based vision systems come together in real-world disaster monitoring. Through this process, I learned how complex and powerful even “simple” detection systems can become when applied to global issues like wildfires and deforestation.
This project represents my curiosity, persistence, and growing interest in building systems that matter beyond code. I still have a long way to go, but Satellite Sentinel is an early step in that direction.
For now, I see this as more than just a project—it’s a direction I want to grow in. In the future, I hope to expand it into something that can integrate live satellite feeds and contribute, even in a small way, to global climate monitoring and early disaster response systems.

""")