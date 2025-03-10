import streamlit as st
from backend.resume_parser import extract_text
from backend.keyword_matcher import extract_keywords
from backend.cover_letter_gen import generate_cover_letter
from backend.ats_checker import check_ats_compliance

st.title("📄 AI Resume & Job Application Assistant")

uploaded_file = st.file_uploader("📂 Upload your resume (PDF/DOCX)")
job_desc = st.text_area("📝 Paste Job Description")

if uploaded_file and job_desc:
    resume_text = extract_text(uploaded_file.name)
    matched_keywords = set(extract_keywords(resume_text)) & set(extract_keywords(job_desc))
    cover_letter = generate_cover_letter(job_desc, resume_text)
    ats_score = check_ats_compliance(resume_text, job_desc)

    st.subheader("🔑 Matching Keywords:")
    st.write(matched_keywords)

    st.subheader("📄 AI-Generated Cover Letter:")
    st.write(cover_letter)

    st.subheader("📊 ATS Score:")
    st.write(f"✅ Your resume matches {ats_score}% of the job description.")

