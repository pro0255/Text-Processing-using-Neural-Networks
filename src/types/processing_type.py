from enum import Enum
from src.config.config import BLANK_DESCRIPTION

class PreprocessingType(Enum):
    Default = "Default"
    Lowercase = "Lowercase"
    Blank = BLANK_DESCRIPTION