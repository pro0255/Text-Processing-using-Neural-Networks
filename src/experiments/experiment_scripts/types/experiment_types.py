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
