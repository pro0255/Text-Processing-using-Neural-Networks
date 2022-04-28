from src.encoder.create_encoder_from_path import create_encoder_from_path
from src.experiments.descriptions.create_description import \
    create_description_for_transformer
from src.experiments.experiment_scripts.neural_nets.neural_net_configuration import \
    NNExpConf
from src.experiments.experiment_scripts.neural_nets.neural_net_wrapper import \
    NNExpRunWrapper
from src.experiments.experiment_scripts.neural_nets.use_lookup import \
    use_lookup_seq
from src.experiments.experiment_scripts.types.experiment_types import \
    ExperimentType
from src.experiments.helpers.experiment_summarization import \
    ExperimentSummarization
from src.models.transformer.pooling_strategy import pooling_strategy_dictionary
from src.models.transformer.transformer import TransformerArchitecture
from src.tokenizers.prepare_dataset_from_tokenizer import \
    prepare_dataset_from_tokenizer
from src.tokenizers.transformer_tokenizer import TransformerTokenizer
from src.types.experiment_generator_part_type import ExperimentGeneratorPart
from src.utils.create_experiment_id import create_experiment_id
from src.utils.get_train_test_valid_ds import get_train_test_valid_ds


class TransformerRunner:
    """Helper class which starts Transformer experiment.

    Firstly load data from configuration, then loads data, split, and one after one starts experiment with specified configuration.

    Same as NNRunner, ClassicRunner.
    """
    def __init__(
        self,
        experiment_type: ExperimentType,
        save_best: bool = True,
        save_model: bool = False,
        config_dict={},
    ) -> None:
        self.save_model = save_model
        self.save_best = save_best
        self.experiment_type = experiment_type

        self.config_object_getter = config_dict.get(self.experiment_type, None)

        if self.config_object_getter is not None:

            config_dict = self.config_object_getter()

            print(f"Loaded configuration {list(config_dict.keys())}")

            self.experiment_configurations = config_dict[
                ExperimentGeneratorPart.ExperimentConfiguration
            ]
            self.dataset_generator = config_dict[
                ExperimentGeneratorPart.DatasetGenerator
            ]
            self.experiment_type_str = self.experiment_type.value

            self.transformer_architecture = TransformerArchitecture()

        

    def run(self):
        if self.config_object_getter is None:
            print("Experiment was not specified well!")
            return


        for dataset_value in self.dataset_generator:
            print()

            if dataset_value is None:
                print('Dataset value is None')
                continue

            print("Loaded dataset!")
            sets, loaded_data, paths, conf = dataset_value
            X_train, X_valid, X_test, y_train, y_valid, y_test = sets
            data_path, author_path = paths
            current_authors, current_sentences, current_preprocessing, norm_size = conf

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

            print(f'Running experiment pre={current_preprocessing}, norm_size={norm_size}, authors={current_authors}, sentences={current_sentences}')

            for conf_parameters in self.experiment_configurations:
                (
                    model_name,
                    pooling_strategy,
                    output_sequence_length,
                    trainable,
                    learning_settings,
                ) = conf_parameters

                try:
                    output_sequence_length = use_lookup_seq(
                        output_sequence_length,
                        current_authors,
                        current_sentences,
                        current_preprocessing,
                    )
                    if output_sequence_length is None:
                        print("Look up does not exists!")
                        continue


                    print(learning_settings, trainable, pooling_strategy, model_name, output_sequence_length)

                    tokenizer = TransformerTokenizer(
                        model_name.value,
                        create_encoder_from_path(author_path),
                        max_len=output_sequence_length,
                    )

                    current_experiment_id = create_experiment_id(
                        self.experiment_type_str
                    )

                    description = create_description_for_transformer(
                        current_experiment_id,
                        self.experiment_type_str,
                        current_authors,
                        current_sentences,
                        model_name,
                        pooling_strategy_dictionary[pooling_strategy],
                        output_sequence_length,
                        trainable,
                        norm_size,
                        data_path,
                        learning_settings,
                        pooling_strategy,
                        current_preprocessing.value,
                    )

                    train_ds_trans = prepare_dataset_from_tokenizer(
                        train_ds, tokenizer
                    ).batch(learning_settings.batch_size)
                    valid_ds_trans = (
                        prepare_dataset_from_tokenizer(val_ds, tokenizer).batch(1),
                    )
                    test_ds_trans = prepare_dataset_from_tokenizer(
                        test_ds, tokenizer
                    ).batch(1)

                    current_model = self.transformer_architecture.create_model(
                        current_authors,
                        model_name.value,
                        output_sequence_length,
                        trainable,
                        *pooling_strategy_dictionary[pooling_strategy],
                    )

                    current_model.summary()

                    summarization = ExperimentSummarization(
                        experiment_id=current_experiment_id,
                        experiment_type=self.experiment_type_str,
                    )
                    summarization.set_records(
                        train_records, test_records, valid_records
                    )

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

                    print('Ended one experiment \n')

                except Exception as e:
                    print(conf_parameters)
                    print(f"Error occured in {e}")
