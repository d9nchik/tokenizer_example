from json import dump
import spacy
import re
from typing import List


def read() -> str:
    with open('input.txt', 'r', encoding='utf-8') as f:
        return f.read()


def write(tokens: List[str]) -> None:
    with open('output.json', 'w', encoding='utf-8') as f:
        dump(tokens, f, ensure_ascii=False)


def tokenize(text: str) -> List[str]:
    # loading model
    nlp = spacy.load('uk_core_news_sm')
    stop_words = nlp.Defaults.stop_words

    lemmatized_words = [doc.lemma_ for doc in nlp(text)]

    # removing stop words and punctuation
    return [word for word in lemmatized_words if word not in stop_words and re.match(r'\w+', word)]


if __name__ == '__main__':
    text = read()
    tokens = tokenize(text)
    write(tokens)
