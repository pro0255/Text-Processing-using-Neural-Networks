from src.experiments.experiment_description import ExperimentDescription

from src.config.config import BLANK_DESCRIPTION, USE_TESTING_DATASET_FOLDER
from src.types.embedding_type import EmbeddingType
from src.types.net_type import NetType
from src.types.prediction_model_type import PredictionModelType
from src.types.processing_type import PreprocessingType
from src.types.transformer_pooling import TransformerPooling

description = ExperimentDescription(
    experiment_id=experiment_id,
    experiment_type="Trainable",
    learning_settings=settings,
    transformer_name=self.model_name,
    transformer_pooling=TransformerPooling.Pooler.value,
    prediction_model_type=PredictionModelType.NeuralNet.value,
    net_type=NetType.Dense.value,
    embedding_type=EmbeddingType.Transformer.value,
    trainable=trainable,
    preprocessing_type=PreprocessingType.Default.value,
    number_of_authors=10,
    number_of_sentences=3,
    load_path=path_data,
    seq_len=512,
    is_test=USE_TESTING_DATASET_FOLDER,
    classic_model=BLANK_DESCRIPTION,
    extra_field=BLANK_DESCRIPTION,
    transformer_start_index=BLANK_DESCRIPTION,
    transformer_end_index=BLANK_DESCRIPTION,
    transformer_pooling_strategy=BLANK_DESCRIPTION,
    normalization_size=BLANK_DESCRIPTION,
)
