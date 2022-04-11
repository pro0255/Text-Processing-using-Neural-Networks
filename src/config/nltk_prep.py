import os

import nltk


def prepare_nltk_package(nltk_path):
    if not os.path.exists(nltk_path):
        os.makedirs(nltk_path)

    if nltk_path not in nltk.data.path:
        nltk.data.path.append(nltk_path)

    nltk.download("punkt", nltk_path)
    nltk.download("wordnet", nltk_path)
    nltk.download("omw-1.4", nltk_path)
