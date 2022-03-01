import pandas as pd
from os.path import exists as file_exists
from src.config.config import BLANK_DESCRIPTION
from src.types.experiment_summarization_fields import ExperimentSummarizationFields
from src.types.experiment_description import ExperimentDescriptionType
from src.types.results import ResultType


def merge_content(confusion_matrix, metrics, description, summarization, directory):
    concat_df = pd.DataFrame()

    for df in [metrics, description, summarization]:
        if df is not None:
            concat_df = pd.concat([concat_df, df])

    keys = concat_df.iloc[:, 0].values
    values = concat_df.iloc[:, 1].values


    if metrics is None:
        print(f"No metrics in {directory}")
        append_keys = [x.value for x in list(ResultType) if x != ResultType.ConsfusionMatrix] 
        keys = keys + append_keys
        values = values + [BLANK_DESCRIPTION] * len(append_keys)

    if description is None:
        print(f"No description in {directory}")
        append_keys = [x.value for x in list(ExperimentDescriptionType)] 
        keys = keys + append_keys
        values = values + [BLANK_DESCRIPTION] * len(append_keys)

    if summarization is None:
        print(f"No summarization in {directory}")
        append_keys = [x.value for x in list(ExperimentSummarizationFields)] 
        keys = keys + append_keys
        values = values + [BLANK_DESCRIPTION] * len(append_keys)

    dic = {k:v for k, v in zip(keys, values)}

    dic['ConfusionMatrix'] = confusion_matrix.values if confusion_matrix is not None else BLANK_DESCRIPTION
    dic['Directory'] = directory
    

    record = pd.DataFrame.from_dict(dic, orient='index').T

    return record