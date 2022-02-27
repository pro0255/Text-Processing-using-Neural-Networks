from src.experiments.experiment_summarization import ExperimentSummarization
from src.experiments.sandbox.classic_experiment_runner import ClassicExperimentWrapper 

class ClassicModelWithVectorizerExperiment:
    def __init__(self) -> None:
        pass

    def run(
        self,
        experiment_configuration
    ):
        train_ds = experiment_configuration.get_train()
        test_ds = experiment_configuration.get_test()
        experiment_id = experiment_configuration.get_experiment_id()
        description = experiment_configuration.get_description()
        predict_instance = experiment_configuration.get_predict_instance()
        vectorization_instance = experiment_configuration.get_vectorization_instance()

        summarization = ExperimentSummarization(experiment_id)
        wrapper = ClassicExperimentWrapper(
            experiment_id, 
            summarization
        )

        wrapper.run(
            predict_instance,
            vectorization_instance,
            train_ds,
            None,
            test_ds,
            description,
        )