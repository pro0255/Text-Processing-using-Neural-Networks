import os
from src.statistic.create_stats_filename import create_stats_filename
from src.statistic.metric_wrapper import MetricWrapper
from src.data_loading.get_dataset_object_from import get_dataset_object_from_path
from src.statistic.DEFAULT_INSTANCES import DEFAULT_STATISTICS_INSTANCES
from src.config.config import SPECIFIC_DIRECTORY_FOR_STATISTICS, STATISTICS_SUBDIRECTORY


def build_input_for_statistics(
    path_to_load,
    sep,
    statistic_description,
    metric_instances=DEFAULT_STATISTICS_INSTANCES,
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
