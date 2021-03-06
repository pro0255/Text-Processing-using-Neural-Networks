import itertools
import typing

from src.data_loading.get_dataset_object_from import get_dataset_all
from src.data_loading.load_dataset_from_path import (
    load_dataset_from_path_with_normalization,
)
from src.experiments.experiment_scripts.neural_nets.use_lookup import (
    use_lookup_normalization,
)
from src.utils.normalize_dataframe_to_size import normalize_dataframe_to_size
from src.utils.split_dataframe import split_dataframe_to_train_test_valid


class ExperimentLoader:
    def __init__(self) -> None:
        pass

    def create_dataset_generator(
        self,
        number_of_authors: typing.List[int],
        number_of_sentences: typing.List[int],
        preprocessing_types: typing.List,
        norm_sizes: typing.List[int],
    ):
        """According to parameters create generator, where is loaded csv, normalized, and splitted to train, test and valid.

        Args:
            number_of_authors (typing.List[int]): number of authors which should be loaded
            number_of_sentences (typing.List[int]): number of sentences which should be loaded
            preprocessing_types (typing.List): types of preprocessing which should be used
            norm_sizes (typing.List[int]): integer value with descriptions of normalization value

        Yields:
            _type_: generates value descriptions of loaded data and splitted data train, test, valid
        """

        load_configs = list(
            itertools.product(
                number_of_authors, number_of_sentences, preprocessing_types, norm_sizes
            )
        )

        for conf in load_configs:
            current_authors, current_sentences, current_preprocessing, norm_size = conf
            norm_size = use_lookup_normalization(
                norm_size, current_authors, current_sentences
            )
            if norm_size is None:
                print("Look up does not exists!")
                yield None

            _, paths = get_dataset_all(current_authors, current_sentences)
            data_path, author_path = paths
            loaded_data = load_dataset_from_path_with_normalization(
                data_path, None, current_preprocessing
            )
            normalized_loaded_data = normalize_dataframe_to_size(loaded_data, norm_size)
            (
                X_train,
                X_valid,
                X_test,
                y_train,
                y_valid,
                y_test,
            ) = split_dataframe_to_train_test_valid(normalized_loaded_data)

            yield (
                X_train,
                X_valid,
                X_test,
                y_train,
                y_valid,
                y_test,
            ), loaded_data, paths, conf
