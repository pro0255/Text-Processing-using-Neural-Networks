from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class PredictionModelType(Enum):
    """Type of prediction models which are used in project.
    """
    NeuralNet = "NeuralNet"
    Classic = "Classic"
    Blank = BLANK_DESCRIPTION
