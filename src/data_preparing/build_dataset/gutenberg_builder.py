import os

from src.authors.authors_generator import authors_generator
from src.config.config import (
    GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS,
    GUTENBERG_DOWNLOADED_DIRECTORY,
    PATTERN,
)
from src.data_loading.iterate_over_files import iterate_over_files
from src.data_preparing.build_dataset.build_process_func import build_process_func
from src.types.dataset_type import DataSetType


class gutenberg_builder:
    """Helper class which builds dataset according to input arguments."""

    def __init__(self) -> None:
        self.author_generator = authors_generator()

    def build_dataset(
        self,
        number_of_sentences: int,
        number_of_authors: int,
        load_path: str = os.sep.join([GUTENBERG_DOWNLOADED_DIRECTORY, PATTERN]),
        directory_to_save: str = GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS,
    ):
        """Function which starts to build dataset. It gonna iterate over specified directory of downloaded .json files. And one after one .json file is handled by build_process_func.

        Args:
            number_of_sentences (int): number of senteces (chunk parameter)
            number_of_authors (int): number of authors whos should be in dataset
            load_path (str, optional): path where is situated .json files. Defaults to os.sep.join([GUTENBERG_DOWNLOADED_DIRECTORY, PATTERN]).
            directory_to_save (str, optional): path where should be saved data. Defaults to GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS.
        """
        iterate_over_files(
            load_path,
            build_process_func(
                number_of_sentences,
                DataSetType.Sentence.value + str(number_of_sentences),
                directory_to_save,
                self.author_generator.generate_top_k(number_of_authors),
            ),
        )
