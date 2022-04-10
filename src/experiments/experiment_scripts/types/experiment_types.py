from enum import Enum


class ExperimentType(Enum):
    TrainableTransformer = "Learning"  # Done
    PoolingStrategyTransformer = "PoolingStrategyTransformer"  # Done
    OutputSequenceLengthTransformer = "OutputSequenceLength"  # Done
    LearningRateTransformer = "LearningRateTransformer"  # Done
    LabelSize = "LabelSize"  # Done
    PreprocessingType = "PreprocessingType"  # Done
    TransformerType = "TransformerType"
    



    NumberOfAuthorsNN = "NumberOfAuthorsNN"
    NumberOfSentencesNN = "NumberOfSentencesNN"


    Classic = "Classic"

