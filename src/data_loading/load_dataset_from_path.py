from collections.abc import Callable

import pandas as pd

from src.config.config import LABEL_COLUMN, PROJECT_CSV_DELIMITER, TEXT_COLUMN
from src.preprocessing.preprocessing_factory import (
    PreprocessingFactory,
    PreprocessingType,
)


def load_dataset_from_path_with_normalization(
    path: str, normalize: Callable[[str], str] = None, preprocessing_type=None
):
    """Helper method which loads data and normalize them according to preprocessing type or specified method.

    Args:
        path (str): path to data which should be loaded
        normalize (Callable[[str], str], optional): method which is called when preprocessing type is not specified. Defaults to None.
        preprocessing_type (_type_, optional): according this type is used PreprocessingType and called method for preprocessing text data. Defaults to None.

    Returns:
        _type_: DataFrame with two columns Label and Text which describes data for experiment or analysis
    """
    factory = PreprocessingFactory()

    normalize_final = None

    if normalize is not None:
        print("Specified normalize method")
        normalize_final = normalize
    else:
        print(f"Specified type {preprocessing_type.value}")
        if preprocessing_type is None:
            normalize_final = factory.create(PreprocessingType.Default)
        else:
            normalize_final = factory.create(preprocessing_type)

    dataset = load_dataset_from_path(path)
    dataset[TEXT_COLUMN] = dataset[TEXT_COLUMN].apply(normalize_final)
    return dataset


def load_dataset_from_path(path):
    dataset = pd.read_csv(path, sep=PROJECT_CSV_DELIMITER, header=None)
    dataset.columns = [TEXT_COLUMN, LABEL_COLUMN]
    return dataset
