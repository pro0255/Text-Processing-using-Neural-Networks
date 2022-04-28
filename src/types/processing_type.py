from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class PreprocessingType(Enum):
    """Types of preprocessing which are used in project."""

    Default = "Default"
    Lowercase = "Lowercase"
    CaseInterpunction = "CaseInterpunction"
    Raw = "Raw"
    Blank = BLANK_DESCRIPTION
