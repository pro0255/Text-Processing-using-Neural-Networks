from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class TransformerPooling(Enum):
    """Type of pooling key which can be found in HuggingFace objects.
    """
    LastHiddenState = "last_hidden_state"
    Pooler = "pooler_output"
    HiddenStates = "hidden_states"
    Blank = BLANK_DESCRIPTION
