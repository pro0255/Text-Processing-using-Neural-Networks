from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class PredictionModelType(Enum):
    NeuralNet = "NeuralNet"
    Classic = "Classic"
    Blank = BLANK_DESCRIPTION
