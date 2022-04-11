import typing
from src.experiments.experiment_scripts.classic.classic_configuration import ClassicExpConf
from src.config.config import (EXPERIMENT_RESULTS_DIRECTORY,
                               NAME_OF_LEARNING_LOGS)
from src.experiments.helpers.experiment_evaluate import ExperimentEvaluate
from src.experiments.helpers.experiment_setup import ExperimentSetup
from src.experiments.helpers.experiment_summarization import \
    ExperimentSummarization
from src.experiments.helpers.experiment_timer import ExperimentTimer
from src.types.experiment_description import ExperimentDescriptionType
from src.types.subset_type import SubsetType
from src.types.time_type import TimeType
from src.utils.get_extra_field import get_extra
from src.vectorizers.runner import VectorizerRunner


class ClassicExpRunWrapper:
    def __init__(
        self,
        experiment_id:str,
        experiment_summarization=None,
        directory:str=EXPERIMENT_RESULTS_DIRECTORY,
        log_filename:str=NAME_OF_LEARNING_LOGS,
    ) -> None:
        self.directory = directory
        self.experiment_id = experiment_id
        self.log_filename = log_filename
        self.experiment_timer = ExperimentTimer()
        self.experiment_summarization = (
            ExperimentSummarization(experiment_id, self.directory)
            if experiment_summarization is None
            else experiment_summarization
        )
        self.set_id(experiment_id)

    def set_id(self, experiment_id:str):
        self.experiment_id = experiment_id
        self.experiment_setup = ExperimentSetup(experiment_id, self.directory)
        self.experiment_evaluate = ExperimentEvaluate(experiment_id, self.directory)

    def vectorizer_sentences(
        self, train_ds, test_ds, vectorization_instance
    ):
        print("New vectorization")

        vectorization_runner = VectorizerRunner()

        self.experiment_timer.start(TimeType.VectorizationTime.value)
        X_train, y_train = vectorization_runner.fit(
            train_ds,
            vectorization_instance,
            SubsetType.Train,
            self.experiment_summarization,
        )
        print("End train")

        X_test, y_true_labels = vectorization_runner.fit(
            test_ds,
            vectorization_instance,
            SubsetType.Test,
            self.experiment_summarization,
        )
        print("End test")
        self.experiment_timer.end(TimeType.VectorizationTime.value)
        print("End of vectorization")

        return X_train, X_test, y_train, y_true_labels

    def fit(self, X_train, y_train, predict_instance):
        print("Fitting model")
        self.experiment_timer.start(TimeType.LearningTime.value)
        predict_instance.fit(X_train, y_train)
        self.experiment_timer.end(TimeType.LearningTime.value)

    def predict(self, X_test, predict_instance):
        print("Predicting test dataset")
        self.experiment_timer.start(TimeType.PredictionTime.value)
        y_pred_labels = predict_instance.predict(X_test)
        self.experiment_timer.end(TimeType.PredictionTime.value)
        return y_pred_labels

    def run_vectorization(self, vectorization_instance, train_ds, test_ds):
        X_train, X_test, y_train, y_test = self.vectorizer_sentences(
            train_ds, test_ds, vectorization_instance
        )
        return X_train, X_test, y_train, y_test

    def get_configuration_values(self, classic_conf: typing.Type[ClassicExpConf]):
        X_train, y_train = classic_conf.get_train()
        X_test, y_test = classic_conf.get_test()
        return (
            X_train,
            y_train,
            X_test,
            y_test,
            classic_conf.get_description(),
            classic_conf.get_predict_instance(),
        )

    def run_prediction(self, classic_conf: typing.Type[ClassicExpConf]):
        (
            X_train,
            y_train,
            X_test,
            y_test,
            description,
            predict_instance,
        ) = self.get_configuration_values(classic_conf)

        self.description = description

        self.experiment_setup.run()

        self.fit(X_train, y_train, predict_instance)
        y_pred_labels = self.predict(X_test, predict_instance)

        print("Evaluating results")
        self.experiment_timer.start(TimeType.EvaluateTime.value)
        self.experiment_evaluate.calc(y_test, y_pred_labels)
        self.experiment_timer.end(TimeType.EvaluateTime.value)

        self.experiment_summarization.map_timer(self.experiment_timer)

        print("Saving")
        self.experiment_evaluate.save()
        self.experiment_summarization.save()

        print("Saving decription of experiment")

        try:
            description.state[ExperimentDescriptionType.ExtraField.value] = get_extra(
                predict_instance
            )
        except:
            print(
                f"Error when getting extra field for experiment {classic_conf.get_experiment_id()}!"
            )

        self.description.save()
