
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType
import gensim.downloader

loaded_models = {
    DownloadedEmbeddingType.Glove.value: gensim.downloader.load(DownloadedEmbeddingType.Glove.value),
    DownloadedEmbeddingType.Word2Vec.value: gensim.downloader.load(DownloadedEmbeddingType.Word2Vec.value)
}

