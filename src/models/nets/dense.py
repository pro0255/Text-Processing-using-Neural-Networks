import tensorflow as tf
from src.models.nets.nn import NNArchitecture
from src.types.net_type import NetType

class DenseArchitecture(NNArchitecture):
    def __init__(self) -> None:
        super().__init__(
            "Dense"
        )

    def get_net_type(self):
        return NetType.Dense.value

    def create_model(
        self,
        number_of_authors,
        train_ds,
        valid_ds,
        vocab_size,
        embedding_dim,
        output_sequence_length,
        trainable,
        embedding_dictionary=None
    ):

        emb, input_layer = self.emb.create_vect_embedding(
            train_ds,
            valid_ds,
            vocab_size,
            output_sequence_length,
            trainable,
            embedding_dim,
            embedding_dictionary
        )

        x = tf.keras.layers.Flatten()(emb)
        x = tf.keras.layers.Dense(64, activation='relu')(x)
        x = tf.keras.layers.Dropout(rate=0.2)(x)
        x = tf.keras.layers.Dense(32, activation='relu')(x)
        x = tf.keras.layers.Dropout(rate=0.4)(x)
        x = tf.keras.layers.Dense(64, activation='relu')(x)
        x = tf.keras.layers.Dropout(rate=0.2)(x)

        output_layer = tf.keras.layers.Dense(number_of_authors, activation='softmax')(x)

        model = tf.keras.Model(input_layer, output_layer)

        return model 
