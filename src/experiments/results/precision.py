import typing

from sklearn.metrics import precision_score


def presicion(y_true: typing.List[int], y_pred: typing.List[int]):
    """Calculates metric which is named precision

    Args:
        y_true (typing.List[int]): real values
        y_pred (typing.List[int]): predicted values

    Returns:
        _type_: float values which describes precision score
    """
    return precision_score(y_true, y_pred, average="micro")
