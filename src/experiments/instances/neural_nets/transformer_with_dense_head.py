from src.experiments.experiment_run_wrapper import ExperimentRunWrapper
from src.experiments.settings import LearningSettings
from src.tokenizers.transformer_tokenizer import TransformerTokenizer
from src.encoder.create_encoder_from_path import create_encoder_from_path
from transformers import TFAutoModel, AutoConfig
import tensorflow as tf
import os
from src.tokenizers.prepare_dataset_from_tokenizer import prepare_dataset_from_tokenizer
from src.models.transformer.bert_pooling_layer import BertPoolingLayer
import time
from src.experiments.experiment_summarization import ExperimentSummarization
from src.types.experiment_summarization_fields import ExperimentSummarizationFields
from src.config.learning_config import TRANSFORMER_EPOCHS
from src.experiments.descriptions.create_description import (
    create_description_for_transformer_with_dense_head
)
import os
from src.config.config import TEXT_COLUMN, LABEL_COLUMN, VALIDATION_SIZE
from src.experiments.experiment_description import ExperimentDescription
from src.types.transformer_pooling import TransformerPooling
from src.types.prediction_model_type import PredictionModelType
from src.types.net_type import NetType
from src.types.embedding_type import EmbeddingType
from src.types.processing_type import PreprocessingType
import time
from src.data_loading.get_dataset_object_from import get_dataset_all
from src.utils.from_dataset_arrays import from_dataset_dataframe
from src.utils.split_dataframe import split_dataframe
from src.utils.normalize_dataframe_to_size import normalize_dataframe_to_size
from src.utils.create_dataset_from_dataframe import create_dataset_from_Xy
import pandas as pd
from src.utils.generate_random_stamp import generator_random_stamp
from src.types.transformer_pooling import TransformerPooling

NAME_OF_EXPERIMENT = "TransformerWithDenseHeadExperiment"
class TransformerWithDenseHeadExperiment:
    def __init__(
        self,
        save_model=False
    ) -> None:
        self.save_model = save_model


    def get_generator(self, seq_lenghts, trainable, model_name_with_pooling_strategy):
        for max_len in seq_lenghts:
            for model_name_with_p_s in model_name_with_pooling_strategy:
                for train in trainable:
                    yield (max_len, model_name_with_p_s, train)

    def create_experiment_id(self):
        current_experiment_id = (
            NAME_OF_EXPERIMENT + os.path.sep + f"stamp_{generator_random_stamp()}"
        )
        return current_experiment_id


    def get_model(self, trainable, model_name, number_of_authors, seq_len, pooling_strategy):
        config = AutoConfig.from_pretrained(model_name, output_hidden_states=True)
        transformer = TFAutoModel.from_config(config)

        input_ids = tf.keras.layers.Input(shape=(seq_len,), name="input_ids", dtype="int32")
        mask = tf.keras.layers.Input(shape=(seq_len,), name="attention_mask", dtype="int32")


        embeddings = transformer(input_ids, attention_mask=mask)['last_hidden_state'][:, 0, :]  # we only keep tensor 0 (last_hidden_state)

        X = tf.keras.layers.Dropout(0.3)(embeddings)
        X = tf.keras.layers.Dense(128, activation='relu')(X)
        X = tf.keras.layers.BatchNormalization()(X)
        X = tf.keras.layers.Dense(128, activation='relu')(X)
        X = tf.keras.layers.Dropout(0.2)(X)
        y = tf.keras.layers.Dense(number_of_authors, activation='softmax', name='outputs')(X)  # adjust based on number of sentiment classes

        model = tf.keras.Model(inputs=[input_ids, mask], outputs=y)

        model.layers[2].trainable = trainable

        return model

    def run(
        self,
        number_of_authors,
        number_of_sentences,
        seq_lengths=[],
        trainable=[],
        model_name_with_pooling_strategy=[],        
        normalize_value=None,
        all_data=None,
        data=None,
        paths=None,
    ):

        settings = LearningSettings()
        settings.epochs = TRANSFORMER_EPOCHS
        data_path, authors_path = paths

        data_normalized = normalize_dataframe_to_size(all_data, normalize_value)
        X_train, X_test, y_train, y_test = split_dataframe(data_normalized)
        df = pd.DataFrame()
        df[TEXT_COLUMN] = X_train
        df[LABEL_COLUMN] = y_train
        X_train, X_val, y_train, y_val = split_dataframe(df, VALIDATION_SIZE)

        train_ds = create_dataset_from_Xy(X_train, y_train)
        test_ds = create_dataset_from_Xy(X_test, y_test)
        val_ds = create_dataset_from_Xy(X_val, y_val)

        for value in self.get_generator(seq_lengths, trainable, model_name_with_pooling_strategy):
            seq_length, model_name_with_pooling_strategy, trainable = value
            model_name, pooling_strategy = model_name_with_pooling_strategy

            tokenizer = TransformerTokenizer(
                model_name.value, create_encoder_from_path(authors_path), max_len=seq_length
            )

            current_experiment_id = self.create_experiment_id()

            description = create_description_for_transformer_with_dense_head(
                current_experiment_id,
                NAME_OF_EXPERIMENT,
                number_of_authors,
                number_of_sentences,
                model_name,
                pooling_strategy,
                seq_length,
                trainable,
                normalize_value,
                data_path,
                settings
            )

            summarization = ExperimentSummarization(current_experiment_id)

            summarization.inspect_set(
                train_ds, ExperimentSummarizationFields.TrainRecords.value
            )
            summarization.inspect_set(
                val_ds, ExperimentSummarizationFields.ValidRecords.value
            )
            summarization.inspect_set(
                test_ds, ExperimentSummarizationFields.TestRecords.value
            )

            wrapper = ExperimentRunWrapper(current_experiment_id, summarization)

            current_model = self.get_model(trainable, model_name.value, number_of_authors, seq_length, pooling_strategy)


            current_model.compile(
                loss=settings.loss,
                optimizer=settings.optimizer,
                metrics=settings.metric,
            )
            
            current_model.summary()

            wrapper.run(
                current_model,
                prepare_dataset_from_tokenizer(train_ds, tokenizer)
                .shuffle(buffer_size=30000)
                .cache()
                .batch(settings.batch_size)
                .prefetch(4),
                prepare_dataset_from_tokenizer(val_ds, tokenizer).batch(1),
                prepare_dataset_from_tokenizer(test_ds, tokenizer).batch(1),
                settings,
                description,
                self.save_model,
            )
