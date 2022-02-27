import time
from src.experiments.experiment_summarization import ExperimentSummarization
from src.experiments.sandbox.classic_experiment_runner import ClassicExperimentWrapper 

class ClassicModelWithVectorizerExperiment:
    def __init__(self) -> None:
        pass

    def run(
        self,
        experiment_configurations
    ):
        for experiment_configuration in experiment_configurations:
            current_timestamp = time.time()

            train_ds = experiment_configuration.get_train()
            test_ds = experiment_configuration.get_test()
            experiment_id = experiment_configuration.get_experiment_id(current_timestamp)
            description = experiment_configuration.get_description()
            predict_instance = experiment_configuration.get_predict_instance()
            vectorization_instance = experiment_configuration.get_vectorization_instance()


            summarization = ExperimentSummarization(experiment_id)
            wrapper = ClassicExperimentWrapper(
                experiment_id, 
                summarization
            )

            wrapper.run(
                predict_instance=predict_instance,
                vectorization_instance=vectorization_instance,
                train_ds=train_ds,
                val_ds=None,
                test_ds=test_ds,
                description=description,
            )