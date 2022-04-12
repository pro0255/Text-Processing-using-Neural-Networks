import typing

import tensorflow as tf

from src.tokenizers.transformer_tokenizer import TransformerTokenizer


def prepare_dataset_from_tokenizer(
    dataset: typing.Type[tf.data.Dataset], tokenizer: typing.Type[TransformerTokenizer]
):
    return dataset.map(tokenizer.ty_py_func).map(tokenizer.to_model_input)
