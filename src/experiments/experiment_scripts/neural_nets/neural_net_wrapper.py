import os
import typing

import tensorflow as tf

from src.callbacks.callback_factory import CallbacksFactory
from src.callbacks.save_best_weights import create_save_best_weights_filepath
from src.config.config import (EXPERIMENT_RESULTS_DIRECTORY,
                               NAME_OF_LEARNING_LOGS)
from src.experiments.experiment_scripts.neural_nets.neural_net_configuration import \
    NNExpConf
from src.experiments.helpers.experiment_evaluate import ExperimentEvaluate
from src.experiments.helpers.experiment_setup import ExperimentSetup
from src.experiments.helpers.experiment_summarization import \
    ExperimentSummarization
from src.experiments.helpers.experiment_timer import ExperimentTimer
from src.experiments.settings.settings import LearningSettings
from src.types.time_type import TimeType
from src.utils.dataset_to_ytrue import dataset_to_ytrue
from src.utils.log_juypter import add_experiment_jupyter_logger
from src.utils.prediction_to_labels import prediction_to_labels


class NNExpRunWrapper:
    def __init__(
        self,
        experiment_id: str,
        experiment_summarization: typing.Union[
            typing.Type[ExperimentSummarization], None
        ] = None,
        directory: str = EXPERIMENT_RESULTS_DIRECTORY,
        log_filename: str = NAME_OF_LEARNING_LOGS,
    ) -> None:
        self.directory = directory
        self.experiment_id = experiment_id
        self.log_filename = log_filename
        self.experiment_setup = ExperimentSetup(experiment_id, self.directory)
        self.experiment_evaluate = ExperimentEvaluate(experiment_id, self.directory)
        self.experiment_summarization = (
            ExperimentSummarization(experiment_id, self.directory)
            if experiment_summarization is None
            else experiment_summarization
        )
        self.experiment_timer = ExperimentTimer()

    def get_configuration_values(self, nn_conf: typing.Type[NNExpConf]):
        return (
            nn_conf.get_model(),
            nn_conf.get_train(),
            nn_conf.get_valid(),
            nn_conf.get_test(),
            nn_conf.get_learning_settings(),
            nn_conf.get_description(),
            nn_conf.get_save_model(),
            nn_conf.get_save_best(),
        )

    def compile_nn_model(
        self, nn_model, learning_settings: typing.Type[LearningSettings]
    ):
        print("Compiling model")
        nn_model.compile(
            loss=learning_settings.loss,
            optimizer=learning_settings.optimizer,
            metrics=learning_settings.metric,
        )

    def fit_nn_model(
        self,
        nn_model,
        train_ds: typing.Type[tf.data.Dataset],
        valid_ds: typing.Type[tf.data.Dataset],
        learning_settings: typing.Type[LearningSettings],
        save_model: bool,
        save_best: bool,
    ):
        callback_factory = CallbacksFactory(save_model, save_best)
        print("Fitting model")
        self.experiment_timer.start(TimeType.LearningTime.value)
        nn_model.fit(
            train_ds,
            validation_data=valid_ds,
            epochs=learning_settings.epochs,
            callbacks=callback_factory.create(
                self.experiment_id, self.directory, self.log_filename
            ),
        )
        self.experiment_timer.end(TimeType.LearningTime.value)

    def load_nn_best(self, nn_model):
        print("Loading best weights to model")
        experiment_directory = os.path.sep.join([self.directory, self.experiment_id])
        best_weights_path = create_save_best_weights_filepath(experiment_directory)
        nn_model.load_weights(best_weights_path)

    def predict_on_nn(self, nn_model, test_ds: typing.Type[tf.data.Dataset]):
        print("Predicting test dataset")
        self.experiment_timer.start(TimeType.PredictionTime.value)
        y_pred = nn_model.predict(test_ds)
        self.experiment_timer.end(TimeType.PredictionTime.value)
        return y_pred

    def evaluate_prediction(self, y_pred, test_ds: typing.Type[tf.data.Dataset]):
        print("Evaluating results")
        self.experiment_timer.start(TimeType.EvaluateTime.value)
        y_pred_labels = prediction_to_labels(y_pred)
        y_true_labels = dataset_to_ytrue(test_ds)
        self.experiment_evaluate.calc(y_true_labels, y_pred_labels)
        self.experiment_timer.end(TimeType.EvaluateTime.value)

    def save_experiment(self):
        self.experiment_summarization.map_timer(self.experiment_timer)
        print("Saving")
        self.experiment_evaluate.save()
        self.experiment_summarization.save()
        print("Saving decription of experiment")
        self.description.save()

    def run(self, nn_conf: typing.Type[NNExpConf]):

        # Getting values from configuration object
        (
            nn_model,
            train_ds,
            valid_ds,
            test_ds,
            learning_settings,
            description,
            save_model,
            save_best,
        ) = self.get_configuration_values(nn_conf)

        # Saving description to object
        self.description = description

        # Creating experiment directory
        self.experiment_setup.run()

        # Adding logger of jupyter
        f = add_experiment_jupyter_logger(self.experiment_setup.parent_path)

        # Compiling model
        self.compile_nn_model(nn_model, learning_settings)

        # Fitting model
        self.fit_nn_model(
            nn_model, train_ds, valid_ds, learning_settings, save_model, save_best
        )

        # Before prediction load best weights
        if save_best:
            self.load_nn_best(nn_model)

        # Make prediction
        y_pred = self.predict_on_nn(nn_model, test_ds)

        # Evaluate
        self.evaluate_prediction(y_pred, test_ds)

        # Saving experiment
        self.save_experiment()

        print("End of experiment")
