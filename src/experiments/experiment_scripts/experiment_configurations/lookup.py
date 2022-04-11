from enum import Enum
from src.types.processing_type import PreprocessingType

LOOKUP_KEY = "LOOKUP_KEY"


class LookupField(Enum):
    SeqLen = "SeqLen"
    NormalizationSize = "NormalizationSize"


# number_of_authors, number_of_sentences, preprocessing_type
gutenberg_lookup_seq = {(5, 3, PreprocessingType.CaseInterpunction): 130}


# number_of_authors, number_of_sentences
gutenberg_lookup_normalization = {(5, 3): 15000}
