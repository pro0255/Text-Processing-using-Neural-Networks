import os
import typing

import tensorflow as tf

from src.config.config import BEST_WEIGHTS_NAME


def create_save_best_weights_callback(filepath: str) -> typing.Type[tf.keras.callbacks.ModelCheckpoint]:
    return tf.keras.callbacks.ModelCheckpoint(
        filepath=filepath,
        save_weights_only=True,
        monitor="val_loss",
        mode="auto",
        save_best_only=True,
        save_format="tf",
    )


def create_save_best_weights_filepath(directory:str, filename:str=BEST_WEIGHTS_NAME) -> str:
    return os.path.sep.join([directory, filename])
