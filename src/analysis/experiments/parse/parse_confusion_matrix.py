from src.config.config import FILENAME_CONFUSION_MATRIX
from src.analysis.experiments.validation.exists import exists
import pandas as pd


def parse_confusion_matrix(directory):
    path = exists(directory, FILENAME_CONFUSION_MATRIX)

    if path is None:
        return None

    content = pd.read_csv(path, sep=";")
    return content