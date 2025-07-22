import streamlit as st
from cv_module import analyze_cxr
from rag_module import generate_report
from utils import load_templates

st.set_page_config(page_title="Chest X-Ray Report Assistant", layout="wide")
st.title("Chest X-Ray Report Assistant")

st.sidebar.header("Patient Information")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=45)
sex = st.sidebar.selectbox("Sex", ["Male", "Female", "Other"])
symptoms = st.sidebar.text_area("Primary Symptom(s)")
history = st.sidebar.text_area("Medical History")

uploaded_file = st.file_uploader("Upload Chest X-Ray Image", type=["png", "jpg", "jpeg", "bmp", "tiff"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded CXR", use_column_width=True)
    with st.spinner("Analyzing image..."):
        findings = analyze_cxr(uploaded_file)
    st.subheader("Visual Findings")
    st.write(findings)

    templates = load_templates()

    with st.spinner("Generating report..."):
        report = generate_report(findings, {
            "age": age,
            "sex": sex,
            "symptoms": symptoms,
            "history": history
        }, templates)
    st.subheader("Draft Radiology Report")
    st.code(report, language="markdown")
    st.download_button("Download Report", report, file_name="cxr_report.txt")
else:
    st.info("Please upload a chest X-ray image to begin.") 