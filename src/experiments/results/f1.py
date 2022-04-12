import typing

from sklearn.metrics import f1_score


def f1(y_true: typing.List[int], y_pred: typing.List[int]):
    return f1_score(y_true, y_pred, average="micro")
