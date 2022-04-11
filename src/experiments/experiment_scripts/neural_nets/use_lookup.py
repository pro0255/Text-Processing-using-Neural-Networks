from src.experiments.experiment_scripts.experiment_configurations.lookup import (
    LOOKUP_KEY, gutenberg_lookup_normalization, gutenberg_lookup_seq)


def use_lookup_seq(value, current_authors, current_sentences, preprocessing_type):
    if value != LOOKUP_KEY:
        return value

    key = (current_authors, current_sentences, preprocessing_type)
    return gutenberg_lookup_seq.get(key, None)


def use_lookup_normalization(value, current_authors, current_sentences):
    if value != LOOKUP_KEY:
        return value

    key = (current_authors, current_sentences)
    return gutenberg_lookup_normalization.get(key, None)
