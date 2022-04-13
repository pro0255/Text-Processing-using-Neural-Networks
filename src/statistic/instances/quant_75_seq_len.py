import pandas as pd
import numpy as np


class Quant75SeqLen:
    def __init__(self):
        self.state = {}

    def update_state(self, text, label):

        current_list = self.state.get(label, [])

        splitted_text = text.split(" ")
        
        current_length = len(splitted_text)

        current_list.append(current_length)

        self.state[label] = current_list

    def get_dataframe(self):
        dic = {k:np.quantile(v, 0.75) for k, v in self.state.items()}
        
        mem_all = []
        for x in self.state.values():
            mem_all += x
            
        value_together = np.quantile(mem_all, 0.75)

        dic['All'] = value_together

        return pd.DataFrame.from_dict(dic, orient="index")
