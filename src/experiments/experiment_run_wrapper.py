from src.experiments.experiment_setup import ExperimentSetup
from src.experiments.experiment_evaluate import ExperimentEvaluate
from src.experiments.experiment_summarization import ExperimentSummarization
from src.config.config import EXPERIMENT_RESULTS_DIRECTORY, NAME_OF_LEARNING_LOGS
from src.utils.prediction_to_labels import prediction_to_labels
from src.utils.dataset_to_ytrue import dataset_to_ytrue
from src.callbacks.callback_factory import CallbacksFactory

class ExperimentRunWrapper:
    def __init__(
        self,
        experiment_id,
        directory=EXPERIMENT_RESULTS_DIRECTORY,
        log_filename=NAME_OF_LEARNING_LOGS
    ) -> None:
        self.directory = directory 
        self.experiment_id = experiment_id
        self.log_filename = log_filename
        self.experiment_setup = ExperimentSetup(experiment_id, self.directory)
        self.experiment_evaluate = ExperimentEvaluate(experiment_id, self.directory)
        self.experiment_summarization = ExperimentSummarization(experiment_id, self.directory)

    def run(
        self, 
        model,
        train_ds,
        val_ds,
        test_ds,
        learning_config,
        description,
        save_model
    ):
        self.description = description
        #create directory
        self.experiment_setup.run()

        print('Saving decription of experiment')
        self.description.save()
        #compile model

        print('Compiling model')
        model.compile(
            loss=learning_config.loss,
            optimizer=learning_config.optimizer,
            metrics=learning_config.metric
        )
        #run model, with callbacks

        callback_factory = CallbacksFactory(save_model)

        print('Fitting model')
        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=learning_config.epochs,
            callbacks=callback_factory.create(self.experiment_id, self.directory, self.log_filename),
        )

        #save results
        print('Predicting test dataset')
        y_pred = model.predict(test_ds)

        y_pred_labels = prediction_to_labels(y_pred)
        y_true_labels = dataset_to_ytrue(test_ds)


        print('Evaluating results')
        self.experiment_evaluate.calc(y_true_labels, y_pred_labels)
        self.experiment_evaluate.save()

        self.experiment_summarization.save()




        
