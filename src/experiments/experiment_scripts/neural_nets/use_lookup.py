import typing

from src.experiments.experiment_scripts.experiment_configurations.lookup import (
    LOOKUP_KEY,
    gutenberg_lookup_normalization,
    gutenberg_lookup_seq,
)
from src.types.processing_type import PreprocessingType


def use_lookup_seq(
    value: typing.Union[str, int],
    current_authors: int,
    current_sentences: int,
    preprocessing_type: PreprocessingType,
):
    if value != LOOKUP_KEY:
        return value

    key = (current_authors, current_sentences, preprocessing_type)
    return gutenberg_lookup_seq.get(key, None)


def use_lookup_normalization(
    value: typing.Union[str, int], current_authors: int, current_sentences: int
):
    if value != LOOKUP_KEY:
        return value

    key = (current_authors, current_sentences)
    return gutenberg_lookup_normalization.get(key, None)
