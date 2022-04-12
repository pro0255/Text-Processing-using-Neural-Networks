import typing
from sklearn.metrics import confusion_matrix


def conf_matrix(y_true: typing.List[int], y_pred: typing.List[int]):
    return confusion_matrix(y_true, y_pred)
