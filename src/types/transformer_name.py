from enum import Enum

from src.config.config import BLANK_DESCRIPTION


class TransformerName(Enum):
    """Types of BERT derivates which are used in project.
    """
    DistilBertBaseUncased = "distilbert-base-uncased"
    BertBaseUncased = "bert-base-uncased"
    ElectraBase = "google/electra-base-discriminator"
    Blank = BLANK_DESCRIPTION
