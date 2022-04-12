from src.experiments.experiment_scripts.neural_nets.transformers.transformer_runner import \
    TransformerRunner
from src.experiments.experiment_scripts.types.experiment_types import \
    ExperimentType


class TransformerLearningRate(TransformerRunner):
    def __init__(
        self,
        save_model: bool = False,
    ) -> None:
        super().__init__(
            experiment_type=ExperimentType.LearningRateTransformer,
            save_model=save_model,
        )
