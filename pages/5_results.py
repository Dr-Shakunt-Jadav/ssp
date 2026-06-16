from pathlib import Path

import streamlit as st

from utils.model_utils import load_ml_model
from src.services.predictor import get_prediction
from src.components.results import render_results
from src.components.navigation import render_navigation

st.set_page_config(page_title="Results", page_icon="📊", layout="wide")

render_navigation("Results")

ASSETS = Path(__file__).parent.parent / "assets"
brand_css = (ASSETS / "css" / "brand_mark.css").read_text()
brand_html = (ASSETS / "html" / "brand_mark.html").read_text()
st.markdown(f"<style>{brand_css}</style>{brand_html}", unsafe_allow_html=True)


@st.cache_resource
def get_model():
    return load_ml_model()


if "payload" not in st.session_state:
    st.info("Fill out the Company Profile form first to see results.")
else:
    model = get_model()
    result = get_prediction(st.session_state.payload, model)
    render_results(result, st.session_state.payload)
