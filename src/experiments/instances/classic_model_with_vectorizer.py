from src.experiments.experiment_summarization import ExperimentSummarization
from src.experiments.sandbox.classic_experiment_runner import ClassicExperimentWrapper 

class ClassicModelWithVectorizerExperiment:
    def __init__(self) -> None:
        pass

    def get_summarization(self, experiment_id, cache=None):
        if cache is not None:
            old_summarization = cache[4]
            old_summarization.experiment_id = experiment_id
        else:
            return ExperimentSummarization(experiment_id)

    def run(
        self,
        experiment_configuration,
        cache=None
    ):
        train_ds = experiment_configuration.get_train()
        test_ds = experiment_configuration.get_test()
        experiment_id = experiment_configuration.get_experiment_id()
        description = experiment_configuration.get_description()
        predict_instance = experiment_configuration.get_predict_instance()
        vectorization_instance = experiment_configuration.get_vectorization_instance()

        summarization = self.get_summarization(experiment_id, cache)

        wrapper = ClassicExperimentWrapper(
            experiment_id, 
            summarization
        )

        X_train, X_test, y_train, y_true_labels, experiment_summarization, experiment_timer = wrapper.run(
            predict_instance,
            vectorization_instance,
            train_ds,
            None,
            test_ds,
            description,
            cache
        )

        return X_train, X_test, y_train, y_true_labels, experiment_summarization, experiment_timer