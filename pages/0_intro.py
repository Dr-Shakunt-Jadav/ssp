from pathlib import Path

import streamlit as st

from src.components.navigation import render_navigation

st.set_page_config(page_title="Intro", page_icon="🚀", layout="wide")

render_navigation("Intro")

ASSETS = Path(__file__).parent.parent / "assets"

# Streamlit's wide layout reserves ~6rem top / ~10rem bottom / ~1rem side padding
# on .block-container for its toolbar. The hero is designed edge-to-edge at 1440px,
# so that padding is zeroed here to match the wireframe exactly.
st.markdown(
    "<style>.block-container { padding: 2rem 0 0 0; max-width: 100%; }</style>",
    unsafe_allow_html=True,
)

hero_css = (ASSETS / "css" / "intro_hero.css").read_text()
hero_html = (ASSETS / "html" / "intro_hero.html").read_text()
st.markdown(
    f"<style>{hero_css}</style>"
    f'<div style="width:100%; max-width:1440px; margin:0 auto;">{hero_html}</div>',
    unsafe_allow_html=True,
)
