from src.vectorizers.instances import CLASSIC, EMBEDDING, TRANSFORMER
from src.config.config import LABEL_COLUMN, TEXT_COLUMN
from src.utils.from_dataset_arrays import from_dataset_dataframe
from src.types.subset_type import SubsetType
from src.types.experiment_summarization_fields import ExperimentSummarizationFields
import numpy as np

class VectorizerRunner:
    def __init__(self, ) -> None:
        pass

    def fit_classic(self, vectorizer_instance, dataset, subset_type, experiment_summarization_instance):
        dataframe = from_dataset_dataframe(dataset)

        X = dataframe[TEXT_COLUMN]
        y = dataframe[LABEL_COLUMN]

        if subset_type in [SubsetType.Train]:
            X = vectorizer_instance.fit_transform(X)
            _X = X.toarray()
            experiment_summarization_instance.state[ExperimentSummarizationFields.EmbeddingSize.value] = _X.shape[1]
            experiment_summarization_instance.state[ExperimentSummarizationFields.TrainRecords.value] = _X.shape[0]

        if subset_type in [SubsetType.Valid, SubsetType.Test]:
            X = vectorizer_instance.transform(X)
            _X = X.toarray()
            experiment_summarization_instance.state[ExperimentSummarizationFields.TestRecords.value] = _X.shape[0]

        return X, y

    def fit_embedding(self, vectorizer_instance, dataset, subset_type, experiment_summarization_instance):
            dataframe = from_dataset_dataframe(dataset)

            X = dataframe[TEXT_COLUMN]
            y = dataframe[LABEL_COLUMN]

            if subset_type in [SubsetType.Train]:
                X = vectorizer_instance.fit_transform(X)
                _X = np.array(X)
                state = vectorizer_instance.get_state()
                experiment_summarization_instance.state[ExperimentSummarizationFields.EmbeddingSize.value] = _X.shape[1]
                experiment_summarization_instance.state[ExperimentSummarizationFields.TrainRecords.value] = _X.shape[0]
                experiment_summarization_instance.state[ExperimentSummarizationFields.MissingRatioTrain.value] = state

            if subset_type in [SubsetType.Valid, SubsetType.Test]:
                X = vectorizer_instance.fit_transform(X)
                _X = np.array(X)
                state = vectorizer_instance.get_state()
                experiment_summarization_instance.state[ExperimentSummarizationFields.TestRecords.value] = _X.shape[0]
                experiment_summarization_instance.state[ExperimentSummarizationFields.MissingRatioTest.value] = state

            return X, y

    def fit_transformer(self, vectorizer_instance, dataset, subset_type, experiment_summarization_instance):
            X, y = None, None

            if subset_type in [SubsetType.Train]:
                X, y = vectorizer_instance.fit_transform(dataset)
                experiment_summarization_instance.state[ExperimentSummarizationFields.EmbeddingSize.value] = X.shape[1]
                experiment_summarization_instance.state[ExperimentSummarizationFields.TrainRecords.value] = X.shape[0]

            if subset_type in [SubsetType.Valid, SubsetType.Test]:
                X, y = vectorizer_instance.fit_transform(dataset)
                experiment_summarization_instance.state[ExperimentSummarizationFields.TestRecords.value] = X.shape[0]

            return X, y

    def fit(self, dataset, vectorizer_instance, subset_type, experiment_summarization_instance):
        name_of_instance = type(vectorizer_instance).__name__
        
        print(f"Fitting transformer with name {name_of_instance}")

        if name_of_instance in CLASSIC:
            return self.fit_classic(vectorizer_instance, dataset, subset_type, experiment_summarization_instance)

        if name_of_instance in EMBEDDING:
            return self.fit_embedding(vectorizer_instance, dataset, subset_type, experiment_summarization_instance)

        if name_of_instance in TRANSFORMER:
            return self.fit_transformer(vectorizer_instance, dataset, subset_type, experiment_summarization_instance)


        










