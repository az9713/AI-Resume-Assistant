from fastapi import FastAPI, File, UploadFile
from backend.resume_parser import extract_text
from backend.keyword_matcher import extract_keywords
from backend.cover_letter_gen import generate_cover_letter
from backend.ats_checker import check_ats_compliance

app = FastAPI()

@app.post("/analyze/")
async def analyze_resume(resume: UploadFile, job_desc: str):
    """
    API endpoint to analyze a resume.
    """
    resume_text = extract_text(resume.file.name)
    matched_keywords = set(extract_keywords(resume_text)) & set(extract_keywords(job_desc))
    cover_letter = generate_cover_letter(job_desc, resume_text)
    ats_score = check_ats_compliance(resume_text, job_desc)

    return {
        "matched_keywords": list(matched_keywords),
        "cover_letter": cover_letter,
        "ats_score": ats_score
    }

