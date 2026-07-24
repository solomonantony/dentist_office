#about.py
import streamlit as st
from pathlib import Path

st.title("About")
content = Path(__file__).parent.parent / "README.md"
st.markdown(content.read_text(encoding="utf-8"))
