from enum import Enum

"""Decleration of experiments which can be runned. These are keys and should be created definition with experiment values.
"""


class ExperimentType(Enum):
    TrainableTransformer = "Learning"
    PoolingStrategyTransformer = "PoolingStrategyTransformer"
    OutputSequenceLengthTransformer = "OutputSequenceLength"
    LearningRateTransformer = "LearningRateTransformer"
    LabelSizeTransformer = "LabelSizeLabelSizeTransformer"
    PreprocessingType = "PreprocessingType"
    TransformerType = "TransformerType"
    PreprocessingTransformer = "PreprocessingTransformer"

    Transformer310Combinations = "Transformer310Combinations"
    Transformer5SentencesCombinations = "Transformer5SentencesCombinations"

    EmbeddingSizeModelingNN = "EmbeddingSizeModelingNN"

    NumberOfAuthorsNN = "NumberOfAuthorsNN"
    NumberOfSentencesNN = "NumberOfSentencesNN"

    NN310Combinations = "NN310Combinations"
    NN5SentencesCombinations = "NN5SentencesCombinations"

    NNCNN5SentencesCombinations = "NNCNN5SentencesCombinations"
    NNCNN310SentencesCombinations = "NNCNN310SentencesCombinations"

    EmbeddingSizeNN = "EmbeddingSizeNN"

    Classic = "Classic"
    ClassicLogisticRegressionLabelSize = "ClassicLogisticRegressionLabelSize"
    ClassicLogisticRegressionPreprocessing = "ClassicLogisticRegressionPreprocessing"

    Classic310Combinations = "Classic310Combinations"
    Classic5SentencesCombinations = "Classic5SentencesCombinations"

    TransformerTest = "TransformerTest"
    NNTest = "NNTest"
    ClassicTest = "ClassicTest"
