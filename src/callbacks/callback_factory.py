import tensorflow as tf
from src.callbacks.csv_callback import CSVLogger
import os
from src.config.config import NAME_OF_LEARNING_LOGS, EXPERIMENT_RESULTS_DIRECTORY, MODEL_SAVE_DIRECTORY

class CallbacksFactory:
    def __init__(self, save_model):
        self.save_model = save_model
    
    def create(
        self, 
        experiment_id: str, 
        directory: str = EXPERIMENT_RESULTS_DIRECTORY, 
        filename: str = NAME_OF_LEARNING_LOGS
    ) -> list:
        early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
        model_path = os.sep.join([directory, experiment_id, MODEL_SAVE_DIRECTORY])
        checkpoint_path = model_path + os.path.sep + "cp-{epoch:04d}.ckpt"

        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path, 
            verbose=0, 
            save_weights_only=True,
            save_freq=1
        )


        callbacks = [
            CSVLogger(os.sep.join([directory, experiment_id, filename])),
            early_stopping,
        ]

        if self.save_model:
            callbacks.append(cp_callback)


        return callbacks