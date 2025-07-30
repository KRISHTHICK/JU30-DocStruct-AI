import streamlit as st
from document_parser import parse_docx
from pattern_detector import detect_patterns
import json

st.title("DocStruct-AI - Document Structure Pattern Detector")

uploaded = st.file_uploader("Upload MS Word document (.docx)", type=["docx"])

if uploaded:
    sections = parse_docx(uploaded)
    rules = detect_patterns(sections)

    st.subheader("Detected Patterns")
    st.json(rules)

    if st.button("Save Rules"):
        with open("rules/approved_rules.json", "w") as f:
            json.dump(rules, f, indent=2)
        st.success("Rules saved and approved!")
