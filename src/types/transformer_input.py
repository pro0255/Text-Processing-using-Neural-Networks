from enum import Enum


class TransformerInput(Enum):
    """Parts of transformer input. It is according to paper.
    """
    mask = "attention_mask"
    input = "input_ids"
