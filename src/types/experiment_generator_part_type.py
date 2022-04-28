from enum import Enum


class ExperimentGeneratorPart(Enum):
    """Fields which are part of generator for experiments."""

    DatasetGenerator = "DatasetGenerator"
    ExperimentConfiguration = "ExperimentConfiguration"
    ExperimentArchitecture = "ExperimentArchitecture"
    FeatureExtractors = "FeatureExtractors"
    Predictor = "Predictor"
    TransformerPoolingStrategy = "TransformerPoolingStrategy"
