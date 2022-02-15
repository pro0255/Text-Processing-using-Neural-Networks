import pandas as pd
from src.statistic.DEFAULT_DIC_VALUE import DEFAULT_DIC_VALUE
from src.statistic.utils.avg_min_max_updater import AvgMaxMinUpdate


#TODO: add mean avg streaming 
class LabelTokenMetric:
    def __init__(self):
        self.state = {}
        self.updater = AvgMaxMinUpdate()
    
    def update_state(self, text, label):
        current_dic = self.state.get(label, DEFAULT_DIC_VALUE)

        splitted_text = text.split(' ')

        current_length = len(splitted_text)

        self.state[label] = self.updater.update(current_dic, current_length)

    def get_dataframe(self):
        return pd.DataFrame.from_dict(self.state, orient='index')