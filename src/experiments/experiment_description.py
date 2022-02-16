

import pandas as pd
from src.config.config import LOG_SEP, EXPERIMENT_RESULTS_DIRECTORY, FILENAME_DESCRIPTION, BLANK_DESCRIPTION
import os
from src.types.experiment_description import ExperimentDescriptionType

class ExperimentDescription:
    def __init__(
        self, 
        experiment_id, 
        experiment_type,
        learning_settings,
        transformer_name,
        transformer_pooling,
        prediction_model_type,
        net_type,
        embedding_type,
        trainable,
        preprocessing_type,
        number_of_authors,
        number_of_sentences,
        load_path,
        seq_len,
        is_test,
        classic_model_name = BLANK_DESCRIPTION,
        extra_field = BLANK_DESCRIPTION,
        transformer_start_index = BLANK_DESCRIPTION,
        transformer_end_index = BLANK_DESCRIPTION,
        transformer_pooling_strategy = BLANK_DESCRIPTION,
        directory = EXPERIMENT_RESULTS_DIRECTORY

    ) -> None:
        self.directory = directory
        self.experiment_id = experiment_id

        self.state = {}

        self.state[ExperimentDescriptionType.ExperimentType.value] = experiment_id
        self.state[ExperimentDescriptionType.ExperimentId.value] = experiment_type
        self.state[ExperimentDescriptionType.BatchSize.value] = learning_settings.batch_size
        self.state[ExperimentDescriptionType.Epochs.value] = learning_settings.epochs
        self.state[ExperimentDescriptionType.LearningRate.value] = learning_settings.learning_rate
        self.state[ExperimentDescriptionType.TransformerName.value] = transformer_name
        self.state[ExperimentDescriptionType.TransformerPooling.value] = transformer_pooling
        self.state[ExperimentDescriptionType.PredictionModelType.value] = prediction_model_type
        self.state[ExperimentDescriptionType.NetType.value] = net_type
        self.state[ExperimentDescriptionType.EmbeddingType.value] = embedding_type
        self.state[ExperimentDescriptionType.IsTrainable.value] = trainable
        self.state[ExperimentDescriptionType.PreprocessingType.value] = preprocessing_type
        self.state[ExperimentDescriptionType.NumberOfAuthors.value] = number_of_authors
        self.state[ExperimentDescriptionType.NumberOfSentences.value] = number_of_sentences
        self.state[ExperimentDescriptionType.LoadPath.value] = load_path
        self.state[ExperimentDescriptionType.SeqLen.value] = seq_len
        self.state[ExperimentDescriptionType.IsTest.value] = is_test
        self.state[ExperimentDescriptionType.ClassicModelName.value] = classic_model_name
        self.state[ExperimentDescriptionType.ExtraField.value] = extra_field
        self.state[ExperimentDescriptionType.TransformerStartIndex.value] = transformer_start_index
        self.state[ExperimentDescriptionType.TransformerEndIndex.value] = transformer_end_index
        self.state[ExperimentDescriptionType.TransformerPoolingStrategy.value] = transformer_pooling_strategy

    def save(self):
        df = pd.DataFrame.from_dict(self.state, orient="index")
        path = os.path.sep.join([self.directory, self.experiment_id, FILENAME_DESCRIPTION])
        df.to_csv(path, sep=LOG_SEP)

    def __str__(self) -> str:
        s = []
        for k, v in self.state.items():
            s.append(f"{k}={v}")
        return "\n".join(s)
