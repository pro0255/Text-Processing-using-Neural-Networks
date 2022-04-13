import typing

from src.experiments.experiment_scripts.classic.classic_runner import \
    ClassicRunner
from src.experiments.experiment_scripts.neural_nets.no_transformer.neural_net_runner import \
    NNRunner
from src.experiments.experiment_scripts.neural_nets.transformers.transformer_runner import \
    TransformerRunner
from src.experiments.experiment_scripts.test.test_config import \
    test_experiment_config
from src.experiments.experiment_scripts.types.experiment_types import \
    ExperimentType
from src.types.test_types import TestType


class TestRunner:
    def __init__(self) -> None:
        pass

    def run_tests(self, test_types: typing.List[TestType]) -> None:
        for current_t_t in test_types:
            self.run_test(current_t_t)

    def run_test(self, test_type: TestType) -> None:
        if test_type == TestType.Transformer:
            self.run_transformer_tests()
        elif test_type == TestType.Classic:
            self.run_classic_tests()
        elif test_type == TestType.NN:
            self.run_nn_tests()

    def run_transformer_tests(self) -> None:
        print("Running transformer tests!")

        runner = TransformerRunner(
            experiment_type=ExperimentType.TransformerTest, config_dict=test_experiment_config
        )
        runner.run()

        print("End of transformer tests!")

    def run_nn_tests(self) -> None:
        print("Running NN tests!")

        runner = NNRunner(experiment_type=ExperimentType.NNTest, config_dict=test_experiment_config)
        runner.run()

        print("End of NN tests!")

    def run_classic_tests(self) -> None:
        print("Running transformer tests!")

        runner = ClassicRunner(
            experiment_type=ExperimentType.ClassicTest, config_dict=test_experiment_config
        )
        runner.run()

        print("End of classic tests!")
