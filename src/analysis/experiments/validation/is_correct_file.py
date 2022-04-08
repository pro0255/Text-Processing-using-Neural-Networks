import os
from src.config.config import (
    FILENAME_CONFUSION_MATRIX,
    FILENAME_METRICS,
    FILENAME_DESCRIPTION,
    FILENAME_SUMMARIZATION,
    FILENAME_LOGS
)

filenames = [
    FILENAME_CONFUSION_MATRIX,
    FILENAME_METRICS,
    FILENAME_DESCRIPTION,
    FILENAME_SUMMARIZATION,
    FILENAME_LOGS
]


def is_correct_file(path):
    for filename in filenames:
        current_path = os.path.sep.join([path, filename])
        if os.path.exists(current_path):
            return True
    return False
