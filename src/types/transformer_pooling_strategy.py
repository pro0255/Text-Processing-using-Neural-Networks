from enum import Enum
from src.config.config import BLANK_DESCRIPTION


class TransformerPoolingStrategy(Enum):
    CLS = "CLS"
    Average = "Average"
    ConcatCLS = "ConcatCLS"
    ConcatAverage = "ConcatAverage"
    Blank = BLANK_DESCRIPTION
