import typing

import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from transformers import AutoConfig, TFAutoModel

from src.encoder.create_encoder_from_path import create_encoder_from_path
from src.models.transformer.bert_pooling_layer import BertPoolingLayer
from src.models.transformer.pooling_strategy import (
    TransformerPoolingStrategySelection, pooling_strategy_dictionary)
from src.tokenizers.prepare_dataset_from_tokenizer import \
    prepare_dataset_from_tokenizer
from src.tokenizers.transformer_tokenizer import TransformerTokenizer
from src.types.transformer_name import TransformerName
from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy


class TransformerVectorizer:
    def __init__(
        self,
        transformer_type: TransformerName,
        transformer_pooling_type: TransformerPooling,
        path_authors: typing.Union[None, str] = None,
        encoder: typing.Union[None, typing.Type[LabelEncoder]] = None,
        max_len: typing.Union[None, int] = None,
        preprocess_pipeline=typing.Union[None, typing.Callable[[str], str]],
        transformer_pooling_strategy: TransformerPoolingStrategy = TransformerPoolingStrategy.Blank,
        transformer_start_index: typing.Union[int, typing.Callable[[int], int]] = -1,
        transformer_end_index: typing.Union[int, typing.Callable[[int], int]] = -1,
    ) -> None:
        self.transformer_pooling_strategy = transformer_pooling_strategy
        self.transformer_start_index = transformer_start_index
        self.transformer_end_index = transformer_end_index
        self.transformer_type = transformer_type.value
        self.transformer_pooling_type = transformer_pooling_type
        self.encoder = encoder
        self.max_len = max_len
        self.preprocess_pipeline = preprocess_pipeline
        self.path_to_authors = path_authors

    def setup(self) -> None:
        """Run setup on current vectorizer according to transformer type. To self state will be saved downloaded tokenizer and transformer.
        """
        self.config = AutoConfig.from_pretrained(
            self.transformer_type, output_hidden_states=True
        )
        self.transformer = TFAutoModel.from_config(self.config)
        encoder = (
            None
            if self.path_to_authors is None
            else create_encoder_from_path(self.path_to_authors)
        )
        self.tokenizer = TransformerTokenizer(
            self.transformer_type, encoder, self.max_len
        )

    def fit_transform(self, dataset: typing.Type[tf.data.Dataset]):
        """Will be downloaded specified transformer and tokenizer. Then input will be iterated and transformed to number vectors.

        Args:
            dataset (typing.Type[tf.data.Dataset]): TensorFlow dataset with textual_data:id

        Returns:
            _type_: X, y
        """
        self.setup()
        sentence_embedding = []
        labels = []

        for x in prepare_dataset_from_tokenizer(dataset, self.tokenizer).batch(1):
            transformer_input, label = x
            output = self.transformer(transformer_input)

            output = BertPoolingLayer()(
                output,
                self.transformer_pooling_type,
                self.transformer_pooling_strategy,
                self.transformer_start_index,
                self.transformer_end_index,
            )

            output = output.numpy().reshape(-1)
            label = label.numpy()[0]

            labels.append(label)
            sentence_embedding.append(output)
        return np.array(sentence_embedding), np.array(labels)

    def get_transformer_name(self) -> str:
        return self.transformer_type

    def get_transformer_pooling(self) -> str:
        return self.transformer_pooling_type.value

    def get_transformer_start_index(
        self,
    ) -> typing.Union[int, typing.Callable[[int], int]]:
        return self.transformer_start_index

    def get_transformer_end_index(
        self,
    ) -> typing.Union[int, typing.Callable[[int], int]]:
        return self.transformer_end_index

    def get_transformer_pooling_strategy(self) -> str:
        return self.transformer_pooling_strategy.value

    def get_len(self) -> int:
        return self.max_len

    def verify(
        self,
        transformer_pooling,
        transformer_pooling_strategy,
        transformer_start_index,
        transformer_end_index,
    ) -> bool:
        return True

    def set_pooling_strategy(
        self, pooling_strategy: TransformerPoolingStrategySelection
    ):
        print(f"Setting pooling strategy {pooling_strategy}")
        (
            transformer_pooling,
            transformer_pooling_strategy,
            transformer_start_index,
            transformer_end_index,
        ) = pooling_strategy_dictionary[pooling_strategy]

        if self.verify(
            transformer_pooling,
            transformer_pooling_strategy,
            transformer_start_index,
            transformer_end_index,
        ):
            self.transformer_pooling_strategy = transformer_pooling_strategy
            self.transformer_start_index = transformer_start_index
            self.transformer_end_index = transformer_end_index
            self.transformer_pooling_type = transformer_pooling
