import tensorflow as tf
from src.models.nets.nn import NNArchitecture
from src.types.net_type import NetType


class RNNArchitecture(NNArchitecture):
    def __init__(self) -> None:
        super().__init__("RNNBidirectionalLSTMAndGru")

    def get_net_type(self):
        return NetType.LSTM.value

    def create_model(
        self,
        number_of_authors,
        train_ds,
        valid_ds,
        vocab_size,
        embedding_dim,
        output_sequence_length,
        trainable,
        embedding_dictionary=None,
    ):

        emb, input_layer, stats = self.emb.create_vect_embedding(
            train_ds,
            valid_ds,
            vocab_size,
            output_sequence_length,
            trainable,
            embedding_dim,
            embedding_dictionary,
        )

        x = tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(
                64,
                activation="relu",
                return_sequences=True,
                dropout=0.2,
                recurrent_dropout=0.2,
            )
        )(emb)
        x = tf.keras.layers.GRU(64, activation="relu", return_sequences=False)(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(0.2)(x)
        x = tf.keras.layers.Dense(32, "relu")(x)
        x = tf.keras.layers.Dropout(0.3)(x)
        x = tf.keras.layers.Dense(64, "relu")(x)
        output_layer = tf.keras.layers.Dense(number_of_authors, "softmax")(x)

        model = tf.keras.Model(input_layer, output_layer, name=self.model_name)

        return model, stats
