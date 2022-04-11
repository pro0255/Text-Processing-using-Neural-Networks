import csv
import os

import pandas as pd

from src.config.config import (AUTHORS_FILE_NAME, FILE_DATA_NAME,
                               PROJECT_CSV_DELIMITER)
from src.data_preparing.build_dataset.chunk_document_by_sentence import \
    chunk_document_by_sentence
from src.data_preparing.build_dataset.logger import log_error
from src.types.gutenberg_json_attributes import GutenbergJsonAttributes
from src.types.label_type import GutenbergLabelType
from src.utils.get_data_from_gutenberg import get_data_from_gutenberg


def build_process_func(k, name, path, authors_tuple):
    number_of_authors = len(authors_tuple)
    authors_ids, authors_names = zip(*authors_tuple)

    directory_for_file = os.sep.join(
        [path, f"{number_of_authors}{GutenbergLabelType.Authors.value}", name]
    )

    if not os.path.exists(directory_for_file):
        os.makedirs(directory_for_file)

    authors_dataframe = pd.DataFrame.from_dict(
        {
            GutenbergJsonAttributes.AuthorId.value: authors_ids,
            GutenbergJsonAttributes.Author.value: authors_names,
        },
    )

    name_of_authors_file = AUTHORS_FILE_NAME
    authors_save = os.sep.join([directory_for_file, name_of_authors_file])

    print(f"Saving authors csv to {authors_save}")

    authors_dataframe.to_csv(authors_save, index=False, sep=";")

    def process_to_create_dataset(data):
        # current_author = data[GutenbergJsonAttributes.Author.value][0]
        try:
            current_gutenberg_id = get_data_from_gutenberg(
                data, GutenbergJsonAttributes.Id.value
            )
            current_text = get_data_from_gutenberg(
                data, GutenbergJsonAttributes.Text.value
            )
            current_author_id = get_data_from_gutenberg(
                data, GutenbergJsonAttributes.AuthorId.value
            )

            is_required_author = current_author_id in authors_ids

            print(current_gutenberg_id)
            if is_required_author:

                chunked_sentences = chunk_document_by_sentence(current_text, k)

                name_of_file = FILE_DATA_NAME
                full_path = os.sep.join([directory_for_file, name_of_file])

                with open(full_path, "a", newline="") as f:
                    writer = csv.writer(f, delimiter=PROJECT_CSV_DELIMITER)

                    for chunk in chunked_sentences:
                        value = [chunk, current_author_id]
                        writer.writerow(value)

                return chunked_sentences
            return []
        except Exception as e:
            log_error(
                directory_for_file,
                get_data_from_gutenberg(data, GutenbergJsonAttributes.Id.value),
                e,
            )
            print(f"Oops error! {e}")
            return []

    return process_to_create_dataset
