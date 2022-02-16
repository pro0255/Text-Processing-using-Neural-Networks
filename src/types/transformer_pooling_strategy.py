from enum import Enum
from src.config.config import BLANK_DESCRIPTION

class TransformerPooling(Enum):
    CLS = "CLS"
    Average = "Average"
    Stacking = "Stacking"
    Blank = BLANK_DESCRIPTION
    #TODO create own others