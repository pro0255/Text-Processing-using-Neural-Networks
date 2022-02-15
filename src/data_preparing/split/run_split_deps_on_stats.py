from src.config.config import TRAIN_SIZE, TEST_SIZE, VALIDATION_SIZE
from src.utils.check_dataset_sizes import check_dataset_sizes
from src.statistic.build_input_for_statistics import build_input_for_statistics
from src.statistic.create_statistics_from import create_statistics_from
from src.statistic.instances.label_metric import LabelMetric
from src.data_preparing.split.split_file_to_train_test_valid import split_file_to_train_test_valid
import os


def run_split_deps_on_stats(
    path_to_load, 
    path_to_save, 
    normalization = True, 
    train_size=TRAIN_SIZE, 
    test_size=TEST_SIZE, 
    valid_size=VALIDATION_SIZE
):
    check_dataset_sizes(train_size, test_size, valid_size)
    
    metric_instance = create_statistics_from(
        *build_input_for_statistics(
            path_to_load,
            ';', 
            [LabelMetric()], 
            None,
            False
        )
    )
    
    number_of_min_label = None
    label_metric = metric_instance.metric_instances[0].get_dataframe()
    
    if normalization:
        sorted_label_metric_frame = label_metric.sort_values(by=0)
        number_of_min_label = sorted_label_metric_frame.iloc[0][0]
    
    print(label_metric)
    split_file_to_train_test_valid(path_to_load, path_to_save, label_metric, number_of_min_label)
    print('Splitting finished!')



def run_split_deps_on_stats_same_dir(
    path_to_load, 
    normalization=True
):
    run_split_deps_on_stats(
        path_to_load,
        os.path.sep.join(path_to_load.split(os.path.sep)[0:-1]),
        normalization
    )
