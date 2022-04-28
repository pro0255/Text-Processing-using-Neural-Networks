from src.statistic.instances.label_metric import LabelMetric
from src.statistic.instances.label_token_counter import LabelTokenMetric
from src.statistic.instances.sentence_length import SentenceLengthMetric
from src.statistic.instances.quant_50_seq_len import Quant50SeqLen
from src.statistic.instances.quant_75_seq_len import Quant75SeqLen
from src.statistic.instances.sentence_length import SentenceLengthMetric
from src.statistic.instances.token_counter import TokenMetric
from src.statistic.instances.transformer_tokenizer import TransformerTokenizerCounter
from src.types.transformer_name import TransformerName

DEFULT_WITHOUT_TRANSFORMER_INSTANCES = [
    LabelMetric(),
    LabelTokenMetric(),
    SentenceLengthMetric(),
    TokenMetric(),
]

DEFAULT_STATISTICS_INSTANCES = DEFULT_WITHOUT_TRANSFORMER_INSTANCES.copy().append(
    TransformerTokenizerCounter()
)


def build_default_instances():
    instances = []
    instances.append(LabelMetric())
    instances.append(LabelTokenMetric())
    instances.append(SentenceLengthMetric())
    instances.append(TokenMetric())
    instances.append(Quant50SeqLen())
    instances.append(Quant75SeqLen())
    return instances


def build_statistic_instances(model_name=TransformerName.BertBaseUncased.value):
    instances = build_default_instances()
    if model_name is not None:
        instances.append(TransformerTokenizerCounter(model_name))
    return instances
