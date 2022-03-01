import os
from src.config.config import get_current_folder
from src.models.classic.linear import LinearClassifier
from src.models.classic.naive_bayes import NaiveBayes
from src.models.classic.random_forest import RandomForest
from src.vectorizers.classic.bow_vectorizer import BoWVectorizer
from src.vectorizers.classic.tfidf_vectorizer import TfidfVectorizer
from src.vectorizers.transformer.bert_base_vectorizer import BertBaseUncasedVectorizer
from src.vectorizers.transformer.distil_bert_base_vectorizer import DistilBertBaseUncasedVectorizer
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
from src.experiments.instances.classic_model_with_vectorizer import ClassicModelWithVectorizerExperiment
from src.experiments.experiment_configuration import ExperimentConfiguration
from src.utils.split_dataframe import split_dataframe
from src.utils.normalize_dataframe_to_size import normalize_dataframe_to_size
from src.utils.create_dataset_from_dataframe import create_dataset_from_Xy
from src.experiments.descriptions.create_description import create_description_for_classic


NAME_OF_EXPERIMENT = "ClassicAndVectorizer"

class ClassicModelAndVectorizer:
    def __init__(self, number_of_authors, number_of_sentences) -> None:
        self.number_of_authors = number_of_authors
        self.number_of_sentences = number_of_sentences


    def create_experiment_id(self, args):
        current_timestamp = time.time()
        current_experiment_id = args[0] + os.path.sep + f"stamp:{str(current_timestamp)}"
        return (*args, current_experiment_id)


    def experiments_generator(self):
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            RandomForest(),
            BoWVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            NaiveBayes(),
            BoWVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            LinearClassifier(),
            BoWVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            RandomForest(),
            TfidfVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            NaiveBayes(),
            TfidfVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            LinearClassifier(),
            TfidfVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            RandomForest(),
            GloveVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            NaiveBayes(),
            GloveVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            LinearClassifier(),
            GloveVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            RandomForest(),
            Word2VecVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            NaiveBayes(),
            Word2VecVectorizer())
        )
        yield self.create_experiment_id(
            (NAME_OF_EXPERIMENT,
            30000,
            self.number_of_authors,
            self.number_of_sentences,
            LinearClassifier(),
            Word2VecVectorizer())
        )
        

    def run(self):
        data, paths = get_dataset_all(self.number_of_authors, self.number_of_sentences)
        all_data = from_dataset_dataframe(data[0])

        for value in self.experiments_generator():
            experiment_type, normalize_value, number_of_authors, number_of_sentences, prediction_instance, vectorizer_instance, experiment_id = value
            
            print(f"Experiment id {experiment_id}")

            description = create_description_for_classic(
                experiment_id,
                experiment_type,
                number_of_authors,
                number_of_sentences,
                prediction_instance,
                vectorizer_instance,
                normalize_value,
                paths[0]
            )

            data_normalized = normalize_dataframe_to_size(all_data, normalize_value)
            X_train, X_test, y_train, y_test = split_dataframe(data_normalized)
            train_ds = create_dataset_from_Xy(X_train, y_train)
            test_ds = create_dataset_from_Xy(X_test, y_test)

            conf = ExperimentConfiguration(
                train=train_ds, 
                test=test_ds, 
                experiment_id=experiment_id, 
                description=description, 
                predict_instance=prediction_instance, 
                vectorization_instance=vectorizer_instance
            )
            experiment = ClassicModelWithVectorizerExperiment()
            experiment.run(conf)