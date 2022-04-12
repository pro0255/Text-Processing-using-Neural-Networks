import typing
import pandas as pd
import tensorflow as tf
from src.config.config import LABEL_COLUMN, TEXT_COLUMN


def from_dataset_array(dataset: typing.Type[tf.data.Dataset]):
    X, y = [], []

    for x in dataset.as_numpy_iterator():
        text, label = x
        text = bytes.decode(text)
        X.append(text)
        y.append(label)

    return X, y


def from_dataset_dataframe(
    dataset: typing.Type[tf.data.Dataset],
) -> typing.Type[pd.DataFrame]:
    X, y = from_dataset_array(dataset)

    df = pd.DataFrame()
    df[TEXT_COLUMN] = X
    df[LABEL_COLUMN] = y

    return df
