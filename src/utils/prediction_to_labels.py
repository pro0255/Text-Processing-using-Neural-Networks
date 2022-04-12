import typing

import numpy as np


def prediction_to_labels(y_pred: typing.List[float]) -> typing.List[int]:
    y_pred = np.argmax(y_pred, axis=1)
    return y_pred
