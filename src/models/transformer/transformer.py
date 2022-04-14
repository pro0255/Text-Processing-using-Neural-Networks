import typing

import tensorflow as tf
from transformers import AutoConfig, TFAutoModel

from src.models.transformer.bert_pooling_layer import BertPoolingLayer
from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy


class TransformerArchitecture:
    def __init__(self) -> None:
        pass

    def create_model(
        self,
        number_of_authors: int,
        model_name: str,
        output_sequence_length: int,
        trainable: bool,
        pooling_type: TransformerPooling,
        transformer_pooling_strategy: typing.Union[
            None, TransformerPoolingStrategy
        ] = None,
        transformer_start_index: typing.Union[
            int, typing.Callable[[int], int]
        ] = lambda x: 0,
        transformer_end_index: typing.Union[
            int, typing.Callable[[int], int]
        ] = lambda x: 0,
    ):
        print(f"Creating model with name={model_name}")
        config = AutoConfig.from_pretrained(model_name, output_hidden_states=True)
        transformer_model = TFAutoModel.from_config(config)

        input_ids = tf.keras.layers.Input(
            shape=(output_sequence_length,), dtype=tf.int32, name="input_ids"
        )
        attention_mask = tf.keras.layers.Input(
            (output_sequence_length,), dtype=tf.int32, name="attention_mask"
        )

        output = transformer_model([input_ids, attention_mask])

        transformer_vectors = BertPoolingLayer()(
            output,
            pooling_type,
            transformer_pooling_strategy,
            transformer_start_index,
            transformer_end_index,
        )

        output = tf.keras.layers.Dropout(rate=0.15)(transformer_vectors)
        output = tf.keras.layers.Dense(units=64, activation="relu")(output)
        output = tf.keras.layers.BatchNormalization()(output)
        output = tf.keras.layers.Dense(units=64, activation="relu")(output)
        output = tf.keras.layers.BatchNormalization()(output)
        output_layer = tf.keras.layers.Dense(
            units=number_of_authors, activation="softmax"
        )(output)
        model = tf.keras.Model(
            inputs=[input_ids, attention_mask],
            outputs=output_layer,
            name="TransformerDenseHead",
        )

        model.layers[2].trainable = trainable

        return model
