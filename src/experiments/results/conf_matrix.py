import typing

from sklearn.metrics import confusion_matrix


def conf_matrix(y_true: typing.List[int], y_pred: typing.List[int]):
    """Calculated confusion matrix for prediction.

    Args:
        y_true (typing.List[int]): real values
        y_pred (typing.List[int]): predicted values

    Returns:
        _type_: confusion matrix
    """
    return confusion_matrix(y_true, y_pred)
