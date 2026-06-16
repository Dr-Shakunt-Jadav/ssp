# Tests the Intro page in isolation.
# Run from project root: streamlit run tests/t_pages/test_0_intro.py
import runpy

runpy.run_path("pages/0_intro.py", run_name="__main__")
