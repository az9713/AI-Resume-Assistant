import gradio as gr
from backend.resume_parser import extract_text
from backend.keyword_matcher import extract_keywords
from backend.cover_letter_gen import generate_cover_letter
from backend.ats_checker import check_ats_compliance

def analyze_resume(resume_file, job_desc):
    resume_text = extract_text(resume_file.name)
    matched_keywords = set(extract_keywords(resume_text)) & set(extract_keywords(job_desc))
    cover_letter = generate_cover_letter(job_desc, resume_text)
    ats_score = check_ats_compliance(resume_text, job_desc)

    return "\n".join(matched_keywords), cover_letter, f"ATS Score: {ats_score}%"

iface = gr.Interface(
    fn=analyze_resume,
    inputs=["file", "text"],
    outputs=["text", "text", "text"],
    title="AI Resume & Job Application Assistant",
)

iface.launch()

