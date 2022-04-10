from src.experiments.experiment_scripts.types.experiment_types import ExperimentType
from src.experiments.settings.settings import settings_generator
from src.models.transformer.transformer_configuration_generator import (
    transformer_configuration_generator,
)
from src.models.nets.nets_configuration_generator import nets_configuration_generator
from src.data_loading.experiment_loader import ExperimentLoader
from enum import Enum
from src.config.learning_config import METRIC, OPTIMIZER, LOSS
from src.models.transformer.pooling_strategy import TransformerPoolingStrategySelection

from src.types.processing_type import PreprocessingType
from src.types.transformer_name import TransformerName
from src.models.nets.cnn import CNNArchitecture
from src.models.nets.rnn import RNNArchitecture
from src.models.nets.dense import DenseArchitecture
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType

loader = ExperimentLoader()





class ExperimentGeneratorPart(Enum):
    DatasetGenerator = "DatasetGenerator"
    ExperimentConfiguration = "ExperimentConfiguration"
    ExperimentArchitecture = "ExperimentArchitecture"


experiment_config = {
    ExperimentType.TrainableTransformer: {
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
    ExperimentType.PoolingStrategyTransformer: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            list(TransformerPoolingStrategySelection),
            [130],
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.OutputSequenceLengthTransformer: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            list(range(50, 220, 20)),
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.LearningRateTransformer: {
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
                    [5],
                )
            ),
        ),
    },
    ExperimentType.TransformerType: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5], [3], [PreprocessingType.CaseInterpunction], [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [
                TransformerName.DistilBertBaseUncased,
                TransformerName.ElectraBase,
                TransformerName.BertBaseUncased,
            ],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [10])),
        ),
    },
    ExperimentType.LabelSize: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            list(range(5000, 22000, 2000)),
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [130],
            [True],
            list(settings_generator([64], [5e-5], [METRIC], [LOSS], [OPTIMIZER], [5])),
        ),
    },
    ExperimentType.NumberOfAuthorsNN: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            [100],
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: nets_configuration_generator(
            [10000],
            [130],
            [True, False],
            list(settings_generator([64], [0.001], [METRIC], [LOSS], [OPTIMIZER], [10])),
            [
                (50, None),
                (150, None),
                (300, DownloadedEmbeddingType.Word2Vec),
                (300, DownloadedEmbeddingType.Glove),
            ],
        ),
        ExperimentGeneratorPart.ExperimentArchitecture: [
            CNNArchitecture(),
            RNNArchitecture(),
            DenseArchitecture()
        ]
    }
}


