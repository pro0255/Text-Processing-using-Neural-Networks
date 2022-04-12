import os
import typing

from src.analysis.experiments.validation.is_correct_file import is_correct_file
from src.analysis.stats.config import FILENAMES, START_DIRECTORY
from src.analysis.stats.process_path import process_path
from src.types.processing_type import PreprocessingType
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName


def load_paths(directory: str=START_DIRECTORY, storage: typing.Union[typing.List, None]=None):
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
    directories: typing.List[str],
    normalization_values: typing.List[int],
    preprocessing_types: typing.List[PreprocessingType],
    subsets: typing.List[SubsetType],
    transformer_names: typing.List[typing.Union[TransformerName, None]],
    storage: typing.Union[typing.List, None]=None,
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
