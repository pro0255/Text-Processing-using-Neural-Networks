from enum import Enum

class ResultType(Enum):
    Recall = "Recall"
    ConsfusionMatrix = "ConsfusionMatrix"
    Precision = "Precision"
    Accuracy = "Accuracy"
    F1 = "F1"
