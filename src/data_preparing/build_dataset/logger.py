import csv
import os

from src.config.config import LOG_FILE_NAME


def log_error(directory: str, id: int, error) -> None:
    """Sometimes was not saved data from work of art. Because of this problem was created new function which take care of logging action."""
    full_path = os.sep.join([directory, LOG_FILE_NAME])
    print(f"Logging to {full_path}")
    with open(full_path, "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        value = [id, error]
        writer.writerow(value)
