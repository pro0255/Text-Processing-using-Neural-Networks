from enum import Enum

class TransformerInput(Enum):
    mask = 'attention_mask'
    input = 'input_ids'