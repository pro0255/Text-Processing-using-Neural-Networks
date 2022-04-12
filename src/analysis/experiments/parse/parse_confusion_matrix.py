import typing

import pandas as pd

from src.analysis.experiments.validation.exists import exists
from src.config.config import FILENAME_CONFUSION_MATRIX


def parse_confusion_matrix(directory: str) -> typing.Union[pd.DataFrame, None]:
    path = exists(directory, FILENAME_CONFUSION_MATRIX)

    if path is None:
        return None

    content = pd.read_csv(path, sep=";")
    return content
