from src.config.config import NLTK_PATH
from src.config.nltk_prep import prepare_nltk_package


def run_prep():
    print("Running preperation of packages")
    prepare_nltk_package(NLTK_PATH)
