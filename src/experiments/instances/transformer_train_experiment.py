from src.experiments.experiment_run_wrapper import ExperimentRunWrapper
from src.experiments.settings import LearningSettings
from src.utils.create_path_to_gutenberg import get_path_to_gutenberg_sets
from src.data_loading.get_dataset_object_from import get_datasets
from src.tokenizers.transformer_tokenizer import TransformerTokenizer
from src.encoder.create_encoder_from_path import create_encoder_from_path
from transformers import TFAutoModel, AutoConfig
import tensorflow as tf
import os
from src.tokenizers.prepare_dataset_from_tokenizer import prepare_dataset_from_tokenizer
from src.config.config import USE_TESTING_DATASET_FOLDER, BLANK_DESCRIPTION
from src.experiments.experiment_description import ExperimentDescription
from src.models.transformer.bert_pooling_layer import BertPoolingLayer
from src.types.transformer_name import TransformerName
from src.types.transformer_pooling import TransformerPooling
from src.types.prediction_model_type import PredictionModelType
from src.types.net_type import NetType
from src.types.embedding_type import EmbeddingType
from src.types.processing_type import PreprocessingType
from src.preprocessing.preprocessing_factory import PreprocessingFactory
from src.config.config import get_current_folder
import time
from src.experiments.experiment_summarization import ExperimentSummarization
from src.types.experiment_summarization_fields import ExperimentSummarizationFields


class TransformerTrainExperiment:
    def __init__(self, number_of_authors, number_of_sentences, model_name=TransformerName.BertBaseUncased.value) -> None:
        self.number_of_authors = number_of_authors
        self.number_of_sentences = number_of_sentences
        self.model_name = model_name


    def get_model(self, trainable):
        config = AutoConfig.from_pretrained(self.model_name, output_hidden_states=True)
        transformer = TFAutoModel.from_config(config)

        input_ids = tf.keras.layers.Input(shape=(512, ), name='input_ids', dtype='int32')
        mask = tf.keras.layers.Input(shape=(512, ), name='attention_mask', dtype='int32')

        embeddings = transformer(input_ids, attention_mask=mask)
        X = BertPoolingLayer()(embeddings, TransformerPooling.Pooler)
        X = tf.keras.layers.Dense(128, activation='relu')(X)
        X = tf.keras.layers.Dropout(0.1)(X)
        y = tf.keras.layers.Dense(self.number_of_authors, activation='softmax', name='outputs')(X)

        model = tf.keras.Model(inputs=[input_ids, mask], outputs=y)

        model.layers[2].trainable = trainable

        return model  


    def run(self):
        settings = LearningSettings()


        current_folder = get_current_folder()
        print(f'Load folder {current_folder}')

        path_data, path_authors = get_path_to_gutenberg_sets(
            self.number_of_authors, 
            self.number_of_sentences,
            current_folder
        )


        preprocessing_factory = PreprocessingFactory()

        train, valid, test = get_datasets(path_data, ';', preprocessing_factory.create(PreprocessingType.Default))

        tokenizer = TransformerTokenizer(
            self.model_name, 
            create_encoder_from_path(
                path_authors
            )
        )

        for trainable in [True, False]:

            current_timestamp = time.time()

            experiment_id = "Trainable" + os.path.sep + f"Train_{trainable}_stamp:{str(current_timestamp)}"
            print(experiment_id)

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
                extra_field=BLANK_DESCRIPTION
            )

            summarization = ExperimentSummarization(experiment_id)

            summarization.inspect_set(train, ExperimentSummarizationFields.TrainRecords.value)
            summarization.inspect_set(valid, ExperimentSummarizationFields.ValidRecords.value)
            summarization.inspect_set(test, ExperimentSummarizationFields.TestRecords.value)
             
            wrapper = ExperimentRunWrapper(experiment_id, summarization)
            current_model = self.get_model(trainable)
            current_model.compile(loss=settings.loss, optimizer=settings.optimizer, metrics=settings.metric)

            wrapper.run(
                current_model, 
                prepare_dataset_from_tokenizer(train, tokenizer)
                    .shuffle(buffer_size=30000)
                    .cache()
                    .batch(settings.batch_size)
                    .prefetch(4),
                prepare_dataset_from_tokenizer(valid, tokenizer)
                    .batch(1),
                prepare_dataset_from_tokenizer(test, tokenizer)
                    .batch(1),
                settings,
                description,
                False
            )
     