import typing
from src.config.config import (NORMALIZATION_SUFFIX, TEST_SIZE, TRAIN_SIZE,
                               VALIDATION_SIZE)
from src.data_loading.get_dataset_object_from import \
    get_dataset_object_from_path
from src.data_preparing.split.DataSetSplitter import DataSetSplitter
from src.utils.check_dataset_sizes import check_dataset_sizes


def create_subdirectory_name(normalization_size: int):
    if normalization_size is None:
        return None

    return f"{normalization_size}{NORMALIZATION_SUFFIX}"


def split_file_to_train_test_valid(
    path_to_load: str,
    path_to_save: str,
    label_metric=None,
    normalization_size:typing.Union[None, int]=None,
    train_size: int=TRAIN_SIZE,
    test_size: int=TEST_SIZE,
    valid_size:int=VALIDATION_SIZE,
):
    check_dataset_sizes(train_size, test_size, valid_size)

    splitter = DataSetSplitter(
        path_to_save,
        train_size,
        test_size,
        valid_size,
        label_metric,
        normalization_size,
        create_subdirectory_name(normalization_size),
    )

    dataset = get_dataset_object_from_path(path_to_load, ";", None)
    splitter.build_subsets(dataset)
