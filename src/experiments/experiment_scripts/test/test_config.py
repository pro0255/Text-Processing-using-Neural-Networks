from src.config.learning_config import LOSS, METRIC, OPTIMIZER
from src.data_loading.experiment_loader import ExperimentLoader
from src.experiments.experiment_scripts.experiment_configurations.lookup import (
    LOOKUP_KEY,
)
from src.experiments.experiment_scripts.types.experiment_types import ExperimentType
from src.experiments.settings.settings import settings_generator
from src.models.classic.kneighbors import KNeighborsClassifier
from src.models.classic.linear import SGDClassifier
from src.models.classic.naive_bayes import GaussianNB
from src.models.classic.random_forest import RandomForestClassifier
from src.models.nets.cnn import CNNArchitecture
from src.models.nets.dense import DenseArchitecture
from src.models.nets.nets_configuration_generator import nets_configuration_generator
from src.models.nets.rnn import RNNArchitecture
from src.models.transformer.pooling_strategy import TransformerPoolingStrategySelection
from src.models.transformer.transformer_configuration_generator import (
    transformer_configuration_generator,
)
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType
from src.types.experiment_generator_part_type import ExperimentGeneratorPart
from src.types.processing_type import PreprocessingType
from src.types.transformer_name import TransformerName
from src.utils.coss_sim import coss_similarity
from src.vectorizers.classic.bow_vectorizer import BoWVectorizer
from src.vectorizers.classic.tfidf_vectorizer import TFIDFVectorizer
from src.vectorizers.embedding.glove_vectorizer import GloveVectorizer
from src.vectorizers.embedding.word2vec_vectorizer import Word2VecVectorizer
from src.vectorizers.transformer.bert_base_vectorizer import BertBaseUncasedVectorizer
from src.vectorizers.transformer.distil_bert_base_vectorizer import (
    DistilBertBaseUncasedVectorizer,
)
from src.vectorizers.transformer.electra_small_vectorizer import ElectraSmallVectorizer

"""Definition of values for test experiments.
"""

loader = ExperimentLoader()

AUTHORS_TEST = [5]
SENTENCES_TEST = [3]
LABEL_SIZE_TEST = [100]
EPOCHS_TEST = [1]
PREPROCESSING_TEST = [PreprocessingType.CaseInterpunction]
SEQ_LEN_TEST = [50]


test_experiment_config = {
    ExperimentType.TransformerTest: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            AUTHORS_TEST, SENTENCES_TEST, PREPROCESSING_TEST, LABEL_SIZE_TEST
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            SEQ_LEN_TEST,
            [True, False],
            list(
                settings_generator(
                    [64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], EPOCHS_TEST
                )
            ),
        ),
    },
    ExperimentType.NNTest: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            AUTHORS_TEST, SENTENCES_TEST, PREPROCESSING_TEST, LABEL_SIZE_TEST
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            SEQ_LEN_TEST,
            [LOOKUP_KEY],
            [True, False],
            list(
                settings_generator(
                    [64], [0.001], [METRIC], [LOSS], [OPTIMIZER], EPOCHS_TEST
                )
            ),
            [
                (50, None),
                (150, None),
                (300, None),
                (300, DownloadedEmbeddingType.Word2Vec),
                (300, DownloadedEmbeddingType.Glove),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
            RNNArchitecture(),
            DenseArchitecture(),
        ],
    },
    ExperimentType.ClassicTest: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            AUTHORS_TEST, SENTENCES_TEST, PREPROCESSING_TEST, LABEL_SIZE_TEST
        ),
        ExperimentGeneratorPart.FeatureExtractors: [
            BoWVectorizer(),
            TFIDFVectorizer(),
            GloveVectorizer(),
            Word2VecVectorizer(),
            ElectraSmallVectorizer(),
            BertBaseUncasedVectorizer(),
            DistilBertBaseUncasedVectorizer(),
        ],
        ExperimentGeneratorPart.Predictor: [
            GaussianNB(),
            SGDClassifier(),
            RandomForestClassifier(),
            KNeighborsClassifier(n_neighbors=5, metric=coss_similarity),
        ],
        ExperimentGeneratorPart.TransformerPoolingStrategy: None,
    },
}
