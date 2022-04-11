from enum import Enum

from src.types.time_type import TimeType


class ExperimentSummarizationFields(Enum):
    ExperimentType = "ExperimentType"
    ExperimentId = "ExperimentId"
    TrainRecords = "TrainRecords"
    TestRecords = "TestRecords"
    ValidRecords = "ValidRecords"
    VectorizationTime = TimeType.VectorizationTime.value
    LearningTime = TimeType.LearningTime.value
    PredictionTime = TimeType.PredictionTime.value
    EvaluateTime = TimeType.EvaluateTime.value
    EmbeddingSize = "EmbeddingSize"
    MissingRatioTrain = "MissingRatioTrain"
    MissingRatioTest = "MissingRatioTest"
