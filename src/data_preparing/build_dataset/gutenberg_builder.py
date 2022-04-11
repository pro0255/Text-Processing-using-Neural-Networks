import os

from authors.authors_generator import authors_generator
from src.config.config import (GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS,
                               GUTENBERG_DOWNLOADED_DIRECTORY, PATTERN)
from src.data_loading.iterate_over_files import iterate_over_files
from src.data_preparing.build_dataset.build_process_func import build_process_func
from src.types.dataset_type import DataSetType


class gutenberg_builder:
    def __init__(self) -> None:
        self.author_generator = authors_generator()

    def build_dataset(
        self,
        number_of_sentences,
        number_of_authors,
        load_path=os.sep.join([GUTENBERG_DOWNLOADED_DIRECTORY, PATTERN]),
        directory_to_save=GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS,
    ):
        iterate_over_files(
            load_path,
            build_process_func(
                number_of_sentences,
                DataSetType.Sentence.value + str(number_of_sentences),
                directory_to_save,
                self.author_generator.generate_top_k(number_of_authors),
            ),
        )
