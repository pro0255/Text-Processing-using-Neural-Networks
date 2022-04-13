from enum import Enum


class ExperimentType(Enum):
    TrainableTransformer = "Learning"  # Done
    PoolingStrategyTransformer = "PoolingStrategyTransformer"  # Done
    OutputSequenceLengthTransformer = "OutputSequenceLength"  # Done
    LearningRateTransformer = "LearningRateTransformer"  # Done
    LabelSizeTransformer = "LabelSizeLabelSizeTransformer"  # Done
    PreprocessingType = "PreprocessingType"  # Done
    TransformerType = "TransformerType"
    PreprocessingTransformer = "PreprocessingTransformer"

    NumberOfAuthorsNN = "NumberOfAuthorsNN"
    NumberOfSentencesNN = "NumberOfSentencesNN"

    


    EmbeddingSizeNN = "EmbeddingSizeNN"

    Classic = "Classic"
    ClassicLogisticRegressionLabelSize = "ClassicLogisticRegression"
    ClassicLogisticRegressionPreprocessing = "ClassicLogisticRegression"

    TransformerTest = "TransformerTest"
    NNTest = "NNTest"
    ClassicTest = "ClassicTest"
