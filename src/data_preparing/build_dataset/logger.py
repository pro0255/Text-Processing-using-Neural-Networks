import csv
import os

from src.config.config import LOG_FILE_NAME


def log_error(directory: str, id: int, error) -> None:
    full_path = os.sep.join([directory, LOG_FILE_NAME])
    print(f"Logging to {full_path}")
    with open(full_path, "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        value = [id, error]
        writer.writerow(value)
