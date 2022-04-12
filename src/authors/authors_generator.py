import typing

import pandas as pd

from src.config.config import ALL_AUTHORS_DELIMITER, PATH_TO_ALL_AUTHORS


class authors_generator:
    def __init__(
        self, path: str = PATH_TO_ALL_AUTHORS, sep: str = ALL_AUTHORS_DELIMITER
    ) -> None:
        self.path = path
        self.sep = sep

    def generate_top_k(self, k: int) -> typing.List[typing.Tuple[int, str]]:
        data = pd.read_csv(self.path, sep=self.sep)
        rows = data.shape[0]
        authors_ids = data.iloc[0 : rows - 1, 0].astype(int).values[0:k]
        authors_names = data.iloc[0 : rows - 1, 1].astype(str).values[0:k]
        authors_tuple = list(zip(authors_ids, authors_names))
        del data
        return authors_tuple
