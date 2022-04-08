import os
import sys

def adding_module_path():
    module_path = os.path.abspath(os.path.sep.join([".."]*2))

    if module_path not in sys.path:
        sys.path.append(module_path)

adding_module_path()

from src.config.run_prep import run_prep
from src.utils.log_juypter import add_experiment_jupyter_logger

run_prep()
add_experiment_jupyter_logger(os.getcwd())



