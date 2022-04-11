
import tensorflow as tf
from src.config.config import BLANK_DESCRIPTION
from src.models.embedding.prepare_embedding_matrix import prepare_embedding_matrix
from tensorflow import string as tf_string

class Embedding:
    def __init__(self) -> None:
        pass

    def create_vect_embedding(self, train_ds, valid_ds, vocab_size, output_sequence_length, trainable, embedding_dim, embedding_dictionary=None):
        input_layer = tf.keras.layers.Input(shape=(1,), dtype=tf_string)

        vector_layer = tf.keras.layers.TextVectorization(
            max_tokens=vocab_size, 
            output_mode='int', 
            output_sequence_length=output_sequence_length,
            standardize=None,
            split='whitespace'
        )

        vector_layer.adapt(train_ds.map(lambda x, y: x))
        voc = vector_layer.get_vocabulary()

        x = vector_layer(input_layer)

        state = BLANK_DESCRIPTION
        if embedding_dictionary is not None:
            word_index = dict(zip(voc, range(len(voc))))
            embedding_matrix, num_tokens, stats = prepare_embedding_matrix(word_index, embedding_dictionary, embedding_dim)
            x = tf.keras.layers.Embedding(num_tokens, embedding_dim, embeddings_initializer=tf.keras.initializers.Constant(embedding_matrix), trainable=trainable)(x)
        else:
            x = tf.keras.layers.Embedding(len(voc), embedding_dim, trainable=trainable)(x)

        return x, input_layer, stats
