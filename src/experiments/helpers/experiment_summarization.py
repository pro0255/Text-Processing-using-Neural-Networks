import pandas as pd
from src.config.config import (
    LOG_SEP,
    EXPERIMENT_RESULTS_DIRECTORY,
    FILENAME_SUMMARIZATION,
)
import os
from src.types.experiment_summarization_fields import ExperimentSummarizationFields


class ExperimentSummarization:
    def __init__(
        self,
        experiment_id,
        directory=EXPERIMENT_RESULTS_DIRECTORY,
        experiment_type=None,
    ) -> None:
        self.directory = directory
        self.experiment_id = experiment_id
        self.state = {}

        print(f"Creating new experiment summarization for {experiment_id}!")
        self.state[ExperimentSummarizationFields.ExperimentType.value] = experiment_id
        self.state[ExperimentSummarizationFields.ExperimentId.value] = experiment_type

        self.state[ExperimentSummarizationFields.VectorizationTime.value] = 0
        self.state[ExperimentSummarizationFields.LearningTime.value] = 0
        self.state[ExperimentSummarizationFields.PredictionTime.value] = 0
        self.state[ExperimentSummarizationFields.EvaluateTime.value] = 0

        self.state[ExperimentSummarizationFields.TrainRecords.value] = 0
        self.state[ExperimentSummarizationFields.TestRecords.value] = 0
        self.state[ExperimentSummarizationFields.ValidRecords.value] = 0

        self.state[ExperimentSummarizationFields.MissingRatioTrain.value] = 0
        self.state[ExperimentSummarizationFields.MissingRatioTest.value] = 0
        self.state[ExperimentSummarizationFields.EmbeddingSize.value] = 0

    def map_timer(self, experiment_timer):
        print("Mapping timer")
        for k in experiment_timer.dic.keys():
            self.state[k] = experiment_timer.get_elapsed(k)
        print("End of maping timer")

    def set_records(self, train_records, test_records, valid_records):
        self.state[ExperimentSummarizationFields.TrainRecords.value] = train_records
        self.state[ExperimentSummarizationFields.TestRecords.value] = test_records
        self.state[ExperimentSummarizationFields.ValidRecords.value] = valid_records

    def inspect_set(self, current_set, records_type):
        print(f"Running inspection of input set for {records_type}")
        counter = 0
        for i in current_set:
            counter += 1
        print(f"End of inspection of input set for {records_type} = {counter}")
        self.state[records_type] = counter

    def save(self):
        df = pd.DataFrame.from_dict(self.state, orient="index")
        path = os.path.sep.join(
            [self.directory, self.experiment_id, FILENAME_SUMMARIZATION]
        )
        df.to_csv(path, sep=LOG_SEP)

    def __str__(self) -> str:
        s = []
        for k, v in self.state.items():
            s.append(f"{k}={v}")
        return "\n".join(s)
