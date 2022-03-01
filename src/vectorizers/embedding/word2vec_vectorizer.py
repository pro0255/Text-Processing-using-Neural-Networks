from src.vectorizers.embedding.embedding_vectorizer import EmbeddingVectorizer
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType


class Word2VecVectorizer(EmbeddingVectorizer):
    def __init__(self):
        super().__init__(DownloadedEmbeddingType.Word2Vec)
