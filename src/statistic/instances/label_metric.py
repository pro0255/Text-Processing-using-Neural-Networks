import pandas as pd


class LabelMetric:
    def __init__(self):
        self.state = {}

    def update_state(self, text, label):
        self.state[label] = self.state.get(label, 0) + 1

    def get_dataframe(self):
        return pd.DataFrame.from_dict(self.state, orient="index")
