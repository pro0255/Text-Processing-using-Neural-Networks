import pandas as pd
from src.config.config import LOG_SEP, EXPERIMENT_RESULTS_DIRECTORY, FILENAME_SUMMARIZATION
import os
from src.types.experiment_summarization_fields import ExperimentSummarizationFields



class ExperimentSummarization:
    def __init__(
        self, 
        experiment_id, 
        experiment_type,
        directory= EXPERIMENT_RESULTS_DIRECTORY
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
    
    def save(self):
        df = pd.DataFrame.from_dict(self.state, orient="index")
        path = os.path.sep.join([self.directory, self.experiment_id, FILENAME_SUMMARIZATION])
        df.to_csv(path, sep=LOG_SEP)

    def __str__(self) -> str:
        s = []
        for k, v in self.state.items():
            s.append(f"{k}={v}")
        return "\n".join(s)
