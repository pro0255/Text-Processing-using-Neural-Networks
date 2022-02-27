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
from src.experiments.sandbox.classic_experiment_runner import ClassicExperimentWrapper 


class ExperimentConfiguration:
    def __init__(
        self, 
        train, 
        test, 
        experiment_id, 
        description, 
        predict_instance, 
        vectorization_instance
    ) -> None:
        self.train = train
        self.test = test
        self.experiment_id = experiment_id
        self.description = description
        self.predict_instance = predict_instance
        self.vectorization_instance = vectorization_instance

    def get_train(self):
        return self.train
    
    def get_test(self):
        return self.test

    def get_experiment_id(self):
        return self.experiment_id

    def get_description(self):
        return self.description

    def get_predict_instance(self):
        return self.predict_instance

    def get_vectorization_instance(self):
        return self.vectorization_instance
