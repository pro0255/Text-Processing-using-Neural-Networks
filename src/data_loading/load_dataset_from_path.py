import pandas as pd
from collections.abc import Callable

from src.config.config import LABEL_COLUMN, PROJECT_CSV_DELIMITER, TEXT_COLUMN
from src.preprocessing.preprocessing_factory import (
    PreprocessingFactory,
    PreprocessingType,
)


def load_dataset_from_path_with_normalization(
    path: str, normalize: Callable[[str], str] = None, preprocessing_type=None
):
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
