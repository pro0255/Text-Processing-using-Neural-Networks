import os
from src.analysis.experiments.validation.is_correct_file import is_correct_file
from src.analysis.stats.config import FILENAMES, NORMALIZATION_VALUES, PREPROCESSING_TYPES, SUBSETS, TRANSFORMER_NAMES
from src.analysis.stats.process_path import process_path

def process_directory(directory, storage=None, normalization_values=NORMALIZATION_VALUES, preprocessing_types=PREPROCESSING_TYPES, subsets=SUBSETS, transformer_names=TRANSFORMER_NAMES):
    for current_directory in os.listdir(directory):
        
        is_correct = is_correct_file(directory, FILENAMES)

        if is_correct:
            if storage is not None:
                records = process_path(directory, normalization_values, preprocessing_types, subsets, transformer_names)
                storage += records
                return


        deeper_level = os.path.sep.join([directory, current_directory])
        if os.path.isdir(deeper_level):
            process_directory(deeper_level, storage, normalization_values, preprocessing_types, subsets, transformer_names)