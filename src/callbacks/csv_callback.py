import time

import pandas as pd
import tensorflow as tf

from src.config.config import LOG_SEP


class CSVLogger(tf.keras.callbacks.Callback):
    def __init__(self, path):
        self.path = path
        self.timetaken = time.time()
        self.state = {}

    def on_epoch_end(self, epoch, logs={}):
        logs["time"] = time.time() - self.timetaken
        self.state[epoch] = logs

    def on_train_end(self, logs={}):
        headers = []
        for k, v in self.state.items():
            headers = self.state[k].keys()
            break

        data = {k: self.state[k].values() for k, v in self.state.items()}
        df = pd.DataFrame.from_dict(data, orient="index")
        df.columns = headers
        df.to_csv(self.path, sep=LOG_SEP)
