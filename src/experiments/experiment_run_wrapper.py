from src.experiments.experiment_setup import ExperimentSetup
from src.experiments.experiment_evaluate import ExperimentEvaluate
from src.experiments.experiment_summarization import ExperimentSummarization
from src.config.config import EXPERIMENT_RESULTS_DIRECTORY, NAME_OF_LEARNING_LOGS
from src.utils.prediction_to_labels import prediction_to_labels
from src.utils.dataset_to_ytrue import dataset_to_ytrue
from src.callbacks.callback_factory import CallbacksFactory
from src.experiments.experiment_timer import ExperimentTimer
from src.types.time_type import TimeType


class ExperimentRunWrapper:
    def __init__(
        self,
        experiment_id,
        experiment_summarization=None,
        directory=EXPERIMENT_RESULTS_DIRECTORY,
        log_filename=NAME_OF_LEARNING_LOGS,
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

    def run(
        self, model, train_ds, val_ds, test_ds, learning_config, description, save_model
    ):

        self.description = description
        # create directory
        self.experiment_setup.run()

        # compile model

        print("Compiling model")
        model.compile(
            loss=learning_config.loss,
            optimizer=learning_config.optimizer,
            metrics=learning_config.metric,
        )
        # run model, with callbacks

        callback_factory = CallbacksFactory(save_model)

        print("Fitting model")

        self.experiment_timer.start(TimeType.LearningTime.value)
        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=learning_config.epochs,
            callbacks=callback_factory.create(
                self.experiment_id, self.directory, self.log_filename
            ),
        )
        self.experiment_timer.end(TimeType.LearningTime.value)

        # save results
        print("Predicting test dataset")
        self.experiment_timer.start(TimeType.PredictionTime.value)
        y_pred = model.predict(test_ds)
        self.experiment_timer.end(TimeType.PredictionTime.value)

        print("Evaluating results")
        self.experiment_timer.start(TimeType.EvaluateTime.value)
        y_pred_labels = prediction_to_labels(y_pred)
        y_true_labels = dataset_to_ytrue(test_ds)
        self.experiment_evaluate.calc(y_true_labels, y_pred_labels)
        self.experiment_timer.end(TimeType.EvaluateTime.value)

        self.experiment_summarization.map_timer(self.experiment_timer)
        print("Saving")
        self.experiment_evaluate.save()
        self.experiment_summarization.save()
        
        print("Saving decription of experiment")
        self.description.save()
