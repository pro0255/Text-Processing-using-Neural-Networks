import typing
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from src.config.config import (LABEL_COLUMN, RANDOM_STATE, TEST_SIZE,
                               TEXT_COLUMN, VALIDATION_SIZE)


def split_dataframe(dataframe: typing.Type[DataFrame], test_size:float=TEST_SIZE):
    features, target = dataframe[TEXT_COLUMN], dataframe[LABEL_COLUMN]
    return train_test_split(features, target, test_size=test_size)


def split_dataframe_to_train_test_valid(
    dataframe:typing.Type[DataFrame], test_size: float=TEST_SIZE, valid_size: float=VALIDATION_SIZE
):
    features, target = dataframe[TEXT_COLUMN], dataframe[LABEL_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=test_size, random_state=RANDOM_STATE
    )
    X_train, X_valid, y_train, y_valid = train_test_split(
        X_train, y_train, test_size=valid_size, random_state=RANDOM_STATE
    )

    print(f"Train {X_train.shape}")
    print(f"Valid {X_valid.shape}")
    print(f"Test {X_test.shape}")

    return X_train, X_valid, X_test, y_train, y_valid, y_test
