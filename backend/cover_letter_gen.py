from transformers import pipeline

cover_letter_generator = pipeline("text-generation", model="facebook/bart-large-cnn")

def generate_cover_letter(job_desc, resume_text):
    """
    Generates a cover letter based on the job description and resume.
    """
    input_text = f"Write a cover letter for the job: {job_desc}\nResume: {resume_text}"
    result = cover_letter_generator(input_text, max_length=300, do_sample=True)
    return result[0]['generated_text']

