from keybert import KeyBERT

kw_model = KeyBERT()

def extract_keywords(text):
    """
    Extracts top keywords from a given text.
    """
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=10)
    return [kw[0] for kw in keywords]

