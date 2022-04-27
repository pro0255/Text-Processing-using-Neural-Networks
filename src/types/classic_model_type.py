from enum import Enum

from sklearn.neighbors import KNeighborsTransformer


class ClassicModelType(Enum):
    """List of classic models which are used in project.
    """
    NaiveBayes = "NaiveBayesClassifier"
    RandomForest = "RandomForestClassifier"
    Linear = "LinearClassifier"
    KNeighbors = "KNeighborsClassifier"
