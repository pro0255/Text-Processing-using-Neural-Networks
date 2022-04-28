from enum import Enum

from src.statistic.instances.label_metric import LabelMetric
from src.statistic.instances.label_token_counter import LabelTokenMetric
from src.statistic.instances.sentence_length import SentenceLengthMetric
from src.statistic.instances.statistic_description import StatisticDescription
from src.statistic.instances.token_counter import TokenMetric
from src.statistic.instances.transformer_tokenizer import TransformerTokenizerCounter
from src.statistic.instances.quant_50_seq_len import Quant50SeqLen
from src.statistic.instances.quant_75_seq_len import Quant75SeqLen


class MetricType(Enum):
    TransformerTokenizerCounter = "TransformerTokenizerCounter"
    SentenceLength = "SentenceLength"
    LabelTokenCounter = "LabelTokenCounter"
    TokenCounter = "TokenCounter"
    LabelCounter = "LabelCounter"
    StatisticDescriptionType = "StatisticDescription"
    Quant50SeqLen = "Quant50SeqLen"
    Quant75SeqLen = "Quant75SeqLen"


def translate_instance_to_type(instance):
    name_of_instance = type(instance).__name__
    dic = {
        type(LabelMetric()).__name__: MetricType.LabelCounter.value,
        type(
            TransformerTokenizerCounter()
        ).__name__: MetricType.TransformerTokenizerCounter.value,
        type(SentenceLengthMetric()).__name__: MetricType.SentenceLength.value,
        type(LabelTokenMetric()).__name__: MetricType.LabelTokenCounter.value,
        type(TokenMetric()).__name__: MetricType.TokenCounter.value,
        type(
            StatisticDescription()
        ).__name__: MetricType.StatisticDescriptionType.value,
        type(Quant50SeqLen()).__name__: MetricType.Quant50SeqLen.value,
        type(Quant75SeqLen()).__name__: MetricType.Quant75SeqLen.value,
    }
    return dic[name_of_instance]
