from src.experiments.experiment_scripts.types.experiment_types import ExperimentType
from src.config.config import BLANK_DESCRIPTION
from src.encoder.create_encoder_from_path import create_encoder_from_path
from src.experiments.experiment_scripts.experiment_configurations.config import (
    ExperimentGeneratorPart, experiment_config)
from src.experiments.experiment_scripts.neural_nets.neural_net_configuration import \
    NNExpConf
from src.experiments.experiment_scripts.neural_nets.neural_net_wrapper import \
    NNExpRunWrapper
from src.experiments.experiment_scripts.neural_nets.use_lookup import \
    use_lookup_seq
from src.experiments.helpers.experiment_summarization import \
    ExperimentSummarization
from src.types.embedding_type import translate_from_embedding
from src.types.experiment_summarization_fields import \
    ExperimentSummarizationFields
from src.utils.create_experiment_id import create_experiment_id
from src.utils.get_train_test_valid_ds import get_train_test_valid_ds


class NNRunner:
    def __init__(
        self,
        experiment_type: ExperimentType,
        save_best: bool=False,
        save_model: bool=False,
    ) -> None:
        self.save_best = save_best
        self.save_model = save_model

        self.experiment_type = experiment_type

        print(self.experiment_type)

        self.experiment_configurations, self.embeddding_index_dict = experiment_config[
            self.experiment_type
        ][ExperimentGeneratorPart.ExperimentConfiguration]

        self.dataset_generator = experiment_config[self.experiment_type][
            ExperimentGeneratorPart.DatasetGenerator
        ]

        self.experiment_type_str = self.experiment_type.value

        self.experiment_architectures = experiment_config[self.experiment_type][
            ExperimentGeneratorPart.ExperimentArchitecture
        ]

    def run(self):
        for dataset_value in self.dataset_generator:
            if dataset_value is None:
                continue
            sets, loaded_data, paths, conf = dataset_value
            X_train, X_valid, X_test, y_train, y_valid, y_test = sets
            data_path, author_path = paths
            current_authors, current_sentences, current_preprocessing, norm_size = conf
            encoder = create_encoder_from_path(author_path)
            y_test = encoder.transform(y_test)
            y_train = encoder.transform(y_train)
            y_valid = encoder.transform(y_valid)

            (
                train_ds,
                val_ds,
                test_ds,
                train_records,
                valid_records,
                test_records,
            ) = get_train_test_valid_ds(
                X_train, X_valid, X_test, y_train, y_valid, y_test
            )

            for current_architecture in self.experiment_architectures:

                for conf_parameters in self.experiment_configurations:
                    (
                        vocab_size,
                        output_sequence_length,
                        trainable,
                        learning_settings,
                        embedding,
                    ) = conf_parameters
                    embedding_size, embedding_dictionary_name = embedding

                    try:

                        print("Settings = \n", learning_settings)
                        output_sequence_length = use_lookup_seq(
                            output_sequence_length,
                            current_authors,
                            current_sentences,
                            current_preprocessing,
                        )
                        if output_sequence_length is None:
                            print("Look up does not exists!")
                            continue

                        current_experiment_id = create_experiment_id(
                            self.experiment_type_str
                        )

                        embedding_type = translate_from_embedding(
                            embedding_dictionary_name
                        )

                        description = current_architecture.get_description(
                            current_experiment_id,
                            self.experiment_type_str,
                            current_authors,
                            current_sentences,
                            norm_size,
                            output_sequence_length,
                            trainable,
                            data_path,
                            learning_settings,
                            embedding_type,
                            vocab_size=vocab_size,
                            embedding_size=embedding_size,
                            embedding_name=embedding_dictionary_name,
                            preprocessing_type=current_preprocessing.value,
                        )

                        train_ds_trans = train_ds.batch(learning_settings.batch_size)
                        valid_ds_trans = val_ds.batch(1)
                        test_ds_trans = test_ds.batch(1)

                        current_model, stats = current_architecture.create_model(
                            current_authors,
                            train_ds,
                            val_ds,
                            vocab_size,
                            embedding_size,
                            output_sequence_length,
                            trainable,
                            self.embeddding_index_dict.get(
                                embedding_dictionary_name, None
                            ),
                        )

                        current_model.summary()

                        summarization = ExperimentSummarization(
                            experiment_id=current_experiment_id,
                            experiment_type=self.experiment_type_str
                        )
                        
                        summarization.set_records(
                            train_records, test_records, valid_records
                        )

                        if stats != BLANK_DESCRIPTION:
                            hits, misses = stats
                            summarization.state[
                                ExperimentSummarizationFields.MissingRatioTrain.value
                            ] = str((misses, hits, 100 * (misses / (hits + misses))))

                        summarization.state[
                            ExperimentSummarizationFields.EmbeddingSize.value
                        ] = embedding_size

                        nn_conf = NNExpConf(
                            nn_model=current_model,
                            train_ds=train_ds_trans,
                            valid_ds=valid_ds_trans,
                            test_ds=test_ds_trans,
                            learning_settings=learning_settings,
                            description=description,
                            save_model=self.save_model,
                            save_best=self.save_best,
                        )

                        wrapper = NNExpRunWrapper(current_experiment_id, summarization)

                        wrapper.run(nn_conf)

                    except Exception as e:
                        print(conf_parameters)
                        print(f"Error occured in {e}")
