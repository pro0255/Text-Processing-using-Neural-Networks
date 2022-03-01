from sklearn.metrics import precision_score


def presicion(y_true, y_pred):
    return precision_score(y_true, y_pred, average="micro")
