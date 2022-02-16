import pandas as pd
from src.statistic.types.description_statistic import StatisticDescriptionField

class StatisticDescription:
    def __init__(
        self,
        number_of_authors=None,
        number_of_sentences=None,
        subset_type=None,
        path=None,
        preprocessing_type=None,
        transformer_tokenizer=None,
        normalization_size=None
    ):
        self.state = {}
        self.state[StatisticDescriptionField.NumberOfAuthors.value] = number_of_authors
        self.state[StatisticDescriptionField.NumberOfSentences.value] = number_of_sentences
        self.state[StatisticDescriptionField.SubsetType.value] = subset_type
        self.state[StatisticDescriptionField.Path.value] = path
        self.state[StatisticDescriptionField.PreprocessingType.value] = preprocessing_type
        self.state[StatisticDescriptionField.TransformerTokenizer.value] = transformer_tokenizer 
        self.state[StatisticDescriptionField.TransformerTokenizer.value] = normalization_size
 
    def update_state(self, text, label):
        pass
        
    def get_dataframe(self):
        return pd.DataFrame.from_dict(self.state, orient='index')

    def __str__(self) -> str:
        s = []
        for k, v in self.state.items():
            s.append(f"{k}={v}")
        return "\n".join(s)

