import numpy as np


def check_dataset_sizes(train_size: float=1, test_size: float=0, valid_size:float=0) -> None:
    if np.sum([train_size, test_size, valid_size]) != 1:
        assert Exception("Is not valid split!")
