from src.config.config import TEST_SIZE, TRAIN_SIZE, VALIDATION_SIZE
from src.utils.check_dataset_sizes import check_dataset_sizes
from src.data_preparing.split.DataSetSplitter import DataSetSplitter
from src.data_loading.get_dataset_object_from import get_dataset_object_from_path

def split_file_to_train_test_valid(
    path_to_load, 
    path_to_save, 
    label_metric=None,
    normalization_size=None,
    train_size=TRAIN_SIZE, 
    test_size=TEST_SIZE, 
    valid_size=VALIDATION_SIZE,
):
    check_dataset_sizes(train_size, test_size, valid_size)
    splitter = DataSetSplitter(path_to_save, train_size, test_size, valid_size, label_metric, normalization_size)
    
    dataset = get_dataset_object_from_path(path_to_load, ';', None)
    splitter.build_subsets(dataset)