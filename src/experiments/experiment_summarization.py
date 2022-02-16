import pandas as pd
from src.config.config import LOG_SEP, EXPERIMENT_RESULTS_DIRECTORY, FILENAME_SUMMARIZATION
import os
from src.types.experiment_summarization_fields import ExperimentSummarizationFields
from src.experiments.experiment_timer import ExperimentTimer
class ExperimentSummarization:
    def __init__(
        self, 
        experiment_id, 
        directory= EXPERIMENT_RESULTS_DIRECTORY,
        experiment_type=None,
    ) -> None:
        self.directory = directory
        self.experiment_id = experiment_id
        self.state = {}

        self.state[ExperimentSummarizationFields.ExperimentType.value] = experiment_id
        self.state[ExperimentSummarizationFields.ExperimentId.value] = experiment_type

        self.state[ExperimentSummarizationFields.VectorizationTime.value] = 0
        self.state[ExperimentSummarizationFields.LearningTime.value] = 0
        self.state[ExperimentSummarizationFields.PredictionTime.value] = 0
        self.state[ExperimentSummarizationFields.EvaluateTime.value] = 0

        self.state[ExperimentSummarizationFields.TrainRecords.value] = 0
        self.state[ExperimentSummarizationFields.TestRecords.value] = 0
        self.state[ExperimentSummarizationFields.ValidRecords.value] = 0

    def map_timer(self, experiment_timer):
        for k in experiment_timer.dic.keys():
            self.state[k] = experiment_timer.get_elapsed(k)

    def inspect_set(self, current_set, records_type):
        counter = 0
        for i in current_set:
            counter += 1
        self.state[records_type] = counter

    def save(self):
        df = pd.DataFrame.from_dict(self.state, orient="index")
        path = os.path.sep.join([self.directory, self.experiment_id, FILENAME_SUMMARIZATION])
        df.to_csv(path, sep=LOG_SEP)

    def __str__(self) -> str:
        s = []
        for k, v in self.state.items():
            s.append(f"{k}={v}")
        return "\n".join(s)
