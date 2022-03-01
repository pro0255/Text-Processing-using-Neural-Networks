from src.config.config import (
    PATH_TO_DATASET_FOLDER,
    FILE_DATA_NAME,
    AUTHORS_FILE_NAME,
    NORMALIZATION_SUFFIX,
)
from src.types.dataset import DataSet
from src.types.dataset_type import DataSetType
from src.authors.create_author_directory import create_author_directory
from src.utils.create_path import create_path
from src.types.subset_type import SubsetType
from src.types.suffix import Suffix


def create_label_sub_directory(specific_label_size):
    if specific_label_size is None:
        return None
    return f"{specific_label_size}{NORMALIZATION_SUFFIX}"


def create_path_to_gutenberg_sentence_authors_sentence(
    number_of_authors,
    number_of_sentence,
    path_to_dataset_folder=PATH_TO_DATASET_FOLDER,
    file_name=FILE_DATA_NAME,
    sub_directory=None,
):
    return create_path(
        path_to_dataset_folder,
        DataSet.Gutenberg,
        create_author_directory(number_of_authors),
        DataSetType.Sentence,
        number_of_sentence,
        file_name,
        sub_directory,
    )


def create_path_to_gutenberg_authors(
    number_of_authors,
    number_of_sentence,
    path_to_dataset_folder=PATH_TO_DATASET_FOLDER,
    file_name=AUTHORS_FILE_NAME,
):
    return create_path(
        path_to_dataset_folder,
        DataSet.Gutenberg,
        create_author_directory(number_of_authors),
        DataSetType.Sentence,
        number_of_sentence,
        file_name,
    )


def get_paths_to_gutenberg(
    number_of_authors,
    number_of_sentence,
    path_to_dataset_folder=PATH_TO_DATASET_FOLDER,
):
    authors = create_path_to_gutenberg_authors(
        number_of_authors, number_of_sentence, path_to_dataset_folder
    )
    data = create_path_to_gutenberg_sentence_authors_sentence(
        number_of_authors, number_of_sentence, path_to_dataset_folder
    )

    return data, authors


def create_file_name_from_type(subset_type):
    dic = {
        SubsetType.All: FILE_DATA_NAME,
        SubsetType.Test: f"{SubsetType.Test.value}{Suffix.CSV.value}",
        SubsetType.Train: f"{SubsetType.Train.value}{Suffix.CSV.value}",
        SubsetType.Valid: f"{SubsetType.Valid.value}{Suffix.CSV.value}",
    }
    return dic[subset_type]


def get_path_to_gutenberg_set(
    number_of_authors,
    number_of_sentence,
    subset_type,
    path_to_dataset_folder=PATH_TO_DATASET_FOLDER,
    specific_label_size=None,
):
    path = create_path_to_gutenberg_sentence_authors_sentence(
        number_of_authors,
        number_of_sentence,
        path_to_dataset_folder,
        create_file_name_from_type(subset_type),
        create_label_sub_directory(specific_label_size),
    )
    return path


def get_path_to_gutenberg_all(
    number_of_authors, number_of_sentence, path_to_dataset_folder=PATH_TO_DATASET_FOLDER
):
    authors = create_path_to_gutenberg_authors(
        number_of_authors, number_of_sentence, path_to_dataset_folder
    )
    all_path = get_path_to_gutenberg_set(
        number_of_authors, number_of_sentence, SubsetType.All, path_to_dataset_folder
    )

    return all_path, authors


def get_path_to_gutenberg_sets(
    number_of_authors,
    number_of_sentence,
    path_to_dataset_folder=PATH_TO_DATASET_FOLDER,
    specific_label_size=None,
):
    authors = create_path_to_gutenberg_authors(
        number_of_authors, number_of_sentence, path_to_dataset_folder
    )

    train_path = get_path_to_gutenberg_set(
        number_of_authors,
        number_of_sentence,
        SubsetType.Train,
        path_to_dataset_folder,
        specific_label_size,
    )
    valid_path = get_path_to_gutenberg_set(
        number_of_authors,
        number_of_sentence,
        SubsetType.Valid,
        path_to_dataset_folder,
        specific_label_size,
    )
    test_path = get_path_to_gutenberg_set(
        number_of_authors,
        number_of_sentence,
        SubsetType.Test,
        path_to_dataset_folder,
        specific_label_size,
    )

    # add train, test, valid
    return (train_path, valid_path, test_path), authors
