from src.utils.create_path_to_gutenberg import (
    create_path_to_gutenberg_sentence_authors_sentence,
)
import pandas as pd
import os
from src.config.config import AUTHORS_FILE_NAME, TEST_DIR, FILE_DATA_NAME
import csv
from src.data_loading.get_dataset_object_from import get_dataset_object_from_path
import numpy as np


def create_test_dataset_from(number_of_authors, number_of_sentences, size):

    path = create_path_to_gutenberg_sentence_authors_sentence(
        number_of_authors, number_of_sentences
    )
    sep_path = path.split(os.path.sep)
    from_path = sep_path[-3:-1]
    del sep_path[-1]
    sep_path.append(AUTHORS_FILE_NAME)
    sep_path = os.path.sep.join(sep_path)
    authors = pd.read_csv(sep_path, sep=";")
    ids = authors.iloc[:, 0].values

    counter = {id: size for id in ids}
    dataset = get_dataset_object_from_path(path, ";", None)

    directory_to_save = TEST_DIR + os.path.sep + os.path.sep.join(from_path)

    if not os.path.exists(directory_to_save):
        os.makedirs(directory_to_save)

    path_to_save = directory_to_save + os.path.sep + FILE_DATA_NAME

    allowed_ids = list(counter.keys())

    for line in dataset.shuffle(10000).as_numpy_iterator():
        if np.sum(list(counter.values())) == 0:
            print("Finished")
            print(counter)
            break

        text, label = line

        text = bytes.decode(text)
        label = int(bytes.decode(label))

        is_in = label in allowed_ids

        if is_in and counter[label] > 0:
            counter[label] -= 1

            with open(path_to_save, "a", newline="") as f:
                writer = csv.writer(f, delimiter=";")
                value = [text, label]
                writer.writerow(value)

    print("Finished")
    print(counter)
