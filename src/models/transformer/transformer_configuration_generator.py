import itertools
import typing
from src.experiments.settings.settings import LearningSettings
from src.models.transformer.pooling_strategy import TransformerPoolingStrategySelection

from src.types.transformer_name import TransformerName


def transformer_configuration_generator(
    model_names: typing.List[TransformerName], pooling_strategies:typing.List[TransformerPoolingStrategySelection], seq_lengths: typing.List[int], trainable: typing.List[bool], settings: typing.List[typing.Type[LearningSettings]]
):
    return itertools.product(
        model_names, pooling_strategies, seq_lengths, trainable, settings
    )
