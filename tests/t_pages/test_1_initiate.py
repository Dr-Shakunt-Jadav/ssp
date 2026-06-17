# Tests the Initiate page in isolation.
# Run from project root: streamlit run tests/t_pages/test_1_initiate.py
import runpy

runpy.run_path("pages/1_initiate.py", run_name="__main__")
