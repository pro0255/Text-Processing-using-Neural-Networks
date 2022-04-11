from enum import Enum

from sklearn.neighbors import KNeighborsTransformer


class ClassicModelType(Enum):
    NaiveBayes = "NaiveBayesClassifier"
    RandomForest = "RandomForestClassifier"
    Linear = "LinearClassifier"
    KNeighbors = "KNeighborsClassifier"
