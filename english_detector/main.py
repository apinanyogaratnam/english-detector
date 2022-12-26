import pycld2 as cld2
from textblob import TextBlob


def detect_english(text: str | None) -> bool:
    if not text:
        return True

    return TextBlob(text).detect_language()

    _, _, _, detect_language = cld2.detect(text, returnVectors=True)

    return len(detect_language) == 1 and detect_language[0][2] == 'ENGLISH'


if __name__ == '__main__':
    print(detect_english('this is english.'))
