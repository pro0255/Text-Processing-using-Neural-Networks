import typing

import tensorflow as tf

from src.models.nets.nn import NNArchitecture
from src.types.net_type import NetType


class RNNArchitecture(NNArchitecture):
    def __init__(self) -> None:
        super().__init__("RNNBidirectionalLSTMAndGru")

    def get_net_type(self) -> str:
        return NetType.LSTM.value

    def create_model(
        self,
        number_of_authors: int,
        train_ds: typing.Type[tf.data.Dataset],
        valid_ds: typing.Type[tf.data.Dataset],
        vocab_size: int,
        embedding_dim: int,
        output_sequence_length: int,
        trainable: bool,
        embedding_dictionary=typing.Union[typing.Dict, None],
    ) -> typing.Union[typing.Tuple[typing.Type[tf.keras.Model], typing.Tuple], None]:

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
                128,
                activation="relu",
                return_sequences=True,
                dropout=0.2,
                recurrent_dropout=0.2,
            )
        )(emb)
        x = tf.keras.layers.LSTM(128, activation="relu", return_sequences=False)(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(0.2)(x)
        x = tf.keras.layers.Dense(256, activation="relu")(x)
        x = tf.keras.layers.Dropout(rate=0.4)(x)
        x = tf.keras.layers.Dense(64, activation="relu")(x)
        x = tf.keras.layers.Dropout(rate=0.4)(x)
        x = tf.keras.layers.Dense(128, activation="relu")(x)
        x = tf.keras.layers.Dropout(rate=0.2)(x)
        output_layer = tf.keras.layers.Dense(number_of_authors, "softmax")(x)

        model = tf.keras.Model(input_layer, output_layer, name=self.model_name)

        return model, stats
