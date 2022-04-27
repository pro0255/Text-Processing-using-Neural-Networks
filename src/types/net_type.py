from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class NetType(Enum):
    """Net types which are used in project.
    """
    Dense = "Dense"
    LSTM = "LSTM"
    RNN = "RNN"
    GRU = "GRU"
    CNN = "CNN"
    Blank = BLANK_DESCRIPTION
