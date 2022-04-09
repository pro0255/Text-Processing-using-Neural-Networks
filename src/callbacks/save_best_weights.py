import tensorflow as tf
from src.config.config import BEST_WEIGHTS_NAME
import os


def create_save_best_weights_callback(filepath):
    return tf.keras.callbacks.ModelCheckpoint(
        filepath=filepath,
        save_weights_only=True,
        monitor="val_loss",
        mode="auto",
        save_best_only=True,
    )


def create_save_best_weights_filepath(directory, filename=BEST_WEIGHTS_NAME):
    return os.path.sep.join([directory, filename])
