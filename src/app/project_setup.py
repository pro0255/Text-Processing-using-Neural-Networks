import itertools
import os

from src.config.config import (FILE_DATA_NAME,
                               GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS)
from src.data_preparing.build_dataset.gutenberg_builder import gutenberg_builder
from src.data_preparing.split.run_split_deps_on_stats import \
    run_split_deps_on_stats_same_dir

AUTHORS = list(range(5, 115, 10))
SENTENCES = list(range(1, 11, 1))


class ProjectSetup:
    def __init__(self) -> None:
        self.builder = gutenberg_builder()
        self.combs = None

    def create_combs(self) -> None:
        self.combs = list(itertools.product(SENTENCES, AUTHORS))

    def create_all_datasets(self) -> None:
        if self.combs is None:
            assert Exception("Cannot create before calculation all of combinations...!")
            return

        for number_of_sentences, number_of_authors in self.combs:
            self.builder.build_dataset(number_of_sentences, number_of_authors)

    def create_datasets(self, sentences, from_authors, to_authors, step=10) -> None:
        combs = list(
            itertools.product([sentences], list(range(from_authors, to_authors, step)))
        )
        print(f"Current combinations {combs}")
        for number_of_sentences, number_of_authors in combs:
            self.builder.build_dataset(number_of_sentences, number_of_authors)

    def split_datasets(self) -> None:
        for dir in os.listdir(GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS):
            for nested_dir in os.listdir(
                os.path.sep.join([GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS, dir])
            ):
                path = os.path.sep.join(
                    [
                        GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS,
                        dir,
                        nested_dir,
                        FILE_DATA_NAME,
                    ]
                )
                run_split_deps_on_stats_same_dir(path)

    def setup_datasets(self) -> None:
        self.create_datasets()
        self.split_datasets()
