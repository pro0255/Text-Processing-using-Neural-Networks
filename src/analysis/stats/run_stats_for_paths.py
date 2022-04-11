import os

from src.analysis.experiments.validation.is_correct_file import is_correct_file
from src.analysis.stats.config import FILENAMES, START_DIRECTORY
from src.analysis.stats.process_path import process_path


def load_paths(directory=START_DIRECTORY, storage=None):
    for current_directory in os.listdir(directory):

        is_correct = is_correct_file(directory, FILENAMES)

        if is_correct:
            if storage is not None:
                storage.append(directory)
                return

        deeper_level = os.path.sep.join([directory, current_directory])
        if os.path.isdir(deeper_level):
            load_paths(deeper_level, storage)


def process_paths(
    directories,
    normalization_values,
    preprocessing_types,
    subsets,
    transformer_names,
    storage=None,
):
    for directory in directories:
        is_correct = is_correct_file(directory, FILENAMES)

        if is_correct:
            print(directory)
            if storage is not None:
                records = process_path(
                    directory,
                    normalization_values,
                    preprocessing_types,
                    subsets,
                    transformer_names,
                )
                storage += records
                return
