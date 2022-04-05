import sys
import logging
from IPython import get_ipython


def add_experiment_jupyter_logger(path):
    nblog = open(path, "a+")
    sys.stdout.echo = nblog
    sys.stderr.echo = nblog

    get_ipython().log.handlers[0].stream = nblog
    get_ipython().log.setLevel(logging.INFO)



