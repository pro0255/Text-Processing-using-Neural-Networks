import typing

from src.config.config import BLANK_DESCRIPTION
from src.defined_types.types import PredictionClassesType, VectorizerClassesType
from src.experiments.helpers.experiment_description import ExperimentDescription
from src.experiments.settings.settings import LearningSettings
from src.models.transformer.pooling_strategy import (
    MAX_FAKE_LAYERS,
    TransformerPoolingStrategySelection,
)
from src.types.classic_model_type import ClassicModelType
from src.types.embedding_type import EmbeddingType
from src.types.net_type import NetType
from src.types.prediction_model_type import PredictionModelType
from src.types.processing_type import PreprocessingType
from src.types.transformer_name import TransformerName
from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy

"""Lot of helper methods which is used for creation of .csv objects.. Summarization, Descriptions etc. 
"""


def from_pred_instance_get_type(
    prediction_instance: typing.Union[PredictionClassesType, str]
):
    if prediction_instance == "":
        return ""
    name_of_instance = type(prediction_instance).__name__
    dic = {
        "SGDClassifier": ClassicModelType.Linear.value,
        "GaussianNB": ClassicModelType.NaiveBayes.value,
        "RandomForestClassifier": ClassicModelType.RandomForest.value,
        "KNeighborsClassifier": ClassicModelType.KNeighbors.value,
    }
    print(f"Current name of instance {name_of_instance} in {list(dic.items())}")
    return dic.get(name_of_instance, BLANK_DESCRIPTION)


def from_vect_instance_get_type(
    vectorizer_instance: typing.Union[VectorizerClassesType, str]
):
    if vectorizer_instance == "":
        return ""
    name_of_vectorizer_instance = type(vectorizer_instance).__name__
    dic = {
        "CountVectorizer": EmbeddingType.BoW.value,
        "TfidfVectorizer": EmbeddingType.TfIdf.value,
        "GloveVectorizer": EmbeddingType.Glove.value,
        "Word2VecVectorizer": EmbeddingType.W2V.value,
        "BertBaseUncasedVectorizer": EmbeddingType.Transformer.value,
        "DistilBertBaseUncasedVectorizer": EmbeddingType.Transformer.value,
        "ElectraSmallVectorizer": EmbeddingType.Transformer.value,
    }
    print(
        f"Current name of vectorizer {name_of_vectorizer_instance} in {list(dic.items())}"
    )
    return dic.get(name_of_vectorizer_instance, BLANK_DESCRIPTION)


def create_description_for_classic(
    experiment_id: str,
    experiment_type: str,
    number_of_authors: int,
    number_of_sentences: int,
    prediction_instance: typing.Union[PredictionClassesType, str],
    vectorizer_instance: typing.Union[VectorizerClassesType, str],
    normalization_size: int,
    path_data: str,
    preprocessing_type=PreprocessingType.Default.value,
):
    classic_model_type = from_pred_instance_get_type(prediction_instance)
    vectorizer_model_type = from_vect_instance_get_type(vectorizer_instance)

    return ExperimentDescription(
        experiment_id=experiment_id,
        experiment_type=experiment_type,
        learning_settings=None,
        transformer_name=BLANK_DESCRIPTION,
        transformer_pooling=BLANK_DESCRIPTION,
        prediction_model_type=PredictionModelType.Classic.value,
        net_type=NetType.Blank.value,
        embedding_type=vectorizer_model_type,
        trainable=True,
        preprocessing_type=preprocessing_type,
        number_of_authors=number_of_authors,
        number_of_sentences=number_of_sentences,
        load_path=path_data,
        seq_len=BLANK_DESCRIPTION,
        is_test=str(False),
        classic_model_name=classic_model_type,
        extra_field=BLANK_DESCRIPTION,
        transformer_start_index=BLANK_DESCRIPTION,
        transformer_end_index=BLANK_DESCRIPTION,
        transformer_pooling_strategy=BLANK_DESCRIPTION,
        normalization_size=normalization_size,
    )


def create_description_for_transformer_with_classic(
    experiment_id: str,
    experiment_type: str,
    number_of_authors: int,
    number_of_sentences: int,
    prediction_instance: typing.Union[PredictionClassesType, str],
    vectorizer_instance: typing.Union[VectorizerClassesType, str],
    normalization_size: int,
    path_data: str,
    preprocessing_type=PreprocessingType.Default.value,
):
    classic_model_type = from_pred_instance_get_type(prediction_instance)
    vectorizer_model_type = from_vect_instance_get_type(vectorizer_instance)

    transformer_name = vectorizer_instance.get_transformer_name()
    transformer_pooling = vectorizer_instance.get_transformer_pooling()
    transformer_start_index = vectorizer_instance.get_transformer_start_index()
    transformer_end_index = vectorizer_instance.get_transformer_end_index()
    transformer_pooling_strategy = (
        vectorizer_instance.get_transformer_pooling_strategy()
    )
    le = vectorizer_instance.get_len()

    return ExperimentDescription(
        experiment_id=experiment_id,
        experiment_type=experiment_type,
        learning_settings=None,
        transformer_name=transformer_name,
        transformer_pooling=transformer_pooling,
        prediction_model_type=PredictionModelType.Classic.value,
        net_type=NetType.Blank.value,
        embedding_type=vectorizer_model_type,
        trainable=True,
        preprocessing_type=preprocessing_type,
        number_of_authors=number_of_authors,
        number_of_sentences=number_of_sentences,
        load_path=path_data,
        seq_len=le,
        is_test=str(False),
        classic_model_name=classic_model_type,
        extra_field=BLANK_DESCRIPTION,
        transformer_start_index=transformer_start_index(MAX_FAKE_LAYERS),
        transformer_end_index=transformer_end_index(MAX_FAKE_LAYERS),
        transformer_pooling_strategy=transformer_pooling_strategy,
        normalization_size=normalization_size,
    )


def create_description_for_transformer(
    experiment_id: str,
    experiment_type: str,
    number_of_authors: int,
    number_of_sentences: int,
    model_name: TransformerName,
    pooling_strategy_arguments: typing.Tuple[
        TransformerPooling,
        TransformerPoolingStrategy,
        typing.Union[int, typing.Callable[[int], int]],
        typing.Union[int, typing.Callable[[int], int]],
    ],
    seq_len: int,
    trainable: bool,
    normalization_size: int,
    path_data: str,
    learning_settings: typing.Type[LearningSettings],
    pooling_strategy: TransformerPoolingStrategySelection,
    preprocessing_type=PreprocessingType.Default.value,
):
    (
        transformer_pooling,
        transformer_pooling_strategy,
        transformer_start_index,
        transformer_end_index,
    ) = pooling_strategy_arguments

    return ExperimentDescription(
        experiment_id=experiment_id,
        experiment_type=experiment_type,
        learning_settings=learning_settings,
        transformer_name=model_name.value,
        transformer_pooling=transformer_pooling.value,
        prediction_model_type=PredictionModelType.NeuralNet.value,
        net_type=NetType.Dense.value,
        embedding_type=EmbeddingType.Transformer.value,
        trainable=trainable,
        preprocessing_type=preprocessing_type,
        number_of_authors=number_of_authors,
        number_of_sentences=number_of_sentences,
        load_path=path_data,
        seq_len=seq_len,
        is_test=str(False),
        classic_model_name=BLANK_DESCRIPTION,
        extra_field=pooling_strategy.value,
        transformer_start_index=transformer_start_index(MAX_FAKE_LAYERS),
        transformer_end_index=transformer_end_index(MAX_FAKE_LAYERS),
        transformer_pooling_strategy=BLANK_DESCRIPTION
        if transformer_pooling_strategy is None
        else transformer_pooling_strategy.value,
        normalization_size=normalization_size,
    )


def create_description_for_nn(
    experiment_id: str,
    experiment_type: str,
    number_of_authors: int,
    number_of_sentences: int,
    normalization_size: int,
    seq_len: int,
    trainable: bool,
    path_data: str,
    net_type: str,
    learning_settings: typing.Type[LearningSettings],
    embedding_type: EmbeddingType,
    extra_field,
    preprocessing_type=PreprocessingType.Default.value,
):

    return ExperimentDescription(
        experiment_id=experiment_id,
        experiment_type=experiment_type,
        learning_settings=learning_settings,
        transformer_name=BLANK_DESCRIPTION,
        transformer_pooling=BLANK_DESCRIPTION,
        prediction_model_type=PredictionModelType.NeuralNet.value,
        net_type=net_type,
        embedding_type=embedding_type.value,
        trainable=trainable,
        preprocessing_type=preprocessing_type,
        number_of_authors=number_of_authors,
        number_of_sentences=number_of_sentences,
        load_path=path_data,
        seq_len=seq_len,
        is_test=False,
        classic_model_name=BLANK_DESCRIPTION,
        transformer_start_index=BLANK_DESCRIPTION,
        transformer_end_index=BLANK_DESCRIPTION,
        transformer_pooling_strategy=BLANK_DESCRIPTION,
        normalization_size=normalization_size,
        extra_field=extra_field,
    )
