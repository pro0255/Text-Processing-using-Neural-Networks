class ExperimentRunner:
    def __init__(self) -> None:
        pass

    def run_experiments(self, experiments):
        for experiment in experiments:
            experiment.run()
