import typing

import pandas as pd

from src.analysis.experiments.merge.merge_content import merge_content
from src.analysis.experiments.parse.parse_confusion_matrix import parse_confusion_matrix
from src.analysis.experiments.parse.parse_description import parse_description
from src.analysis.experiments.parse.parse_log import parse_log
from src.analysis.experiments.parse.parse_metrics import parse_metrics
from src.analysis.experiments.parse.parse_summarization import parse_summarization


def create_record(directory: str) -> typing.Union[pd.DataFrame, None]:
    """Creates record from .csv files which are situated in experiment directory

    Args:
        directory (str): directory which should be loaded

    Returns:
        typing.Union[pd.DataFrame, None]: DataFrame record or None
    """
    try:
        confusion_matrix = parse_confusion_matrix(directory)
        metrics = parse_metrics(directory)
        description = parse_description(directory)
        summarization = parse_summarization(directory)
        logs = parse_log(directory)
        record = merge_content(
            confusion_matrix, metrics, description, summarization, directory, logs
        )
        return record
    except Exception as e:
        print(f"Exception in {directory}")
        print(f"Exception {e}")
        return None
