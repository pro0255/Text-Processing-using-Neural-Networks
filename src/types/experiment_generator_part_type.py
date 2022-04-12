from enum import Enum


class ExperimentGeneratorPart(Enum):
    DatasetGenerator = "DatasetGenerator"
    ExperimentConfiguration = "ExperimentConfiguration"
    ExperimentArchitecture = "ExperimentArchitecture"
    FeatureExtractors = "FeatureExtractors"
    Predictor = "Predictor"
    TransformerPoolingStrategy = "TransformerPoolingStrategy"
