import typing
import numpy as np
import tensorflow as tf


def dataset_to_ytrue(dataset: typing.Type[tf.data.Dataset]):
    return np.concatenate([y for x, y in dataset], axis=0)
