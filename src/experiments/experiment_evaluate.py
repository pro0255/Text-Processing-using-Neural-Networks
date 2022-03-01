from sklearn.metrics import confusion_matrix
from src.experiments.results.accuracy import accuracy
from src.experiments.results.f1 import f1
from src.experiments.results.precision import presicion
from src.experiments.results.recall import recall
from src.experiments.results.conf_matrix import conf_matrix
from src.types.results import ResultType
import pandas as pd
from src.config.config import FILENAME_METRICS, FILENAME_CONFUSION_MATRIX, LOG_SEP
import os


class ExperimentEvaluate:
    def __init__(self, experiment_id, directory=None) -> None:
        self.directory = directory
        self.experiment_id = experiment_id

    def calc(self, y_true, y_pred):
        self.state = {}
        self.state[ResultType.Accuracy.value] = accuracy(y_true, y_pred)
        self.state[ResultType.F1.value] = f1(y_true, y_pred)
        self.state[ResultType.Precision.value] = presicion(y_true, y_pred)
        self.state[ResultType.Recall.value] = recall(y_true, y_pred)
        self.state[ResultType.ConsfusionMatrix.value] = conf_matrix(y_true, y_pred)

    def save_confusion_matrix(self):
        confusion_matrix = self.state[ResultType.ConsfusionMatrix.value]
        df = pd.DataFrame(confusion_matrix)
        path = os.path.sep.join(
            [self.directory, self.experiment_id, FILENAME_CONFUSION_MATRIX]
        )
        df.to_csv(path, sep=LOG_SEP)

    def save_metrics(self):
        metrics = self.state.copy()
        del metrics[ResultType.ConsfusionMatrix.value]
        df = pd.DataFrame.from_dict(metrics, orient="index")
        path = os.path.sep.join([self.directory, self.experiment_id, FILENAME_METRICS])
        df.to_csv(path, sep=LOG_SEP)

    def save(self):
        print("Saving results")
        self.save_confusion_matrix()
        self.save_metrics()
