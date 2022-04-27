import typing

from sklearn.metrics import accuracy_score


def accuracy(y_true: typing.List[int], y_pred: typing.List[int]):
    """Return accuracy score.

    Args:
        y_true (typing.List[int]): real values
        y_pred (typing.List[int]): predicted values

    Returns:
        _type_: float
    """
    return accuracy_score(y_true, y_pred)
