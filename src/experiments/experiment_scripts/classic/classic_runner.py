import typing

from src.encoder.create_encoder_from_path import create_encoder_from_path
from src.experiments.descriptions.create_description import (
    create_description_for_classic,
    create_description_for_transformer_with_classic,
    from_pred_instance_get_type)
from src.experiments.experiment_scripts.classic.classic_configuration import \
    ClassicExpConf
from src.experiments.experiment_scripts.classic.classic_wrapper import \
    ClassicExpRunWrapper
from src.experiments.experiment_scripts.types.experiment_types import \
    ExperimentType
from src.experiments.helpers.experiment_description import \
    ExperimentDescription
from src.experiments.helpers.experiment_summarization import \
    ExperimentSummarization
from src.models.transformer.pooling_strategy import \
    TransformerPoolingStrategySelection
from src.types.experiment_description import ExperimentDescriptionType
from src.types.experiment_generator_part_type import ExperimentGeneratorPart
from src.utils.create_experiment_id import create_experiment_id
from src.utils.get_train_test_valid_ds import get_train_test_valid_ds
from src.vectorizers.instances import TRANSFORMER

DEFAULT_POOLING_STRATEGY = [TransformerPoolingStrategySelection.LastLayerCLS]


class ClassicRunner:
    """Helper class which starts Transformer experiment.

    Firstly load data from configuration, then loads data, split, and one after one starts experiment with specified configuration.

    Same as NNRunner, TransformerRunner.
    """
    def __init__(
        self, experiment_type: ExperimentType, config_dict={}
    ) -> None:

        self.experiment_type = experiment_type
        self.config_object_getter = config_dict.get(self.experiment_type, None)

        if self.config_object_getter is not None:

            config_dict = self.config_object_getter()

            print(f"Loaded configuration {list(config_dict.keys())}")

            self.dataset_generator = config_dict[
                ExperimentGeneratorPart.DatasetGenerator
            ]

            self.feature_extractors = config_dict[
                ExperimentGeneratorPart.FeatureExtractors
            ]

            self.predictors = config_dict[
                ExperimentGeneratorPart.Predictor
            ]

            self.transformer_pooling_strategy = config_dict[
                ExperimentGeneratorPart.TransformerPoolingStrategy
            ]

            self.experiment_type_str = self.experiment_type.value

    def is_transformer(self, feature_extractor):
        if type(feature_extractor).__name__ in TRANSFORMER:
            return True
        return False

    def get_pooling_strategy(self):
        if self.transformer_pooling_strategy is None:
            return DEFAULT_POOLING_STRATEGY

        return self.transformer_pooling_strategy

    def run_prediction(
        self,
        X_train,
        y_train,
        X_test,
        y_test,
        description: typing.Type[ExperimentDescription],
        feature_extractor,
        wrapper: typing.Type[ClassicExpRunWrapper],
    ):

        for predict_instance in self.predictors:

            try:
                current_experiment_id = create_experiment_id(self.experiment_type_str)

                description = description
                description.experiment_id = current_experiment_id
                description.state[
                    ExperimentDescriptionType.ExperimentId.value
                ] = current_experiment_id

                current_predict_instance_name = from_pred_instance_get_type(
                    predict_instance
                )
                print(f"Current predict instance {current_predict_instance_name}")
                description.state[
                    ExperimentDescriptionType.ClassicModelName.value
                ] = current_predict_instance_name

                classic_conf = ClassicExpConf(
                    train=(X_train, y_train),
                    test=(X_test, y_test),
                    experiment_id=current_experiment_id,
                    description=description,
                    predict_instance=predict_instance,
                    vectorization_instance=feature_extractor,
                )

                wrapper.experiment_summarization.set_id(current_experiment_id)
                wrapper.set_id(current_experiment_id)

                wrapper.run_prediction(classic_conf)

            except Exception as e:
                print(f"Error occured in {e}")

    def run(self):
        if self.config_object_getter is None:
            print("Experiment was not specified well!")
            return

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

            # Loaded records

            # Go over vectorizer
            for feature_extractor in self.feature_extractors:

                is_feature_extractor_transformer = self.is_transformer(
                    feature_extractor
                )

                if is_feature_extractor_transformer:

                    for pooling_strategy in self.get_pooling_strategy():

                        print("\n")
                        summarization = ExperimentSummarization(
                            experiment_id="", experiment_type=self.experiment_type_str
                        )
                        wrapper = ClassicExpRunWrapper("", summarization)

                        feature_extractor.set_pooling_strategy(pooling_strategy)

                        # Get vectors
                        (
                            X_train_trans,
                            X_test_trans,
                            y_train_trans,
                            y_test_trans,
                        ) = wrapper.run_vectorization(
                            feature_extractor, train_ds, test_ds
                        )

                        description = create_description_for_transformer_with_classic(
                            "",
                            self.experiment_type_str,
                            current_authors,
                            current_sentences,
                            "",
                            feature_extractor,
                            norm_size,
                            data_path,
                            current_preprocessing.value,
                        )

                        # Predict
                        self.run_prediction(
                            X_train_trans,
                            y_train_trans,
                            X_test_trans,
                            y_test_trans,
                            description,
                            feature_extractor,
                            wrapper,
                        )

                else:
                    print("\n")

                    summarization = ExperimentSummarization(
                        experiment_id="", experiment_type=self.experiment_type_str
                    )
                    wrapper = ClassicExpRunWrapper("", summarization)

                    # Get vectors
                    (
                        X_train_trans,
                        X_test_trans,
                        y_train_trans,
                        y_test_trans,
                    ) = wrapper.run_vectorization(feature_extractor, train_ds, test_ds)

                    description = create_description_for_classic(
                        "",
                        self.experiment_type_str,
                        current_authors,
                        current_sentences,
                        "",
                        feature_extractor,
                        norm_size,
                        data_path,
                        current_preprocessing.value,
                    )

                    # Predict
                    self.run_prediction(
                        X_train_trans,
                        y_train_trans,
                        X_test_trans,
                        y_test_trans,
                        description,
                        feature_extractor,
                        wrapper,
                    )
