import pandas as pd
from transformers import AutoTokenizer

from src.statistic.DEFAULT_DIC_VALUE import DEFAULT_DIC_VALUE
from src.statistic.utils.avg_min_max_updater import AvgMaxMinUpdate
from src.types.transformer_input import TransformerInput
from src.types.transformer_name import TransformerName


class TransformerTokenizerCounter:
    def __init__(self, model_name=TransformerName.BertBaseUncased.value):
        self.state = {}
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.updater = AvgMaxMinUpdate()

    def update_state(self, text, label):
        current_dic = self.state.get(label, DEFAULT_DIC_VALUE)

        current_length = len(self.tokenizer(text)[TransformerInput.input.value])

        self.state[label] = self.updater.update(current_dic, current_length, label)

    def get_dataframe(self):
        return pd.DataFrame.from_dict(self.state, orient="index")
