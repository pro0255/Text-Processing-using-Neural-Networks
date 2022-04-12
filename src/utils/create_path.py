import os
import typing

from src.config.config import FILE_DATA_NAME
from src.types.dataset_type import DataSetType
from src.types.dataset import DataSet


# TODO: refactor
def create_sentence_path(
    directory: str,
    dataset: DataSet,
    authors_directory: str,
    dataset_type: DataSetType,
    k: typing.Union[None, int] = None,
    file_name: str = FILE_DATA_NAME,
    sub_directory: typing.Union[None, str] = None,
) -> str:
    if sub_directory is None:
        return os.path.join(
            directory,
            dataset.value,
            authors_directory,
            dataset_type.value + str(k),
            file_name,
        )

    return os.path.join(
        directory,
        dataset.value,
        authors_directory,
        dataset_type.value + str(k),
        sub_directory,
        file_name,
    )


def create_article_path(
    directory: str,
    dataset: DataSet,
    authors_directory: str,
    dataset_type: DataSetType,
    k: typing.Union[None, int] = None,
    file_name: str = FILE_DATA_NAME,
    sub_directory: typing.Union[None, str] = None,
) -> str:
    if sub_directory is None:
        return os.path.join(
            directory, dataset.value, authors_directory, dataset_type.value, file_name
        )
    return os.path.join(
        directory,
        dataset.value,
        authors_directory,
        dataset_type.value,
        sub_directory,
        file_name,
    )


def create_path(
    directory: str,
    dataset: DataSet,
    authors_directory: str,
    dataset_type: DataSetType,
    k: typing.Union[None, int] = None,
    file_name: str = FILE_DATA_NAME,
    sub_directory: typing.Union[None, str] = None,
) -> str:
    is_sentence_type = dataset_type == DataSetType.Sentence
    if is_sentence_type and k is None:
        raise Exception(f"Sentence should be specified with k argument!")

    return (
        create_sentence_path(
            directory,
            dataset,
            authors_directory,
            dataset_type,
            k,
            file_name,
            sub_directory,
        )
        if is_sentence_type
        else create_article_path(
            directory,
            dataset,
            authors_directory,
            dataset_type,
            k,
            file_name,
            sub_directory,
        )
    )
