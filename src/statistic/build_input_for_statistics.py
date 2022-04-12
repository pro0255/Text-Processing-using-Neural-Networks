import os

from src.config.config import (
    LABEL_COLUMN,
    SPECIFIC_DIRECTORY_FOR_STATISTICS,
    STATISTICS_SUBDIRECTORY,
    TEXT_COLUMN,
)
from src.data_loading.get_dataset_object_from import get_dataset_object_from_path
from src.data_loading.load_dataset_from_path import (
    load_dataset_from_path_with_normalization,
)
from src.statistic.create_stats_filename import create_stats_filename
from src.statistic.DEFAULT_INSTANCES import build_default_instances
from src.statistic.metric_wrapper import MetricWrapper
from src.types.subset_type import SubsetType
from src.utils.create_dataset_from_dataframe import create_dataset_from_Xy
from src.utils.normalize_dataframe_to_size import normalize_dataframe_to_size
from src.utils.split_dataframe import split_dataframe_to_train_test_valid


def get_datset_from_type(subset_type, normalized_data):
    if SubsetType.All == subset_type:
        features, target = normalized_data[TEXT_COLUMN], normalized_data[LABEL_COLUMN]
        return create_dataset_from_Xy(features, target)
    else:
        (
            X_train,
            X_valid,
            X_test,
            y_train,
            y_valid,
            y_test,
        ) = split_dataframe_to_train_test_valid(normalized_data)

        if subset_type == SubsetType.Test:
            return create_dataset_from_Xy(X_test, y_test)
        elif subset_type == SubsetType.Train:
            return create_dataset_from_Xy(X_train, y_train)
        elif subset_type == SubsetType.Valid:
            return create_dataset_from_Xy(X_valid, y_valid)


def build_input_for_statistics_from_path(
    path_to_load,
    sep,
    metric_instances=build_default_instances(),
    norm_size=15000,
    current_preprocessing=None,
    subset_type=SubsetType.All,
):

    loaded_data = load_dataset_from_path_with_normalization(
        path_to_load, None, current_preprocessing
    )

    if norm_size is None:
        normalized_loaded_data = loaded_data
    else:
        normalized_loaded_data = normalize_dataframe_to_size(loaded_data, norm_size)

    return (
        get_datset_from_type(subset_type, normalized_loaded_data),
        MetricWrapper(None, metric_instances, None),
    )


def build_input_for_statistics(
    path_to_load,
    sep,
    statistic_description,
    metric_instances=build_default_instances(),
    text_pipeline_func=None,
    save=True,
    sub_directory=STATISTICS_SUBDIRECTORY,
    specific_directory_for_statistic=SPECIFIC_DIRECTORY_FOR_STATISTICS,
):
    path_parts = path_to_load.split(os.path.sep)
    name_of_file = path_parts[-1]

    del path_parts[-1]

    return (
        get_dataset_object_from_path(path_to_load, sep, text_pipeline_func),
        MetricWrapper(
            statistic_description,
            metric_instances,
            create_path_to_save(
                path_parts,
                name_of_file,
                sub_directory,
                save,
                specific_directory_for_statistic,
            ),
        ),
    )


def create_path_to_save(
    path_parts,
    name_of_file,
    sub_directory,
    save=True,
    specific_directory_for_statistic=None,
):
    if not save:
        return None

    name_of_file = create_stats_filename(name_of_file)

    if specific_directory_for_statistic is not None:
        if not os.path.exists(specific_directory_for_statistic):
            os.makedirs(specific_directory_for_statistic)
        path = os.path.sep.join([specific_directory_for_statistic, name_of_file])
        print(f"Current path to statistics={path}")
        return path

    else:
        path = os.path.sep.join(path_parts)

        if sub_directory is not None:
            path = path + os.path.sep + sub_directory

        if not os.path.exists(path):
            os.makedirs(path)

        path = path + os.path.sep + name_of_file
        print(f"Current path to statistics={path}")
        return path
