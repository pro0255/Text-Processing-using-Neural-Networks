import pandas as pd

from src.config.config import BLANK_DESCRIPTION
from src.types.experiment_description import ExperimentDescriptionType
from src.types.experiment_summarization_fields import ExperimentSummarizationFields
from src.types.results import ResultType


def merge_content(
    confusion_matrix, metrics, description, summarization, directory, logs
):
    """Merge all files to one record.

    Args:
        confusion_matrix (_type_): confusion matrix.csv
        metrics (_type_): metrics.csv
        description (_type_): ExperimentDescription ... description.csv
        summarization (_type_): ExperimentSummarization ... summarization.csv
        directory (_type_): directory
        logs (_type_): log.csv

    Returns:
        _type_: DataFrame which represents experiment
    """
    concat_df = pd.DataFrame()

    for df in [metrics, description, summarization, logs]:
        if df is not None:
            concat_df = pd.concat([concat_df, df])

    keys = concat_df.loc[:, "id"]
    values = concat_df.loc[:, "value"]

    if metrics is None:
        print(f"No metrics in {directory}")
        append_keys = [
            x.value for x in list(ResultType) if x != ResultType.ConsfusionMatrix
        ]
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

    dic = {k: v for k, v in zip(keys, values)}

    dic["ConfusionMatrix"] = (
        confusion_matrix.values if confusion_matrix is not None else BLANK_DESCRIPTION
    )
    dic["Directory"] = directory

    record = pd.DataFrame.from_dict(dic, orient="index").T

    return record
