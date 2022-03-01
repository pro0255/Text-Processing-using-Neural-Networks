from sklearn import preprocessing
import pandas as pd
from src.types.authors_columns import AuthorsColumns


def create_encoder_from_path(path):
    authors = pd.read_csv(path, sep=";")
    ids = authors[AuthorsColumns.AuthorId.value].values
    encoder = preprocessing.LabelEncoder()
    encoder.fit(ids)
    return encoder
