import spacy

from spacy_langdetect import LanguageDetector


def detect_english(text: str | None, expected_score: float | None = None) -> bool:
    if not text:
        return True

    nlp = spacy.load('en')
    nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)
    doc = nlp(text)
    detect_language = doc._.language

    language = detect_language['language']
    actual_score = detect_language['score']

    is_english = True
    if expected_score is not None:
        is_english = is_english and actual_score >= expected_score

    return is_english and language == 'en'
