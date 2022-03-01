import numpy as np


def prediction_to_labels(y_pred):
    y_pred = np.argmax(y_pred, axis=1)
    return y_pred
