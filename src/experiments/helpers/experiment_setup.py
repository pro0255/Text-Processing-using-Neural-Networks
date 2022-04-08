import os
from src.config.config import MODEL_SAVE_DIRECTORY, EXPERIMENT_RESULTS_DIRECTORY


class ExperimentSetup:
    def __init__(self, experiment_id, directory=EXPERIMENT_RESULTS_DIRECTORY) -> None:
        self.directory = directory
        self.experiment_id = experiment_id

    def create_parent_directory(self):
        path = os.path.sep.join([self.directory, self.experiment_id])
        self.parent_path = path
        if not os.path.exists(path):
            os.makedirs(path)

    def create_model_directory(self):
        path = os.path.sep.join(
            [self.directory, self.experiment_id, MODEL_SAVE_DIRECTORY]
        )

        if not os.path.exists(path):
            os.makedirs(path)

    def run(self):
        print(f"Running setup of directory for experiment {self.experiment_id}")
        self.create_parent_directory()
        self.create_model_directory()