from src.config.config import TRAIN_SIZE, TEST_SIZE, VALIDATION_SIZE, AUTHORS_FILE_NAME
from src.utils.check_dataset_sizes import check_dataset_sizes
from src.statistic.build_input_for_statistics import build_input_for_statistics
from src.statistic.create_statistics_from import create_statistics_from
from src.statistic.instances.label_metric import LabelMetric
from src.data_preparing.split.split_file_to_train_test_valid import (
    split_file_to_train_test_valid,
)
import os
import pandas as pd
from src.types.authors_columns import AuthorsColumns


def run_split_deps_on_stats(
    path_to_load,
    path_to_save,
    normalization=True,
    specific_label_size=None,
    train_size=TRAIN_SIZE,
    test_size=TEST_SIZE,
    valid_size=VALIDATION_SIZE,
):
    check_dataset_sizes(train_size, test_size, valid_size)

    label_metric = None
    if specific_label_size is None:
        print("Starting to build statistics")
        metric_instance = create_statistics_from(
            *build_input_for_statistics(
                path_to_load, ";", None, [LabelMetric()], None, False
            )
        )
        label_metric = metric_instance.metric_instances[0].get_dataframe()
        print("End of statistics")
    else:
        path_parts = path_to_load.split(os.path.sep)
        del path_parts[-1]
        path_parts.append(AUTHORS_FILE_NAME)
        authors = pd.read_csv(os.path.sep.join(path_parts), sep=";")
        label_metric = pd.DataFrame.from_dict(
            {
                author_id: specific_label_size
                for author_id in authors[AuthorsColumns.AuthorId.value]
            },
            orient="index",
        )

    number_of_min_label = None

    if normalization:
        sorted_label_metric_frame = label_metric.sort_values(by=0)
        number_of_min_label = sorted_label_metric_frame.iloc[0][0]

    if not normalization and specific_label_size is not None:
        number_of_min_label = specific_label_size

    split_file_to_train_test_valid(
        path_to_load, path_to_save, label_metric, number_of_min_label
    )
    print("Splitting finished!")


def run_split_deps_on_stats_same_dir(
    path_to_load, normalization=True, specific_label_size=None
):
    run_split_deps_on_stats(
        path_to_load,
        os.path.sep.join(path_to_load.split(os.path.sep)[0:-1]),
        normalization,
        specific_label_size,
    )
