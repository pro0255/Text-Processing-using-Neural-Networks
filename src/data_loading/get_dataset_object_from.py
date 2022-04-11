import typing
import tensorflow as tf

from src.preprocessing.preprocessing_factory import (PreprocessingFactory,
                                                     PreprocessingType)
from src.utils.create_path_to_gutenberg import (get_path_to_gutenberg_all,
                                                get_path_to_gutenberg_sets)

def get_dataset_object_from_path(csv_filename: str, delim: str, text_pipeline_func: typing.Union[None, typing.Callable[[str], str]]=None):
    print(f"Loading dataset from={csv_filename}")
    dataset = tf.data.TextLineDataset(filenames=csv_filename)

    def parse_csv(line):
        csv_line = bytes.decode(line.numpy())
        text, author = csv_line.split(delim)
        if text_pipeline_func is not None:
            text = text_pipeline_func(text)
        return text, int(author)

    dataset = dataset.map(
        lambda tpl: tf.py_function(parse_csv, [tpl], [tf.string, tf.int32])
    )

    return dataset


def get_datasets(csv_filenames: str, delim: str, text_pipeline_func:typing.Union[None, typing.Callable[[str], str]]=None):
    datasets = [
        get_dataset_object_from_path(csv_filename, delim, text_pipeline_func)
        for csv_filename in csv_filenames
    ]
    return datasets


def get_datasets_for_split(number_of_authors:int, number_of_sentences:int):
    path_data, path_authors = get_path_to_gutenberg_sets(
        number_of_authors, number_of_sentences
    )
    factory = PreprocessingFactory()
    train, valid, test = get_datasets(
        path_data, ";", factory.create(PreprocessingType.Default)
    )
    return (train, valid, test), (path_data, path_authors)


def get_dataset_all(number_of_authors:int, number_of_sentences:int):
    path_data, path_authors = get_path_to_gutenberg_all(
        number_of_authors, number_of_sentences
    )
    all_data = get_datasets([path_data], ";", None)
    return (all_data), (path_data, path_authors)
