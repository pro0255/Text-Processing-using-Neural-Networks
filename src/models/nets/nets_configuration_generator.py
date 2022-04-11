import itertools
import typing

from src.models.embedding.load_from_gensim import load_from_gensim
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType


def nets_configuration_generator(
    vocab_sizes: typing.List[int], output_sequence_lengths: typing.List[int], trainable:typing.List[bool], learning_settings, embedding: typing.Tuple[int, typing.Union[None, DownloadedEmbeddingType]]
):
    without_load = list(filter(lambda x: x[1] is None, embedding))
    need_to_load = list(filter(lambda x: x[1] is not None, embedding))

    embedding_final = []
    embedding_final += without_load

    embedding_index_dict = {}

    print("Loading embeddding")

    for current_load in need_to_load:
        embedding_size, embedding_name = current_load
        if embedding_name in embedding_index_dict:
            continue

        current_embedding = load_from_gensim(embedding_name.value)
        test_embedding_size = current_embedding["king"].shape[0]
        if embedding_size == test_embedding_size:

            embedding_index_dict[embedding_name] = current_embedding
            embedding_final.append(current_load)

    print("Embedding dictionaries loaded..")

    confs = list(
        itertools.product(
            vocab_sizes,
            output_sequence_lengths,
            trainable,
            learning_settings,
            embedding,
        )
    )

    return confs, embedding_index_dict
