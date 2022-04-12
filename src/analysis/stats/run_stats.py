import typing
from enum import Enum

import pandas as pd

from src.analysis.stats.config import (NORMALIZATION_VALUES,
                                       PREPROCESSING_TYPES, START_DIRECTORY,
                                       SUBSETS, TRANSFORMER_NAMES)
from src.analysis.stats.process_directory import process_directory
from src.types.processing_type import PreprocessingType
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName


class StatsConfiguration(Enum):
    All = "All"


stats_configurations = {
    StatsConfiguration.All.value: ([None], PREPROCESSING_TYPES, SUBSETS, [None])
}


def run_stats_type(
    directory: str = START_DIRECTORY,
    stats_type: StatsConfiguration = StatsConfiguration.All,
):
    parameters = stats_configurations[stats_type.value]
    return run_stats(directory, *parameters)


def run_stats(
    directory: str = START_DIRECTORY,
    normalization_values: typing.List[int] = NORMALIZATION_VALUES,
    preprocessing_types: typing.List[PreprocessingType] = PREPROCESSING_TYPES,
    subsets: typing.List[SubsetType] = SUBSETS,
    transformer_names: typing.List[
        typing.Union[None, TransformerName]
    ] = TRANSFORMER_NAMES,
):
    storage = list()

    print(normalization_values, preprocessing_types, subsets, transformer_names)
    process_directory(
        directory,
        storage,
        normalization_values,
        preprocessing_types,
        subsets,
        transformer_names,
    )

    df = pd.concat(storage)
    df.index = range(len(df))

    return df
