import itertools

from src.config.learning_config import (BATCH_SIZE, EPOCHS, LEARNING_RATE,
                                        LOSS, METRIC, OPTIMIZER)


def settings_generator(
    batch_sizes, learning_rates, metrics, losses, optimizers, epochs
):
    confs = itertools.product(
        batch_sizes, learning_rates, metrics, losses, optimizers, epochs
    )
    for batch_size, lr, metric, loss, optimizer, epoch in confs:
        yield LearningSettings(
            batch_size=batch_size,
            learning_rate=lr,
            metric=metric,
            loss=loss,
            optimizer=optimizer,
            epochs=epoch,
        )


class LearningSettings:
    def __init__(
        self,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        learning_rate=LEARNING_RATE,
        loss=LOSS,
        metric=METRIC,
        optimizer=OPTIMIZER,
    ) -> None:
        self.batch_size = batch_size
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.metric = metric
        self.loss = loss
        self.optimizer = optimizer(learning_rate=self.learning_rate)
