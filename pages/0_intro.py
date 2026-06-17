from pathlib import Path

import streamlit as st

from src.components.navigation import render_navigation, PATH_BY_LABEL

st.set_page_config(page_title="Intro", page_icon="🚀", layout="wide")

render_navigation("Intro")

ASSETS = Path(__file__).parent.parent / "assets"

# Streamlit's wide layout reserves ~6rem top / ~10rem bottom / ~1rem side padding
# on .block-container for its toolbar. The hero is designed edge-to-edge at 1440px,
# so that padding is zeroed here to match the wireframe exactly.
st.markdown(
    """
    <style>
      /* Full-page gradient background */
      [data-testid="stAppViewContainer"],
      [data-testid="stApp"] {
        background: linear-gradient(135deg, #B8E5FF 0%, #7DD3F8 50%, #5BB5F0 100%) !important;
      }
      /* Remove sidebar background so it blends */
      [data-testid="stSidebar"] {
        background: rgba(255,255,255,0.25) !important;
        backdrop-filter: blur(8px);
      }
      .block-container { padding: 2rem 0 0 0; max-width: 100%; }
    </style>
    """,
    unsafe_allow_html=True,
)

hero_css = (ASSETS / "css" / "intro_hero.css").read_text()
hero_html = (ASSETS / "html" / "intro_hero.html").read_text()
st.markdown(
    f"<style>{hero_css}</style>"
    f'<div style="width:100%; max-width:1440px; margin:0 auto;">{hero_html}</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="intro-cta">', unsafe_allow_html=True)
if st.button("Measure yourself", key="intro_cta"):
    st.switch_page(PATH_BY_LABEL["Initiate"])
st.markdown('</div>', unsafe_allow_html=True)
