from src.defined_types.types import PredictionClassesType, VectorizerClassesType


class ClassicExpConf:
    """Helper class which holds important data for experiment wrapper."""

    def __init__(
        self,
        train,
        test,
        experiment_id: str,
        description: str,
        predict_instance: PredictionClassesType,
        vectorization_instance: VectorizerClassesType,
    ) -> None:
        self.train = train
        self.test = test
        self.experiment_id = experiment_id
        self.description = description
        self.predict_instance = predict_instance
        self.vectorization_instance = vectorization_instance

    def get_train(self):
        return self.train

    def get_test(self):
        return self.test

    def get_experiment_id(self) -> str:
        return self.experiment_id

    def get_description(self) -> str:
        return self.description

    def get_predict_instance(self):
        return self.predict_instance

    def get_vectorization_instance(self):
        return self.vectorization_instance
