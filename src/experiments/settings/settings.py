import itertools
import typing

from src.config.learning_config import (BATCH_SIZE, EPOCHS, LEARNING_RATE,
                                        LOSS, METRIC, OPTIMIZER)


def settings_generator(
    batch_sizes:typing.List[int], learning_rates:typing.List[float], metrics:typing.List, losses:typing.List, optimizers:typing.List, epochs:typing.List[int]
):
    print(epochs)
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
        batch_size:int=BATCH_SIZE,
        epochs:int=EPOCHS,
        learning_rate:float=LEARNING_RATE,
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

    def __str__(self) -> str:
        res = ""
        res += f"BatchSize={self.batch_size}"
        res += f"Epochs={self.epochs}"
        res += f"LearningRate={self.learning_rate}"
        res += f"Metric={self.metric}"
        res += f"Loss={self.loss}"
        res += f"Optimizer={self.optimizer}"
        return res
