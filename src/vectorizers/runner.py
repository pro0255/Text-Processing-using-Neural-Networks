import typing

import numpy as np
import tensorflow as tf
from pandas import DataFrame

from src.config.config import LABEL_COLUMN, TEXT_COLUMN
from src.experiments.helpers.experiment_summarization import \
    ExperimentSummarization
from src.types.experiment_summarization_fields import \
    ExperimentSummarizationFields
from src.types.subset_type import SubsetType
from src.utils.from_dataset_arrays import from_dataset_dataframe
from src.vectorizers.instances import CLASSIC, EMBEDDING, TRANSFORMER


class VectorizerRunner:
    def __init__(
        self,
    ) -> None:
        pass

    def fit_classic(
        self,
        vectorizer_instance,
        dataset: typing.Type[DataFrame],
        subset_type: SubsetType,
        experiment_summarization_instance: typing.Type[ExperimentSummarization],
    ):
        """Method which fits classic vectorizer

        Args:
            vectorizer_instance (_type_): instance which will take care of transforming textual data to numeric vectors
            dataset (typing.Type[DataFrame]): dataset object from TensorFlow
            subset_type (SubsetType): description of data which should be transformed (train, test, valid)
            experiment_summarization_instance (typing.Type[ExperimentSummarization]): instance where will be saved specified data

        Returns:
            _type_: returns X and y according to vectorizer instance
        """
        dataframe = from_dataset_dataframe(dataset)

        X = dataframe[TEXT_COLUMN]
        y = dataframe[LABEL_COLUMN]

        if subset_type in [SubsetType.Train]:
            X = vectorizer_instance.fit_transform(X)
            _X = X.toarray()
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.EmbeddingSize.value
            ] = _X.shape[1]
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.TrainRecords.value
            ] = _X.shape[0]

        if subset_type in [SubsetType.Valid, SubsetType.Test]:
            X = vectorizer_instance.transform(X)
            _X = X.toarray()
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.TestRecords.value
            ] = _X.shape[0]

        return X.toarray(), y

    def fit_embedding(
        self,
        vectorizer_instance,
        dataset: typing.Type[DataFrame],
        subset_type: SubsetType,
        experiment_summarization_instance: typing.Type[ExperimentSummarization],
    ):
        """Method which fits embedding vectorizer. In this project was used GloVe and Word2Vec. But can be expanded.

        Args:
            vectorizer_instance (_type_): instance which will take care of transforming textual data to numeric vectors
            dataset (typing.Type[DataFrame]): dataset object from TensorFlow
            subset_type (SubsetType): description of data which should be transformed (train, test, valid)
            experiment_summarization_instance (typing.Type[ExperimentSummarization]): instance where will be saved specified data

        Returns:
            _type_: returns X and y according to vectorizer instance
        """
        dataframe = from_dataset_dataframe(dataset)

        X = dataframe[TEXT_COLUMN]
        y = dataframe[LABEL_COLUMN]

        if subset_type in [SubsetType.Train]:
            X = vectorizer_instance.fit_transform(X)
            _X = np.array(X)
            state = vectorizer_instance.get_state()
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.EmbeddingSize.value
            ] = _X.shape[1]
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.TrainRecords.value
            ] = _X.shape[0]
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.MissingRatioTrain.value
            ] = state

        if subset_type in [SubsetType.Valid, SubsetType.Test]:
            X = vectorizer_instance.fit_transform(X)
            _X = np.array(X)
            state = vectorizer_instance.get_state()
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.TestRecords.value
            ] = _X.shape[0]
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.MissingRatioTest.value
            ] = state

        return X, y

    def fit_transformer(
        self,
        vectorizer_instance,
        dataset: typing.Type[tf.data.Dataset],
        subset_type: SubsetType,
        experiment_summarization_instance: typing.Type[ExperimentSummarization],
    ):
        """Method which fits transformer vectorizer. In this project was used BERT, DistilBERT and ELECTRA. But can be expanded.

        Args:
            vectorizer_instance (_type_): instance which will take care of transforming textual data to numeric vectors
            dataset (typing.Type[DataFrame]): dataset object from TensorFlow
            subset_type (SubsetType): description of data which should be transformed (train, test, valid)
            experiment_summarization_instance (typing.Type[ExperimentSummarization]): instance where will be saved specified data

        Returns:
            _type_: returns X and y according to vectorizer instance
        """
        X, y = None, None

        if subset_type in [SubsetType.Train]:
            X, y = vectorizer_instance.fit_transform(dataset)
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.EmbeddingSize.value
            ] = X.shape[1]
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.TrainRecords.value
            ] = X.shape[0]

        if subset_type in [SubsetType.Valid, SubsetType.Test]:
            X, y = vectorizer_instance.fit_transform(dataset)
            experiment_summarization_instance.state[
                ExperimentSummarizationFields.TestRecords.value
            ] = X.shape[0]

        return X, y

    def fit(
        self,
        dataset: typing.Type[DataFrame],
        vectorizer_instance,
        subset_type: SubsetType,
        experiment_summarization_instance: typing.Type[ExperimentSummarization],
    ):
        """According to vectorizer instance name will be called correct method. Which are described in VectorizerRunner.

        Args:
            dataset (typing.Type[DataFrame]): _description_
            vectorizer_instance (_type_): _description_
            subset_type (SubsetType): _description_
            experiment_summarization_instance (typing.Type[ExperimentSummarization]): _description_

        Returns:
            _type_: _description_
        """
        name_of_instance = type(vectorizer_instance).__name__

        print(f"Fitting vetorizer with name {name_of_instance}")

        if name_of_instance in CLASSIC:
            print(f"Fitting vectorizer in {CLASSIC}")
            return self.fit_classic(
                vectorizer_instance,
                dataset,
                subset_type,
                experiment_summarization_instance,
            )

        if name_of_instance in EMBEDDING:
            print(f"Fitting vectorizer in {EMBEDDING}")
            return self.fit_embedding(
                vectorizer_instance,
                dataset,
                subset_type,
                experiment_summarization_instance,
            )

        if name_of_instance in TRANSFORMER:
            print(f"Fitting vectorizer in {TRANSFORMER}")
            return self.fit_transformer(
                vectorizer_instance,
                dataset,
                subset_type,
                experiment_summarization_instance,
            )
