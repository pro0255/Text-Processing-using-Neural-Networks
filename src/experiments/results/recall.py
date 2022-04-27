import typing

from sklearn.metrics import recall_score


def recall(y_true: typing.List[int], y_pred: typing.List[int]):
    """Calculate metric recall

    Args:
        y_true (typing.List[int]): real values
        y_pred (typing.List[int]): predicted values

    Returns:
        _type_: metric recall
    """
    return recall_score(y_true, y_pred, average="micro")
