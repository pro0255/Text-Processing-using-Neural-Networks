from src.config.config import LOG_FILE_NAME
import os
import csv


def log_error(directory, id, error):
    full_path = os.sep.join([directory, LOG_FILE_NAME])
    print(f"Logging to {full_path}")
    with open(full_path, "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        value = [id, error]
        writer.writerow(value)
