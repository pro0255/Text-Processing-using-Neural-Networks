import os
import typing

from src.config.config import (
    FILENAME_CONFUSION_MATRIX,
    FILENAME_DESCRIPTION,
    FILENAME_LOGS,
    FILENAME_METRICS,
    FILENAME_SUMMARIZATION,
)

filenames = [
    FILENAME_CONFUSION_MATRIX,
    FILENAME_METRICS,
    FILENAME_DESCRIPTION,
    FILENAME_SUMMARIZATION,
    FILENAME_LOGS,
]


def is_correct_file(path: str, filenames: typing.List[str] = filenames) -> bool:
    for filename in filenames:
        current_path = os.path.sep.join([path, filename])
        if os.path.exists(current_path):
            return True
    return False
