import numpy as np


def prepare_embedding_matrix(word_index, embeddings_index, embedding_dim):
    num_tokens = len(word_index) + 2
    hits = 0
    misses = 0

    embedding_matrix = np.zeros((num_tokens, embedding_dim))
    for word, i in word_index.items():
        embedding_vector = None
        try:
            embedding_vector = embeddings_index.get_vector(word)
        except:
            embedding_vector = None
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
            hits += 1
        else:
            misses += 1
    return embedding_matrix, num_tokens, (hits, misses)
