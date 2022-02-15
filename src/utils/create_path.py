from src.types.dataset_type import DataSetType
import os
from src.config.config import FILE_DATA_NAME



def create_path(directory, dataset, authors_directory, dataset_type, k=None, file_name=FILE_DATA_NAME):
    is_sentence_type = dataset_type == DataSetType.Sentence 
    if is_sentence_type and k is None:
        raise Exception(f"Sentence should be specified with k argument!")
    
    return os.path.join(directory, dataset.value, authors_directory, dataset_type.value + str(k), file_name) if is_sentence_type else os.path.join(directory, dataset.value, authors_directory, dataset_type.value, file_name)