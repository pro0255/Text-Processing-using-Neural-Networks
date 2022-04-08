import time
import os
from src.statistic.create_statistics_from import create_statistics_from
from src.statistic.build_input_for_statistics import build_input_for_statistics_from_path
from src.statistic.DEFAULT_INSTANCES import build_statistic_instances
from src.analysis.stats.build_dictionary_from_wrapper import build_dictionary_from_wrapper
import pandas as pd
from src.analysis.stats.types.stats_field import StatsField 
from src.config.config import FILE_DATA_NAME, AUTHORS_FILE_NAME


def create_record(parent_path, norm_value, preprocessing_type, subset_type, transformer_name):
    print(f"Current {parent_path}, {str(norm_value)}, {preprocessing_type.value}, {subset_type.value}, {transformer_name.value}\n" )
    value = {}
    
    parts = parent_path.split(os.path.sep)
    path_to_data = os.path.sep.join([parent_path, FILE_DATA_NAME])



    tic = time.time()
    current_stats = create_statistics_from(
        *build_input_for_statistics_from_path(
            path_to_data,
            ";",
            build_statistic_instances(transformer_name.value),
            norm_value,
            preprocessing_type,
            subset_type,
        )
    )

    authors_data = pd.read_csv(os.path.sep.join([parent_path, AUTHORS_FILE_NAME])).to_dict()
    
    stats_dictionary = build_dictionary_from_wrapper(current_stats)
    toc = time.time()
    
    value = {
        StatsField.Path.value: parent_path,
        StatsField.NumberOfAuthors.value: "".join([c for c in parts[-3] if c.isdigit()]),
        StatsField.NumberOfSentences.value: "".join([c for c in parts[-2] if c.isdigit()]),
        StatsField.CalculationTime.value: toc - tic,
        StatsField.PreprocessingType.value: preprocessing_type.value,
        StatsField.NormalizationValue.value: norm_value,
        StatsField.SubsetType.value: subset_type.value,
        StatsField.TransformerName.value: transformer_name.value,
        StatsField.Authors.value: authors_data,
        **stats_dictionary
    }
    
    
    return pd.DataFrame.from_dict(value, orient="index").T