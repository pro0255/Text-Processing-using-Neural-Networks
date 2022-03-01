from src.config.config import USE_TESTING_DATASET_FOLDER, BLANK_DESCRIPTION
from src.experiments.experiment_description import ExperimentDescription
from src.types.transformer_pooling import TransformerPooling
from src.types.prediction_model_type import PredictionModelType
from src.types.net_type import NetType
from src.types.embedding_type import EmbeddingType
from src.types.processing_type import PreprocessingType
from src.types.classic_model_type import ClassicModelType


def from_pred_instance_get_type(prediction_instance):
    name_of_instance = type(prediction_instance).__name__
    dic = {
        "SGDClassifier": ClassicModelType.Linear.value,
        "GaussianNB": ClassicModelType.NaiveBayes.value,
        "RandomForestClassifier": ClassicModelType.RandomForest.value,
    }
    return dic[name_of_instance]


def from_vect_instance_get_type(vectorizer_instance):
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
    return dic[name_of_vectorizer_instance]


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
        transformer_name=BLANK_DESCRIPTION,  # here
        transformer_pooling=BLANK_DESCRIPTION,  # here
        prediction_model_type=PredictionModelType.Classic.value,
        net_type=NetType.Blank.value,
        embedding_type=vectorizer_model_type,
        trainable=True,
        preprocessing_type=preprocessing_type,
        number_of_authors=number_of_authors,
        number_of_sentences=number_of_sentences,
        load_path=path_data,
        seq_len=BLANK_DESCRIPTION,  # here
        is_test=USE_TESTING_DATASET_FOLDER,
        classic_model_name=classic_model_type,
        extra_field=BLANK_DESCRIPTION,
        transformer_start_index=BLANK_DESCRIPTION,  # here
        transformer_end_index=BLANK_DESCRIPTION,  # here
        transformer_pooling_strategy=BLANK_DESCRIPTION,  # here
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
        is_test=USE_TESTING_DATASET_FOLDER,
        classic_model_name=classic_model_type,
        extra_field=BLANK_DESCRIPTION,
        transformer_start_index=transformer_start_index,
        transformer_end_index=transformer_end_index,
        transformer_pooling_strategy=transformer_pooling_strategy,
        normalization_size=normalization_size,
    )
