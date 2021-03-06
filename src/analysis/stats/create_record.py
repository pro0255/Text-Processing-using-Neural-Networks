import os
import time
import typing
import json

import pandas as pd

from src.analysis.stats.build_dictionary_from_wrapper import (
    build_dictionary_from_wrapper,
)
from src.analysis.stats.types.stats_field import StatsField
from src.config.config import AUTHORS_FILE_NAME, BLANK_DESCRIPTION, FILE_DATA_NAME
from src.statistic.build_input_for_statistics import (
    build_input_for_statistics_from_path,
)
from src.statistic.create_statistics_from import create_statistics_from_with_example
from src.statistic.DEFAULT_INSTANCES import build_statistic_instances
from src.types.processing_type import PreprocessingType
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName


def create_record(
    parent_path: str,
    norm_value: int,
    preprocessing_type: PreprocessingType,
    subset_type: SubsetType,
    transformer_name: typing.Union[None, TransformerName],
) -> typing.Type[pd.DataFrame]:
    """Loads data and run statistics which is saved to DataFrame and represent stats values for specific DataSet.

    Args:
        parent_path (str): path which should be processd
        norm_value (int): normalization value, undersample
        preprocessing_type (PreprocessingType): type of preprocessing which should be applied
        subset_type (SubsetType): subsettype which should be used
        transformer_name (typing.Union[None, TransformerName]): name of transformer which should be used

    Returns:
        typing.Type[pd.DataFrame]: DataFrame which represents statistic record for DataSet
    """
    print(
        f"Current {parent_path}, {str(norm_value)}, {preprocessing_type.value}, {subset_type.value}, {BLANK_DESCRIPTION if transformer_name is None else transformer_name.value}\n"
    )
    value = {}

    parts = parent_path.split(os.path.sep)
    path_to_data = os.path.sep.join([parent_path, FILE_DATA_NAME])

    tic = time.time()
    current_stats, text_example = create_statistics_from_with_example(
        *build_input_for_statistics_from_path(
            path_to_data,
            ";",
            build_statistic_instances(
                None if transformer_name is None else transformer_name.value
            ),
            norm_value,
            preprocessing_type,
            subset_type,
        )
    )

    authors_data = pd.read_csv(
        os.path.sep.join([parent_path, AUTHORS_FILE_NAME])
    ).to_dict()

    stats_dictionary = build_dictionary_from_wrapper(current_stats)
    toc = time.time()

    value = {
        StatsField.Path.value: parent_path,
        StatsField.NumberOfAuthors.value: "".join(
            [c for c in parts[-2] if c.isdigit()]
        ),
        StatsField.NumberOfSentences.value: "".join(
            [c for c in parts[-1] if c.isdigit()]
        ),
        StatsField.CalculationTime.value: toc - tic,
        StatsField.PreprocessingType.value: preprocessing_type.value,
        StatsField.NormalizationValue.value: norm_value,
        StatsField.SubsetType.value: subset_type.value,
        StatsField.TransformerName.value: BLANK_DESCRIPTION
        if transformer_name is None
        else transformer_name.value,
        StatsField.Authors.value: authors_data,
        StatsField.TextExample.value: text_example,
        **stats_dictionary,
    }

    return pd.DataFrame.from_dict(value, orient="index").T
