import typing

from sklearn.metrics import f1_score


def f1(y_true: typing.List[int], y_pred: typing.List[int]):
    """Calculates f1 score

    Args:
        y_true (typing.List[int]): real values
        y_pred (typing.List[int]): predicted values

    Returns:
        _type_: float f1 score
    """
    return f1_score(y_true, y_pred, average="micro")
