from enum import Enum

from src.types.processing_type import PreprocessingType

"""
Lookup logic. When is known some kind of variable from exploratory data analysis then is saved here. From experiments configutaion we can then easily load this variable.
"""


LOOKUP_KEY = "LOOKUP_KEY"


class LookupField(Enum):
    SeqLen = "SeqLen"
    NormalizationSize = "NormalizationSize"


# number_of_authors, number_of_sentences, preprocessing_type
gutenberg_lookup_seq = {
    (5, 3, PreprocessingType.CaseInterpunction): 100,
    (5, 3, PreprocessingType.Default): 70,
    (5, 1, PreprocessingType.CaseInterpunction): 30,
    (5, 2, PreprocessingType.CaseInterpunction): 60,
    (5, 7, PreprocessingType.CaseInterpunction): 190,
    (5, 10, PreprocessingType.CaseInterpunction): 260,
    (5, 15, PreprocessingType.CaseInterpunction): 380,
    (15, 10, PreprocessingType.CaseInterpunction): 260,
    (25, 10, PreprocessingType.CaseInterpunction): 260,
    (15, 3, PreprocessingType.CaseInterpunction): 90,
    (25, 3, PreprocessingType.CaseInterpunction): 90,
}


# number_of_authors, number_of_sentences
gutenberg_lookup_normalization = {
    (5, 3): 15000,
    (5, 1): 45000,
    (5, 2): 22500,
    (5, 7): 6500,
    (5, 10): 4500,
    (5, 15): 3000,
    (15, 10): 5000,
    (25, 10): 3000,
    (75, 10): 3000,
    (55, 10): 3000,
    (105, 10): 3000,
    (15, 3): 5000,
    (25, 3): 3000,
    (55, 3): 3000,
    (75, 3): 3000,
    (105, 3): 3000,
}
