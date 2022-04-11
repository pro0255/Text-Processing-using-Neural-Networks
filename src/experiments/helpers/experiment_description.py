import os

import pandas as pd

from src.config.config import (BLANK_DESCRIPTION, EXPERIMENT_RESULTS_DIRECTORY,
                               FILENAME_DESCRIPTION, LOG_SEP)
from src.types.experiment_description import ExperimentDescriptionType


class ExperimentDescription:
    def __init__(
        self,
        experiment_id: str,
        experiment_type: str,
        learning_settings,
        transformer_name:str,
        transformer_pooling:str,
        prediction_model_type:str,
        net_type:str,
        embedding_type:str,
        trainable:bool,
        preprocessing_type:str,
        number_of_authors:int,
        number_of_sentences:int,
        load_path:str,
        seq_len:str,
        is_test:bool,
        classic_model_name:str=BLANK_DESCRIPTION,
        extra_field:str=BLANK_DESCRIPTION,
        transformer_start_index:int=BLANK_DESCRIPTION,
        transformer_end_index:int=BLANK_DESCRIPTION,
        transformer_pooling_strategy:str=BLANK_DESCRIPTION,
        normalization_size:int=BLANK_DESCRIPTION,
        directory:str=EXPERIMENT_RESULTS_DIRECTORY,
    ) -> None:
        self.directory = directory
        self.experiment_id = experiment_id

        self.state = {}

        self.state[ExperimentDescriptionType.ExperimentType.value] = experiment_type
        self.state[ExperimentDescriptionType.ExperimentId.value] = experiment_id
        self.state[ExperimentDescriptionType.BatchSize.value] = (
            learning_settings.batch_size if learning_settings is not None else None
        )
        self.state[ExperimentDescriptionType.Epochs.value] = (
            learning_settings.epochs if learning_settings is not None else None
        )
        self.state[ExperimentDescriptionType.LearningRate.value] = (
            learning_settings.learning_rate if learning_settings is not None else None
        )
        self.state[ExperimentDescriptionType.TransformerName.value] = transformer_name
        self.state[
            ExperimentDescriptionType.TransformerPooling.value
        ] = transformer_pooling
        self.state[
            ExperimentDescriptionType.PredictionModelType.value
        ] = prediction_model_type
        self.state[ExperimentDescriptionType.NetType.value] = net_type
        self.state[ExperimentDescriptionType.EmbeddingType.value] = embedding_type
        self.state[ExperimentDescriptionType.IsTrainable.value] = trainable
        self.state[
            ExperimentDescriptionType.PreprocessingType.value
        ] = preprocessing_type
        self.state[ExperimentDescriptionType.NumberOfAuthors.value] = number_of_authors
        self.state[
            ExperimentDescriptionType.NumberOfSentences.value
        ] = number_of_sentences
        self.state[ExperimentDescriptionType.LoadPath.value] = load_path
        self.state[ExperimentDescriptionType.SeqLen.value] = seq_len
        self.state[ExperimentDescriptionType.IsTest.value] = is_test
        self.state[
            ExperimentDescriptionType.ClassicModelName.value
        ] = classic_model_name
        self.state[ExperimentDescriptionType.ExtraField.value] = extra_field
        self.state[
            ExperimentDescriptionType.TransformerStartIndex.value
        ] = transformer_start_index
        self.state[
            ExperimentDescriptionType.TransformerEndIndex.value
        ] = transformer_end_index
        self.state[
            ExperimentDescriptionType.TransformerPoolingStrategy.value
        ] = transformer_pooling_strategy
        self.state[
            ExperimentDescriptionType.NormalizationSize.value
        ] = normalization_size

    def save(self):
        df = pd.DataFrame.from_dict(self.state, orient="index")
        path = os.path.sep.join(
            [self.directory, self.experiment_id, FILENAME_DESCRIPTION]
        )
        df.to_csv(path, sep=LOG_SEP)

    def __str__(self) -> str:
        s = []
        for k, v in self.state.items():
            s.append(f"{k}={v}")
        return "\n".join(s)
