from src.experiments.experiment_setup import ExperimentSetup
from src.experiments.experiment_evaluate import ExperimentEvaluate
from src.experiments.experiment_summarization import ExperimentSummarization
from src.config.config import EXPERIMENT_RESULTS_DIRECTORY, NAME_OF_LEARNING_LOGS
from src.experiments.experiment_timer import ExperimentTimer
from src.types.time_type import TimeType
from src.vectorizers.runner import VectorizerRunner
from src.types.subset_type import SubsetType
from src.utils.get_extra_field import get_extra
from src.types.experiment_description import ExperimentDescriptionType

class ClassicExperimentWrapper:
    def __init__(
        self,
        experiment_id,
        experiment_summarization=None,
        directory=EXPERIMENT_RESULTS_DIRECTORY,
        log_filename=NAME_OF_LEARNING_LOGS
    ) -> None:
        self.directory = directory 
        self.experiment_id = experiment_id
        self.log_filename = log_filename
        self.experiment_setup = ExperimentSetup(experiment_id, self.directory)
        self.experiment_evaluate = ExperimentEvaluate(experiment_id, self.directory)
        self.experiment_summarization = ExperimentSummarization(experiment_id, self.directory) if experiment_summarization is None else experiment_summarization
        self.experiment_timer = ExperimentTimer()


    def vectorizer_sentences(self, train_ds, test_ds, vectorization_instance):
        print("Running vectorization of data")
        
        #if cached then set experiment timer VectorizationTime.value with old
        #get X_train, y_train, X_test, y_true_labels
        vectorization_runner = VectorizerRunner()

        self.experiment_timer.start(TimeType.VectorizationTime.value)
        X_train, y_train = vectorization_runner.fit(
            train_ds, 
            vectorization_instance, 
            SubsetType.Train, 
            self.experiment_summarization
        )
        print("End train")


        X_test, y_true_labels = vectorization_runner.fit(
            test_ds, 
            vectorization_instance, 
            SubsetType.Test, 
            self.experiment_summarization
        )
        print("End test")
        self.experiment_timer.end(TimeType.VectorizationTime.value)
        print("End of vectorization")
        

        return X_train, X_test, y_train, y_true_labels


    def fit(self, X_train, y_train, predict_instance):
        print('Fitting model')
        self.experiment_timer.start(TimeType.LearningTime.value)
        predict_instance.fit(X_train, y_train)
        self.experiment_timer.end(TimeType.LearningTime.value)


    def predict(self, X_test, predict_instance):
        print('Predicting test dataset')
        self.experiment_timer.start(TimeType.PredictionTime.value)
        y_pred_labels = predict_instance.predict(X_test)
        self.experiment_timer.end(TimeType.PredictionTime.value)
        return y_pred_labels


    def run(
        self, 
        predict_instance,
        vectorization_instance,
        train_ds,
        val_ds,
        test_ds,
        description
    ):
        self.description = description

        #create directory
        self.experiment_setup.run()

        X_train, X_test, y_train, y_true_labels = self.vectorizer_sentences(train_ds, test_ds, vectorization_instance)


        
        self.fit(X_train, y_train, predict_instance)
        y_pred_labels = self.predict(X_test, predict_instance)


        print('Evaluating results')
        self.experiment_timer.start(TimeType.EvaluateTime.value)
        self.experiment_evaluate.calc(y_true_labels, y_pred_labels)
        self.experiment_timer.end(TimeType.EvaluateTime.value)

        self.experiment_summarization.map_timer(self.experiment_timer)

        print("Saving")
        self.experiment_evaluate.save()
        self.experiment_summarization.save()

        print('Saving decription of experiment')
        description.state[ExperimentDescriptionType.ExtraField.value] = get_extra(predict_instance)
        self.description.save()

        return X_train, X_test, y_train, y_true_labels, self.experiment_summarization





        
