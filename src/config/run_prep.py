from src.config.nltk_prep import prepare_nltk_package
from src.config.config import NLTK_PATH


def run_prep():
    print("Running preperation of packages")
    prepare_nltk_package(NLTK_PATH)
