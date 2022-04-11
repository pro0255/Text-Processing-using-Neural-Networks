from src.config.config import BLANK_DESCRIPTION
from src.experiments.helpers.experiment_description import ExperimentDescription
from src.types.prediction_model_type import PredictionModelType
from src.types.net_type import NetType
from src.types.embedding_type import EmbeddingType
from src.types.processing_type import PreprocessingType
from src.types.classic_model_type import ClassicModelType
from src.models.transformer.pooling_strategy import MAX_FAKE_LAYERS


def from_pred_instance_get_type(prediction_instance):
    print(f"Current prediction instance {prediction_instance}")
    if not prediction_instance:
        return ""
    name_of_instance = type(prediction_instance).__name__
    dic = {
        "SGDClassifier": ClassicModelType.Linear.value,
        "GaussianNB": ClassicModelType.NaiveBayes.value,
        "RandomForestClassifier": ClassicModelType.RandomForest.value,
    }
    return dic.get(name_of_instance, BLANK_DESCRIPTION)


def from_vect_instance_get_type(vectorizer_instance):
    print(f"Current vectorizer instance {vectorizer_instance}")
    if not vectorizer_instance:
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
    return dic.get(name_of_vectorizer_instance, BLANK_DESCRIPTION)


def create_description_for_classic(
    experiment_id,
    experiment_type,
    number_of_authors,
    number_of_sentences,
    prediction_instance,
    vectorizer_instance,
    normalization_size,
    path_data,
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
    experiment_id,
    experiment_type,
    number_of_authors,
    number_of_sentences,
    prediction_instance,
    vectorizer_instance,
    normalization_size,
    path_data,
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
        transformer_start_index=transformer_start_index,
        transformer_end_index=transformer_end_index,
        transformer_pooling_strategy=transformer_pooling_strategy,
        normalization_size=normalization_size,
    )


def create_description_for_transformer(
    experiment_id,
    experiment_type,
    number_of_authors,
    number_of_sentences,
    model_name,
    pooling_strategy_arguments,
    seq_len,
    trainable,
    normalization_size,
    path_data,
    learning_settings,
    pooling_strategy,
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
    experiment_id,
    experiment_type,
    number_of_authors,
    number_of_sentences,
    normalization_size,
    seq_len,
    trainable,
    path_data,
    net_type,
    learning_settings,
    embedding_type,
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
        extra_field=extra_field
    )