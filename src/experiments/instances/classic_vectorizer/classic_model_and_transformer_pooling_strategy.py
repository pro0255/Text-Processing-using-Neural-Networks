import os
from src.config.config import get_current_folder
from src.models.classic.linear import LinearClassifier
from src.models.classic.naive_bayes import NaiveBayes
from src.models.classic.random_forest import RandomForest
from src.vectorizers.classic.bow_vectorizer import BoWVectorizer
from src.vectorizers.classic.tfidf_vectorizer import TfidfVectorizer
from src.vectorizers.transformer.bert_base_vectorizer import BertBaseUncasedVectorizer
from src.vectorizers.transformer.distil_bert_base_vectorizer import (
    DistilBertBaseUncasedVectorizer,
)
from src.vectorizers.transformer.electra_small_vectorizer import ElectraSmallVectorizer
from src.vectorizers.embedding.glove_vectorizer import GloveVectorizer
from src.vectorizers.embedding.word2vec_vectorizer import Word2VecVectorizer
from src.config.config import BLANK_DESCRIPTION
from src.experiments.experiment_description import ExperimentDescription
from src.types.transformer_pooling import TransformerPooling
from src.types.prediction_model_type import PredictionModelType
from src.types.net_type import NetType
from src.types.embedding_type import EmbeddingType
from src.types.processing_type import PreprocessingType
import time
from src.data_loading.get_dataset_object_from import get_dataset_all
from src.utils.from_dataset_arrays import from_dataset_dataframe
from src.experiments.instances.classic_model_with_vectorizer import (
    ClassicModelWithVectorizerExperiment,
)
from src.experiments.experiment_configuration import ExperimentConfiguration
from src.utils.split_dataframe import split_dataframe
from src.utils.normalize_dataframe_to_size import normalize_dataframe_to_size
from src.utils.create_dataset_from_dataframe import create_dataset_from_Xy
from src.experiments.descriptions.create_description import (
    create_description_for_classic,
    create_description_for_transformer_with_classic,
)
from src.models.transformer.pooling_strategy import pooling_strategy_dictionary

NAME_OF_EXPERIMENT = "ClassicAndTransformerPoolingStrategy"


class ClassicModelAndTransformerPoolingStrategy:
    def __init__(self) -> None:
        pass

    def create_experiment_id(self):
        current_timestamp = time.time()
        current_experiment_id = (
            NAME_OF_EXPERIMENT + os.path.sep + f"stamp:{str(current_timestamp)}"
        )
        return current_experiment_id

    def transformer_vectorizer_generator(
        self, max_lenghts=[], transformer_vectorizers=[], pooling_strategies=[]
    ):
        for max_len in max_lenghts:
            for transformer_vectorizer in transformer_vectorizers:
                for strategy in pooling_strategies:
                    (
                        transformer_pooling_type,
                        transformer_pooling_strategy,
                        transformer_start_index,
                        transformer_end_index,
                    ) = pooling_strategy_dictionary[strategy]
                    yield (
                        transformer_vectorizer(
                            max_len=max_len,
                            transformer_pooling_type=transformer_pooling_type,
                            transformer_pooling_strategy=transformer_pooling_strategy,
                            transformer_start_index=transformer_start_index,
                            transformer_end_index=transformer_end_index,
                        )
                    )

    def run(
        self,
        number_of_authors,
        number_of_sentences,
        max_lengths=[],
        transformer_vectorizers=[],
        pooling_strategies=[],
        predictors_factory=[],
        normalize_value=None,
        all_data=None,
        data=None,
        paths=None,
    ):
        if all_data is None:
            data, paths = get_dataset_all(number_of_authors, number_of_sentences)
            all_data = from_dataset_dataframe(data[0])

        for value in self.transformer_vectorizer_generator(
            max_lengths, transformer_vectorizers, pooling_strategies
        ):

            transformer_vectorizer = value

            cache = None

            for predict_instance_factory in predictors_factory:

                current_predict_instance = predict_instance_factory()
                current_experiment_id = self.create_experiment_id()

                description = create_description_for_transformer_with_classic(
                    current_experiment_id,
                    NAME_OF_EXPERIMENT,
                    number_of_authors,
                    number_of_sentences,
                    current_predict_instance,
                    transformer_vectorizer,
                    normalize_value,
                    paths[0],
                )

                data_normalized = normalize_dataframe_to_size(all_data, normalize_value)
                X_train, X_test, y_train, y_test = split_dataframe(data_normalized)
                train_ds = create_dataset_from_Xy(X_train, y_train)
                test_ds = create_dataset_from_Xy(X_test, y_test)

                conf = ExperimentConfiguration(
                    train=train_ds,
                    test=test_ds,
                    experiment_id=current_experiment_id,
                    description=description,
                    predict_instance=current_predict_instance,
                    vectorization_instance=transformer_vectorizer,
                )

                experiment = ClassicModelWithVectorizerExperiment()
                cache = experiment.run(conf, cache)
