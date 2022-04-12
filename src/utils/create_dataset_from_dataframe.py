import typing

import tensorflow as tf
from pandas import DataFrame

from src.config.config import LABEL_COLUMN, TEXT_COLUMN


def create_dataset_from_dataframe(dataframe: typing.Type[DataFrame]):
    features, target = dataframe[TEXT_COLUMN], dataframe[LABEL_COLUMN]
    return create_dataset_from_Xy(features, target)


def create_dataset_from_Xy(X, y):
    return tf.data.Dataset.from_tensor_slices((X, y))
