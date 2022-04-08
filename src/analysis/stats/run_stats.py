from src.analysis.stats.config import START_DIRECTORY 
from src.analysis.stats.process_directory import process_directory 
from src.analysis.stats.config import NORMALIZATION_VALUES, PREPROCESSING_TYPES, SUBSETS, TRANSFORMER_NAMES
import pandas as pd
from enum import Enum

class StatsConfiguration(Enum):
    All = "All"



stats_configurations = {
    StatsConfiguration.All.value: (
        [None],
        PREPROCESSING_TYPES,
        SUBSETS,
        TRANSFORMER_NAMES
    )
}


def run_stats_type(directory=START_DIRECTORY, stats_type=StatsConfiguration):
    parameters = stats_configurations[stats_type.value]
    return run_stats(directory, *parameters)


def run_stats(directory=START_DIRECTORY, normalization_values=NORMALIZATION_VALUES, preprocessing_types=PREPROCESSING_TYPES, subsets=SUBSETS, transformer_names=TRANSFORMER_NAMES):
    storage = list()
    
    print(normalization_values, preprocessing_types, subsets, transformer_names)
    process_directory(directory, storage, normalization_values, preprocessing_types, subsets, transformer_names)

    df = pd.concat(storage)
    df.index = range(len(df))

    return df