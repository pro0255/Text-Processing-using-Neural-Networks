from src.config.config import FILENAME_METRICS
from src.analysis.experiments.validation.exists import exists
import pandas as pd


def parse_metrics(directory):
    path = exists(directory, FILENAME_METRICS)

    if path is None:
        return None

    content = pd.read_csv(path, sep=";")
    content.columns = ["id", "value"]
    return content
