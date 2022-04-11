import typing
import tensorflow as tf

from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy


def verify_bert_pooling_input(
    pooling_type: TransformerPooling,
    transformer_pooling_strategy: typing.Union[None, TransformerPoolingStrategy]=None,
    transformer_start_index:typing.Union[int, typing.Callable[[int], int]]=-1,
    transformer_end_index:typing.Union[int, typing.Callable[[int], int]]=-1,
):
    if pooling_type in [
        TransformerPooling.LastHiddenState,
        TransformerPooling.Pooler,
    ] and (
        transformer_pooling_strategy is not None
        or transformer_start_index != -1
        or transformer_end_index != -1
    ):
        assert Exception(
            f"Cannot use pooling strategy when is not used {TransformerPooling.HiddenStates.value}"
        )
        return None


class BertPoolingLayer(tf.keras.layers.Layer):
    def call(
        self,
        inputs,
        pooling_type: TransformerPooling,
        transformer_pooling_strategy:typing.Union[None, TransformerPoolingStrategy]=None,
        transformer_start_index:typing.Union[int, typing.Callable[[int], int]]=lambda x: 0,
        transformer_end_index:typing.Union[int, typing.Callable[[int], int]]=lambda x: 0,
    ):
        verify_bert_pooling_input(
            pooling_type,
            transformer_pooling_strategy,
            transformer_start_index,
            transformer_end_index,
        )

        if pooling_type == TransformerPooling.LastHiddenState:
            last_hidden_state = inputs[TransformerPooling.LastHiddenState.value]
            return tf.reduce_mean(last_hidden_state, axis=1)

        if pooling_type == TransformerPooling.Pooler:
            pooler = inputs[TransformerPooling.Pooler.value]
            return pooler

        if pooling_type == TransformerPooling.HiddenStates:
            selector = inputs[TransformerPooling.HiddenStates.value]

            number_of_layers = len(selector) - 1
            index_start_from_behind = number_of_layers - transformer_start_index(
                number_of_layers
            )
            index_end_from_behind = (
                number_of_layers - transformer_end_index(number_of_layers) + 1
            )

            selector = selector[index_start_from_behind:index_end_from_behind]

            if transformer_pooling_strategy in [
                TransformerPoolingStrategy.ConcatAverage,
                TransformerPoolingStrategy.ConcatCLS,
            ]:
                concatened = tf.concat(selector, axis=2)

                if transformer_pooling_strategy == TransformerPoolingStrategy.ConcatCLS:
                    cls = concatened[:, 0, :]
                    return cls
                else:
                    averaged_sentence = tf.reduce_mean(concatened, axis=1)
                    return averaged_sentence
            else:
                tf_tensor = tf.convert_to_tensor(selector)
                averaged = tf.reduce_mean(tf_tensor, axis=0)
                if transformer_pooling_strategy == TransformerPoolingStrategy.CLS:
                    cls = averaged[:, 0, :]
                    return cls
                else:
                    averaged_sentence = tf.reduce_mean(averaged, axis=1)
                    return averaged_sentence
