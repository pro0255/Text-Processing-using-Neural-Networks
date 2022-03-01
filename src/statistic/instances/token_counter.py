import pandas as pd


class TokenMetric:
    def __init__(self):
        self.state = {}

    def update_state(self, text, label):
        current_dic_token_counter = self.state.get(label, {})

        tokens = text.split(" ")

        for token in tokens:
            current_token_count = current_dic_token_counter.get(token, 0) + 1
            current_dic_token_counter[token] = current_token_count

        self.state[label] = current_dic_token_counter

    def get_dataframe(self):
        return (
            pd.DataFrame.from_dict(self.state, orient="index").T.fillna(0).astype(int)
        )
