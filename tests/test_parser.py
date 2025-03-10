from backend.resume_parser import extract_text

def test_extract_text():
    text = extract_text("data/sample_resume.pdf")
    assert isinstance(text, str)
    assert len(text) > 0

