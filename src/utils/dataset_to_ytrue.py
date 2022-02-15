import numpy as np

def dataset_to_ytrue(dataset):
    return np.concatenate([y for x, y in dataset], axis=0)