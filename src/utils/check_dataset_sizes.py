import numpy as np

def check_dataset_sizes(train_size=1, test_size=0, valid_size=0):
    if np.sum([train_size, test_size, valid_size]) != 1:
        assert Exception("Is not valid split!")