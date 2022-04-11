import typing
from sklearn.metrics import precision_score


def presicion(y_true:typing.List[int], y_pred:typing.List[int]):
    return precision_score(y_true, y_pred, average="micro")
