from enum import Enum


class TimeType(Enum):
    """Types of time which will be logged."""

    VectorizationTime = "VectorizationTime"
    LearningTime = "LearningTime"
    PredictionTime = "PredictionTime"
    EvaluateTime = "EvaluateTime"
