import typing
import pandas as pd

from src.analysis.experiments.validation.exists import exists
from src.config.config import FILENAME_SUMMARIZATION


def parse_summarization(directory: str) -> typing.Union[pd.DataFrame, None]:
    path = exists(directory, FILENAME_SUMMARIZATION)

    if path is None:
        return None

    content = pd.read_csv(path, sep=";")
    content.columns = ["id", "value"]
    return content
