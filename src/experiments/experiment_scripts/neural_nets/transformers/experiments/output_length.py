from src.experiments.experiment_scripts.types.experiment_types import ExperimentType
from src.experiments.experiment_scripts.neural_nets.transformers.transformer_runner import TransformerRunner


class TransformerOutputSequenceLenght(TransformerRunner):
    def __init__(
        self,
        save_model=False,
    ) -> None:
        super().__init__(
            experiment_type=ExperimentType.OutputSequenceLengthTransformer,
            save_model=save_model
        )