from src.utils.create_dataset_from_dataframe import create_dataset_from_Xy
from src.utils.create_experiment_id import create_experiment_id
from src.models.transformer.transformer import TransformerArchitecture
from src.models.transformer.pooling_strategy import pooling_strategy_dictionary
from src.tokenizers.transformer_tokenizer import TransformerTokenizer
from src.tokenizers.prepare_dataset_from_tokenizer import prepare_dataset_from_tokenizer
from src.encoder.create_encoder_from_path import create_encoder_from_path
from src.experiments.helpers.experiment_summarization import ExperimentSummarization
from src.experiments.descriptions.create_description import create_description_for_transformer
from src.experiments.experiment_scripts.neural_nets.neural_net_configuration import NNExpConf
from src.experiments.experiment_scripts.neural_nets.neural_net_wrapper import NNExpRunWrapper
from src.experiments.experiment_scripts.experiment_configurations.config import experiment_config, ExperimentGeneratorPart
from src.experiments.experiment_scripts.types.experiment_types import ExperimentType

EXPERIMENT_TYPE = ExperimentType.TrainableTransformer
experiment_configurations = experiment_config[EXPERIMENT_TYPE][ExperimentGeneratorPart.ExperimentConfiguration] 
dataset_generator = experiment_config[EXPERIMENT_TYPE][ExperimentGeneratorPart.DatasetGenerator]
EXPERIMENT_TYPE_STR = EXPERIMENT_TYPE.value 


class TransformerTrainable:
    def __init__(
        self,
        save_model=False,
    ) -> None:
        self.save_model = save_model
        self.transformer_architecture = TransformerArchitecture()


    def run(self):
        for sets, loaded_data, paths, conf in dataset_generator:
            X_train, X_valid, X_test, y_train, y_valid, y_test = sets
            data_path, author_path = paths
            current_authors, current_sentences, current_preprocessing, norm_size = conf

            train_ds = create_dataset_from_Xy(X_train, y_train)
            test_ds = create_dataset_from_Xy(X_test, y_test)
            val_ds = create_dataset_from_Xy(X_valid, y_valid)
            
            train_records = X_train.shape[0]
            test_records = X_test.shape[0]
            valid_records = X_valid.shape[0]


            for conf_parameters in experiment_configurations:
                model_name, pooling_strategy, output_sequence_length, trainable, learning_settings = conf_parameters
    
                tokenizer = TransformerTokenizer(
                    model_name.value, create_encoder_from_path(author_path), max_len=output_sequence_length
                )
                
                current_experiment_id = create_experiment_id(EXPERIMENT_TYPE_STR)

                description = create_description_for_transformer(
                    current_experiment_id,
                    EXPERIMENT_TYPE_STR,
                    current_authors,
                    current_sentences,
                    model_name,
                    pooling_strategy_dictionary[pooling_strategy],
                    output_sequence_length,
                    trainable,
                    norm_size,
                    data_path,
                    learning_settings,
                    current_preprocessing.value
                )
                
                
                train_ds_trans = prepare_dataset_from_tokenizer(train_ds, tokenizer).batch(learning_settings.batch_size)
                valid_ds_trans = prepare_dataset_from_tokenizer(val_ds, tokenizer).batch(1),
                test_ds_trans = prepare_dataset_from_tokenizer(test_ds, tokenizer).batch(1)

                current_model = self.transformer_architecture.create_model(
                    current_authors,
                    model_name.value, 
                    output_sequence_length, 
                    trainable,  
                    *pooling_strategy_dictionary[pooling_strategy]
                )


                current_model.summary()

                summarization = ExperimentSummarization(current_experiment_id)
                summarization.set_records(train_records, test_records, valid_records)


                nn_conf = NNExpConf(
                    nn_model=current_model,
                    train_ds=train_ds_trans,
                    valid_ds=valid_ds_trans,
                    test_ds=test_ds_trans,
                    learning_settings=learning_settings,
                    description=description,
                    save_model=self.save_model
                )
                wrapper = NNExpRunWrapper(
                    current_experiment_id, 
                    summarization
                )
                wrapper.run(nn_conf)
                                
