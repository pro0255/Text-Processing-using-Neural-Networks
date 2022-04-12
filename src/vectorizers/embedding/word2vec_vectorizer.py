from src.types.downloaded_embeddings_type import DownloadedEmbeddingType
from src.vectorizers.embedding.embedding_vectorizer import EmbeddingVectorizer


class Word2VecVectorizer(EmbeddingVectorizer):
    def __init__(self, run_on_init: bool = False) -> None:
        super().__init__(DownloadedEmbeddingType.Word2Vec, run_on_init)
