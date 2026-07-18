"""
Global Student Migration Dashboard

Run with:
    streamlit run app.py
"""

import streamlit as st

st.set_page_config(page_title="Global Student Migration Dashboard", page_icon="🎓", layout="wide")

pages = [
    st.Page("pages/1_Overview.py", title="Overview", icon="🏠"),
    st.Page("pages/2_Migration_Patterns.py", title="Migration Patterns", icon="🌍"),
    st.Page("pages/3_Academics.py", title="Academics", icon="🎓"),
    st.Page("pages/4_Career_Outcomes.py", title="Career Outcomes", icon="💼"),
    st.Page("pages/5_Raw_Data.py", title="Raw Data", icon="🗂️"),
]

st.navigation(pages).run()