import typing
from sklearn.metrics import accuracy_score


def accuracy(y_true: typing.List[int], y_pred:typing.List[int]):
    return accuracy_score(y_true, y_pred)
