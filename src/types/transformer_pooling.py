from enum import Enum
from src.config.config import BLANK_DESCRIPTION

class TransformerPooling(Enum):
    LastHiddenState = "last_hidden_state"
    Pooler = "pooler_output"
    HiddenStates = "hidden_states"
    Blank = BLANK_DESCRIPTION
    #TODO create own others