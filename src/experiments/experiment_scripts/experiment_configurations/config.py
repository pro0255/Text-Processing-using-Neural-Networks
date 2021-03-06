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
from sklearn.metrics.pairwise import cosine_similarity

"""Configurations for specific experiments.
"""


loader = ExperimentLoader()


experiment_config = {
    ExperimentType.TrainableTransformer: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True, False],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.PreprocessingTransformer: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [
                PreprocessingType.CaseInterpunction,
                PreprocessingType.Default,
                PreprocessingType.Raw,
            ],
            [10000],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True],
            list(settings_generator([128], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [3])),
        ),
    },
    ExperimentType.PoolingStrategyTransformer: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            list(TransformerPoolingStrategySelection),
            [130],
            [True],
            list(settings_generator([64], [2e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.OutputSequenceLengthTransformer: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            list(range(50, 300, 30)),
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.LearningRateTransformer: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased, TransformerName.ElectraBase],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True],
            list(
                settings_generator(
                    [64],
                    [0.001, 2e-5, 3e-5, 4e-5, 5e-5],
                    [METRIC],
                    [LOSS],
                    [OPTIMIZER],
                    [3],
                )
            ),
        ),
    },
    ExperimentType.TransformerType: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [
                # TransformerName.DistilBertBaseUncased,
                TransformerName.ElectraBase,
                TransformerName.BertBaseUncased,
            ],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True],
            list(
                settings_generator(
                    [64], [2e-5, 5e-5], [METRIC], [LOSS], [OPTIMIZER], [5]
                )
            ),
        ),
    },
    ExperimentType.LabelSizeTransformer: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            list(range(5000, 30000, 5000)),
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [3])),
        ),
    },
    ExperimentType.NumberOfAuthorsNN: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            [100],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [15000],
            [LOOKUP_KEY],
            [True, False],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
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
    ExperimentType.EmbeddingSizeNN: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            [15000],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [15000],
            [LOOKUP_KEY],
            [True],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
            ),
            [
                (50, None),
                (100, None),
                (150, None),
                (200, None),
                (300, None),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
            DenseArchitecture(),
        ],
    },
    ExperimentType.Classic: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            [15000],
        ),
        ExperimentGeneratorPart.FeatureExtractors: [
            BoWVectorizer(lowercase=False, max_features=10000),
            TFIDFVectorizer(lowercase=False, max_features=10000),
            GloveVectorizer(),
            Word2VecVectorizer(),
            ElectraSmallVectorizer(),
            BertBaseUncasedVectorizer(),
            DistilBertBaseUncasedVectorizer(),
        ],
        ExperimentGeneratorPart.Predictor: [
            GaussianNB(),
            SGDClassifier(),
            RandomForestClassifier(n_estimators=100),
            KNeighborsClassifier(
                algorithm="auto",
                n_neighbors=5,
                metric="euclidean",  # coss_similarity
                n_jobs=-1,
            ),
        ],
        ExperimentGeneratorPart.TransformerPoolingStrategy: None,
    },
    ExperimentType.ClassicLogisticRegressionLabelSize: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            list(range(5000, 30000, 5000)),
        ),
        ExperimentGeneratorPart.FeatureExtractors: [
            BoWVectorizer(lowercase=False, max_features=10000),
        ],
        ExperimentGeneratorPart.Predictor: [
            SGDClassifier(),
        ],
        ExperimentGeneratorPart.TransformerPoolingStrategy: None,
    },
    ExperimentType.ClassicLogisticRegressionPreprocessing: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [
                PreprocessingType.CaseInterpunction,
                PreprocessingType.Default,
                PreprocessingType.Lowercase,
                PreprocessingType.Raw,
            ],
            [15000],
        ),
        ExperimentGeneratorPart.FeatureExtractors: [
            BoWVectorizer(lowercase=False, max_features=10000),
        ],
        ExperimentGeneratorPart.Predictor: [
            SGDClassifier(),
        ],
        ExperimentGeneratorPart.TransformerPoolingStrategy: None,
    },
    ExperimentType.Classic5SentencesCombinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [1, 2, 3, 7, 10, 15],
            [
                PreprocessingType.CaseInterpunction,
            ],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.FeatureExtractors: [
            BoWVectorizer(lowercase=False, max_features=10000),
        ],
        ExperimentGeneratorPart.Predictor: [
            SGDClassifier(),
        ],
        ExperimentGeneratorPart.TransformerPoolingStrategy: None,
    },
    ExperimentType.Classic310Combinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [55, 75, 105],  # 5, 15, 25
            [3, 10],
            [
                PreprocessingType.CaseInterpunction,
            ],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.FeatureExtractors: [
            BoWVectorizer(lowercase=False, max_features=10000),
            TFIDFVectorizer(lowercase=False, max_features=10000),
            GloveVectorizer(),
            Word2VecVectorizer(),
        ],
        ExperimentGeneratorPart.Predictor: [
            GaussianNB(),
            SGDClassifier(),
            RandomForestClassifier(n_estimators=100),
            KNeighborsClassifier(
                algorithm="auto",
                n_neighbors=5,
                metric="euclidean",  # coss_similarity
                n_jobs=-1,
            ),
        ],
        ExperimentGeneratorPart.TransformerPoolingStrategy: None,
    },
    ExperimentType.NN310Combinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5, 15, 25],
            [3, 10],
            [PreprocessingType.CaseInterpunction],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [60000],
            [LOOKUP_KEY],
            [True],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
            ),
            [
                (50, None),
                (150, None),
                (200, None),
                (300, DownloadedEmbeddingType.Word2Vec),
                (300, DownloadedEmbeddingType.Glove),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
            DenseArchitecture(),
            RNNArchitecture(),
        ],
    },
    ExperimentType.NN5SentencesCombinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [1, 2, 3, 7, 10, 15],
            [PreprocessingType.CaseInterpunction],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [60000],
            [LOOKUP_KEY],
            [True],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
            ),
            [
                (50, None),
                (150, None),
                (200, None),
                (300, DownloadedEmbeddingType.Word2Vec),
                (300, DownloadedEmbeddingType.Glove),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
            DenseArchitecture(),
            RNNArchitecture(),
        ],
    },
    ExperimentType.NNCNN5SentencesCombinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [1, 2, 3, 7, 10, 15],
            [PreprocessingType.CaseInterpunction],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [60000],
            [LOOKUP_KEY],
            [True],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
            ),
            [
                (300, DownloadedEmbeddingType.Glove),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
        ],
    },
    ExperimentType.NNCNN310SentencesCombinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5, 15, 25],
            [3, 10],
            [PreprocessingType.CaseInterpunction],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [60000],
            [LOOKUP_KEY],
            [True],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
            ),
            [
                (300, DownloadedEmbeddingType.Glove),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
        ],
    },
    ExperimentType.EmbeddingSizeModelingNN: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction, PreprocessingType.Default],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [60000],
            [LOOKUP_KEY],
            [True],
            list(
                settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])
            ),
            [(i, None) for i in range(10, 320, 20)],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
            DenseArchitecture(),
        ],
    },
    ExperimentType.Transformer310Combinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5, 15, 25], [3, 10], [PreprocessingType.CaseInterpunction], [LOOKUP_KEY]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [
                TransformerName.DistilBertBaseUncased,
            ],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [LOOKUP_KEY],
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.Transformer5SentencesCombinations: lambda: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [1, 2, 3, 7, 10, 15],
            [PreprocessingType.CaseInterpunction],
            [LOOKUP_KEY],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [
                TransformerName.DistilBertBaseUncased,
            ],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [LOOKUP_KEY],
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
}
