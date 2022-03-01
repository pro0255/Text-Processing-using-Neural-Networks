from enum import Enum
from src.config.config import BLANK_DESCRIPTION


class EmbeddingType(Enum):
    Glove = "Glove"
    W2V = "Word2Vec"
    Transformer = "Transformer"
    TfIdf = "TfIdf"
    BoW = "BoW"
    TFEmbedding = "TFEmbedding"
    Blank = BLANK_DESCRIPTION
