from src.types.experiment_summarization_fields import ExperimentSummarizationFields
from enum import Enum
import time


class TimeParts(Enum):
    Start = "start"
    End = "end"


DEFAULT_TIMES = [
    ExperimentSummarizationFields.VectorizationTime.value,
    ExperimentSummarizationFields.LearningTime.value,
    ExperimentSummarizationFields.PredictionTime.value,
    ExperimentSummarizationFields.EvaluateTime.value,
]


class ExperimentTimer:
    def __init__(self, times=DEFAULT_TIMES):
        self.dic = self.create_dic(times)

    def create_time_parts(self):
        return {
            TimeParts.Start.value: 0,
            TimeParts.End.value: 0,
        }

    def create_dic(self, times):
        return {time_key: self.create_time_parts() for time_key in times}

    def update(self, time_type, time_part, value):
        self.dic[time_type][time_part] = value

    def get_elapsed(self, time_type):
        return (
            self.dic[time_type][TimeParts.End.value]
            - self.dic[time_type][TimeParts.Start.value]
        )

    def start(self, time_type):
        current = time.time()
        self.update(time_type, TimeParts.Start.value, current)

    def end(self, time_type):
        current = time.time()
        self.update(time_type, TimeParts.End.value, current)
