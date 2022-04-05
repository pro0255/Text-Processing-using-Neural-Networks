from src.config.config import LABEL_COLUMN, RANDOM_STATE
import pandas as pd
from sklearn.utils import shuffle


def normalize_dataframe_to_size(dataframe, size):
    all_labels = dataframe[LABEL_COLUMN].unique()
    new_dataframe = pd.DataFrame()

    for label in all_labels:
        selected_dataframe = dataframe[dataframe.label == label].sample(size, random_state=RANDOM_STATE)
        new_dataframe = pd.concat([new_dataframe, selected_dataframe])

    return shuffle(new_dataframe, random_state=RANDOM_STATE)