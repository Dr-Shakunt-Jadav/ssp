# Tests the Results page in isolation.
# Run from project root: streamlit run tests/t_pages/test_3_results.py
import runpy

runpy.run_path("pages/3_results.py", run_name="__main__")
