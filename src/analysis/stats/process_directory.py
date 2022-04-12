import os
import typing

from src.analysis.experiments.validation.is_correct_file import is_correct_file
from src.analysis.stats.config import (FILENAMES, NORMALIZATION_VALUES,
                                       PREPROCESSING_TYPES, SUBSETS,
                                       TRANSFORMER_NAMES)
from src.analysis.stats.process_path import process_path
from src.types.processing_type import PreprocessingType
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName


def process_directory(
    directory: str,
    storage:typing.Union[typing.List, None]=None,
    normalization_values: typing.List[int]=NORMALIZATION_VALUES,
    preprocessing_types: typing.List[PreprocessingType]=PREPROCESSING_TYPES,
    subsets: typing.List[SubsetType]=SUBSETS,
    transformer_names: typing.List[typing.Union[TransformerName, None]]=TRANSFORMER_NAMES,
):
    for current_directory in os.listdir(directory):

        is_correct = is_correct_file(directory, FILENAMES)

        if is_correct:
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

        deeper_level = os.path.sep.join([directory, current_directory])
        if os.path.isdir(deeper_level):
            process_directory(
                deeper_level,
                storage,
                normalization_values,
                preprocessing_types,
                subsets,
                transformer_names,
            )
