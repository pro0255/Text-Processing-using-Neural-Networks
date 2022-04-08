from src.experiments.experiment_scripts.types.experiment_types import ExperimentType
from src.experiments.settings.settings import settings_generator
from src.models.transformer.transformer_configuration_generator import transformer_configuration_generator
from src.data_loading.experiment_loader import ExperimentLoader
from enum import Enum
from src.config.learning_config import METRIC, OPTIMIZER, LOSS
from src.models.transformer.pooling_strategy import TransformerPoolingStrategySelection

from src.types.processing_type import PreprocessingType
from src.types.transformer_name import TransformerName

loader = ExperimentLoader()

class ExperimentGeneratorPart(Enum):
    DatasetGenerator = "DatasetGenerator"
    ExperimentConfiguration = "ExperimentConfiguration"
    

experiment_config = {
    ExperimentType.TrainableTransformer: {
        ExperimentGeneratorPart.DatasetGenerator: loader.create_dataset_generator(
            [5],
            [3],
            [PreprocessingType.CaseInterpunction],
            [15000]
        ),
        ExperimentGeneratorPart.ExperimentConfiguration: transformer_configuration_generator(
            [TransformerName.DistilBertBaseUncased],
            [TransformerPoolingStrategySelection.LastLayerCLS],
            [128],
            [True, False],
            list(settings_generator(
                [64],
                [5e-5],
                [METRIC],
                [LOSS],
                [OPTIMIZER],
                [1]
            ))
        )
    },









}
