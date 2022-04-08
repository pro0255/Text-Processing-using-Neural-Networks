from src.analysis.experiments.validation.is_correct_file import is_correct_file
from src.analysis.experiments.create_record import create_record
import os


def process_directory(directory, storage=None):
    is_correct = is_correct_file(directory)
    record = None

    if is_correct:
        if storage is not None:
            record = create_record(directory)
            if record is not None:
                storage.append(record)

    for current_directory in os.listdir(directory):
        deeper_level = os.path.sep.join([directory, current_directory])
        if os.path.isdir(deeper_level):
            process_directory(deeper_level, storage)
