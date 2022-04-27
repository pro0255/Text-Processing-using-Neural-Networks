from enum import Enum


class ResultType(Enum):
    """Results which will be saved in .csv experiments folder.
    """
    Recall = "Recall"
    ConsfusionMatrix = "ConsfusionMatrix"
    Precision = "Precision"
    Accuracy = "Accuracy"
    F1 = "F1"
