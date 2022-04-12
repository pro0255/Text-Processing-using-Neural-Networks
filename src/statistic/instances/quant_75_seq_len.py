import pandas as pd
import numpy as np


class Quant75SeqLen:
    def __init__(self):
        self.mem = []

    def update_state(self, text, label):

        splitted_text = text.split(" ")
        
        current_length = len(splitted_text)

        self.mem.append(current_length)


    def get_dataframe(self):
        self.state = {"Value": np.quantile(self.mem, 0.75)}
        return pd.DataFrame.from_dict(self.state, orient="index")
