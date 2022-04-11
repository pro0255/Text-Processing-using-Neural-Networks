import os

from src.utils.count_experiments import count_experiments


def create_experiment_id(name_of_experiment):
    number_of_experiments_in_folder = str(count_experiments(name_of_experiment))
    experiment_id = os.path.sep.join(
        [name_of_experiment, number_of_experiments_in_folder]
    )
    return experiment_id
