from src.config.learning_config import BATCH_SIZE, EPOCHS, LEARNING_RATE, LOSS, METRIC
import tensorflow as tf

class LearningSettings:    
    def __init__(self, 
        batch_size=BATCH_SIZE, 
        epochs=EPOCHS, 
        learning_rate=LEARNING_RATE, 
        loss=LOSS, 
        metric=METRIC
    ) -> None:

        self.batch_size = batch_size 
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.metric = metric
        self.loss = loss
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate, epsilon=1e-08)


    def __str__(self) -> str:
        #TODO
        pass

    def save(self):
        #TODO save to experiment folder
        pass
