from enum import Enum
from src.config.config import BLANK_DESCRIPTION


class TransformerName(Enum):
    DistilBertBaseUncased = "distilbert-base-uncased"
    BertBaseUncased = "bert-base-uncased"
    ElectraBase = "google/electra-base-discriminator"
    Blank = BLANK_DESCRIPTION
