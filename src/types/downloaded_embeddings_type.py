from enum import Enum


class DownloadedEmbeddingType(Enum):
    """Types of embeddings which are used in project.
    """
    Word2Vec = "glove-wiki-gigaword-300"
    Glove = "word2vec-google-news-300"
