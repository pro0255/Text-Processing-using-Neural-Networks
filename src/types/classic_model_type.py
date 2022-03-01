from enum import Enum


class ClassicModelType(Enum):
    NaiveBayes = "NaiveBayesClassifier"
    RandomForest = "RandomForestClassifier"
    Linear = "LinearClassifier"
