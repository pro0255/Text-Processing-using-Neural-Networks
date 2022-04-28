from enum import Enum

from src.config.config import BLANK_DESCRIPTION
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType


class EmbeddingType(Enum):
    """Type of embedding which is used in project."""

    Glove = "Glove"
    W2V = "Word2Vec"
    Transformer = "Transformer"
    TfIdf = "TfIdf"
    BoW = "BoW"
    TFEmbedding = "TFEmbedding"
    Blank = BLANK_DESCRIPTION


def translate_from_embedding(embedding_name):
    if embedding_name == DownloadedEmbeddingType.Word2Vec:
        return EmbeddingType.W2V
    elif embedding_name == DownloadedEmbeddingType.Glove:
        return EmbeddingType.Glove
    elif embedding_name is None:
        return EmbeddingType.TFEmbedding
