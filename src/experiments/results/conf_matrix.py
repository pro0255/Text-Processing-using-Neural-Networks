from sklearn.metrics import confusion_matrix

def conf_matrix(y_true, y_pred):
    return confusion_matrix(y_true, y_pred)