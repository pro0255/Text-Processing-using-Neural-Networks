from enum import Enum


class ExperimentDescriptionType(Enum):
    """Field which are saved in experiment description csv file."""

    ExperimentType = "ExperimentType"
    ExperimentId = "ExperimentId"
    BatchSize = "BatchSize"
    Epochs = "Epochs"
    LearningRate = "LearningRate"
    TransformerName = "TransformerName"
    TransformerPooling = "TransformerPooling"
    PredictionModelType = "PredictionModelType"
    NetType = "NetType"
    EmbeddingType = "EmbeddingType"
    IsTrainable = "IsTrainable"
    PreprocessingType = "PreprocessingType"
    NumberOfAuthors = "NumberOfAuthors"
    NumberOfSentences = "NumberOfSentences"
    LoadPath = "LoadPath"
    SeqLen = "SeqLen"
    IsTest = "IsTest"
    ClassicModelName = "ClassicModelName"
    ExtraField = "ExtraField"
    TransformerStartIndex = "TransformerStartIndex"
    TransformerEndIndex = "TransformerEndIndex"
    TransformerPoolingStrategy = "TransformerPoolingStrategy"
    NormalizationSize = "NormalizationSize"
