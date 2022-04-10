from enum import Enum
from src.config.config import BLANK_DESCRIPTION


class NetType(Enum):
    Dense = "Dense"
    LSTM = "LSTM"
    RNN = "RNN"
    GRU = "GRU"
    CNN = "CNN"
    Blank = BLANK_DESCRIPTION
