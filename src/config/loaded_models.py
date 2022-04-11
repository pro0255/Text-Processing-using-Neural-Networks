import gensim.downloader
import typing
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType

loaded_models: typing.Dict[str, typing.Dict] = {
    DownloadedEmbeddingType.Glove.value: gensim.downloader.load(
        DownloadedEmbeddingType.Glove.value
    ),
    DownloadedEmbeddingType.Word2Vec.value: gensim.downloader.load(
        DownloadedEmbeddingType.Word2Vec.value
    ),
}
