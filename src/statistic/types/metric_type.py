from enum import Enum

from src.statistic.instances.label_metric import LabelMetric
from src.statistic.instances.label_token_counter import LabelTokenMetric
from src.statistic.instances.sentence_length import SentenceLengthMetric
from src.statistic.instances.statistic_description import StatisticDescription
from src.statistic.instances.token_counter import TokenMetric
from src.statistic.instances.transformer_tokenizer import TransformerTokenizerCounter


class MetricType(Enum):
    TransformerTokenizerCounter = "TransformerTokenizerCounter"
    SentenceLength = "SentenceLength"
    LabelTokenCounter = "LabelTokenCounter"
    TokenCounter = "TokenCounter"
    LabelCounter = "LabelCounter"
    StatisticDescriptionType = "StatisticDescription"


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
    }
    return dic[name_of_instance]
