from sklearn.feature_extraction.text import CountVectorizer

def check_ats_compliance(resume_text, job_desc):
    """
    Compares resume text with job description to determine ATS compatibility.
    """
    vectorizer = CountVectorizer().fit([resume_text, job_desc])
    resume_vector = vectorizer.transform([resume_text]).toarray()
    job_vector = vectorizer.transform([job_desc]).toarray()

    match_score = (resume_vector * job_vector).sum() / (sum(job_vector[0]) + 1)
    return round(match_score * 100, 2)

