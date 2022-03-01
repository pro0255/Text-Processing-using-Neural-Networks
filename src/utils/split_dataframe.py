from sklearn.model_selection import train_test_split
from src.config.config import LABEL_COLUMN, TEXT_COLUMN
from src.config.config import TEST_SIZE


def split_dataframe(dataframe, test_size=TEST_SIZE):
    features, target = dataframe[TEXT_COLUMN], dataframe[LABEL_COLUMN]
    return train_test_split(features, target, test_size=test_size)
