from enum import Enum


class TimeType(Enum):
    VectorizationTime = "VectorizationTime"
    LearningTime = "LearningTime"
    PredictionTime = "PredictionTime"
    EvaluateTime = "EvaluateTime"
