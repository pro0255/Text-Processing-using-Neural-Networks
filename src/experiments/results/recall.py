import typing

from sklearn.metrics import recall_score


def recall(y_true: typing.List[int], y_pred: typing.List[int]):
    return recall_score(y_true, y_pred, average="micro")
