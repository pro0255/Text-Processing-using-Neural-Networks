from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class TransformerPoolingStrategy(Enum):
    """Type of strategies which are used in project.
    """
    CLS = "CLS"
    Average = "Average"
    ConcatCLS = "ConcatCLS"
    ConcatAverage = "ConcatAverage"
    Blank = BLANK_DESCRIPTION
