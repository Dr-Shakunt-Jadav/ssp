run:
	fuser -k 8501/tcp 2>/dev/null || true
	streamlit run app.py
