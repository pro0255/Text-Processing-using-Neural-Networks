from src.config.config import EXPERIMENT_RESULTS_DIRECTORY
import os

def count_experiments(experiment_name):
    path = os.path.sep.join([EXPERIMENT_RESULTS_DIRECTORY, experiment_name])
    try:
        current_number_of_experiments = len(os.listdir(path))
        next_experiment_id = current_number_of_experiments
        return next_experiment_id
    except:
        return 0