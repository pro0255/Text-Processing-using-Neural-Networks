import tensorflow as tf
from src.callbacks.csv_callback import CSVLogger
import os
from src.config.config import (
    NAME_OF_LEARNING_LOGS,
    EXPERIMENT_RESULTS_DIRECTORY,
    MODEL_SAVE_DIRECTORY,
)
from src.callbacks.save_best_weights import (
    create_save_best_weights_filepath,
    create_save_best_weights_callback,
)


class CallbacksFactory:
    def __init__(self, save_model, save_best):
        self.save_model = save_model
        self.save_best = save_best

    def create(
        self,
        experiment_id: str,
        directory: str = EXPERIMENT_RESULTS_DIRECTORY,
        filename: str = NAME_OF_LEARNING_LOGS,
    ) -> list:

        experiment_directory = os.path.sep.join([directory, experiment_id])

        best_weights_cb_path = create_save_best_weights_filepath(experiment_directory)
        best_weights_cb = create_save_best_weights_callback(best_weights_cb_path)

        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=3, restore_best_weights=True
        )

        model_path = os.sep.join([experiment_directory, MODEL_SAVE_DIRECTORY])
        checkpoint_path = model_path + os.path.sep + "cp-{epoch:04d}.ckpt"

        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path, verbose=0, save_weights_only=True, save_freq=1
        )

        callbacks = [
            CSVLogger(os.sep.join([experiment_directory, filename])),
            early_stopping
        ]

        if self.save_best:
            callbacks.append(best_weights_cb)

        if self.save_model:
            callbacks.append(cp_callback)

        return callbacks
