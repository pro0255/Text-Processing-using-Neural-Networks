import logging
import os
import sys

from IPython import get_ipython

from src.config.config import JUPYTER_LOG_NAME


def add_experiment_jupyter_logger(path: str) -> None:
    path_file = os.path.sep.join([path, JUPYTER_LOG_NAME])
    nblog = open(path_file, "a+")
    sys.stdout.echo = nblog
    sys.stderr.echo = nblog

    get_ipython().log.handlers[0].stream = nblog
    get_ipython().log.setLevel(logging.INFO)
    return nblog
