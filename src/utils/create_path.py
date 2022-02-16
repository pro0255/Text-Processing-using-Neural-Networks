from src.types.dataset_type import DataSetType
import os
from src.config.config import FILE_DATA_NAME


#TODO: refactor
def create_sentence_path( 
    directory, 
    dataset, 
    authors_directory, 
    dataset_type, 
    k=None, 
    file_name=FILE_DATA_NAME,
    sub_directory=None
):
    if sub_directory is None:
        return os.path.join(
            directory, 
            dataset.value, 
            authors_directory, 
            dataset_type.value + str(k), 
            file_name
        )

    return os.path.join(
        directory, 
        dataset.value, 
        authors_directory, 
        dataset_type.value + str(k), 
        sub_directory,
        file_name
    )



def create_article_path(
    directory, 
    dataset, 
    authors_directory, 
    dataset_type, 
    k=None, 
    file_name=FILE_DATA_NAME,
    sub_directory=None
):
    if sub_directory is None:
         return os.path.join(
             directory, 
             dataset.value, 
             authors_directory, 
             dataset_type.value,
             file_name
         )
    return os.path.join(
        directory, 
        dataset.value, 
        authors_directory, 
        dataset_type.value, 
        sub_directory, 
        file_name
    )


def create_path(
    directory, 
    dataset, 
    authors_directory, 
    dataset_type, 
    k=None, 
    file_name=FILE_DATA_NAME,
    sub_directory=None
):
    is_sentence_type = dataset_type == DataSetType.Sentence 
    if is_sentence_type and k is None:
        raise Exception(f"Sentence should be specified with k argument!")
    
    return create_sentence_path(directory, dataset, authors_directory, dataset_type, k, file_name, sub_directory) if is_sentence_type else create_article_path(directory, dataset, authors_directory, dataset_type, k, file_name, sub_directory)

