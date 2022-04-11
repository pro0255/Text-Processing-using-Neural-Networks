import json
import typing

from src.config.config import BLANK_DESCRIPTION
from src.experiments.descriptions.create_description import \
    create_description_for_nn
from src.models.embedding.embedding import Embedding
from src.types.net_type import NetType
from src.types.processing_type import PreprocessingType


class NNArchitecture:
    def __init__(self, model_name=BLANK_DESCRIPTION) -> None:
        self.emb = Embedding()
        self.model_name = model_name

    def get_description(
        self,
        experiment_id,
        experiment_type,
        number_of_authors,
        number_of_sentences,
        normalization_size,
        seq_len,
        trainable,
        path_data,
        learning_settings,
        embedding_type,
        vocab_size=0,
        embedding_size=0,
        embedding_name=BLANK_DESCRIPTION,
        preprocessing_type=PreprocessingType.Default.value,
    ):
        return create_description_for_nn(
            experiment_id,
            experiment_type,
            number_of_authors,
            number_of_sentences,
            normalization_size,
            seq_len,
            trainable,
            path_data,
            self.get_net_type(),
            learning_settings,
            embedding_type,
            json.dumps(
                self.get_extra_field(vocab_size, embedding_size, embedding_name)
            ),
            preprocessing_type=preprocessing_type,
        )

    def create_model(
        self,
        number_of_authors:int,
        train_ds,
        valid_ds,
        vocab_size:int,
        embedding_dim:int,
        output_sequence_length:int,
        trainable:bool,
        embedding_dictionary=typing.Union[typing.Dict, None],
    ) -> typing.Union[typing.Tuple, None]:
        return None

    def get_name(self):
        return self.model_name

    def get_net_type(self):
        return NetType.Blank.value

    def get_extra_field(self, vocab_size=0, embedding_size=0, name_of_embedding=None):
        return {
            "ModelName": self.model_name,
            "VocabSize": str(vocab_size),
            "EmbeddingSize": str(embedding_size),
            "NameOfEmbedding": BLANK_DESCRIPTION
            if name_of_embedding is None
            else name_of_embedding.value,
        }
