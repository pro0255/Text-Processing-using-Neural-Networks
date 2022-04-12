import typing
import pandas as pd

from src.analysis.experiments.process_directory import process_directory


def create_dataframe(
    start_directory: str, storage: typing.Union[typing.List, None] = None
) -> None:
    return process_directory(start_directory, storage)


class Storage:
    def __init__(self):
        self.records = []

    def reset(self):
        self.records = []

    def run(self, directory: typing.Union[str, None] = None):
        self.directory = directory

        if self.directory is None:
            return

        create_dataframe(self.directory, self.records)

    def get_dataframe(self):
        return pd.concat(self.records)
