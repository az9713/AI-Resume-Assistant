from backend.cover_letter_gen import generate_cover_letter

def test_generate_cover_letter():
    job_desc = "We are hiring a data scientist with expertise in NLP."
    resume_text = "I have 3 years of experience in NLP and machine learning."
    cover_letter = generate_cover_letter(job_desc, resume_text)
    
    assert isinstance(cover_letter, str)
    assert len(cover_letter) > 50

