from enum import Enum

class StatisticDescriptionField(Enum):
    NumberOfAuthors = "NumberOfAuthors"
    NumberOfSentences = "NumberOfSentences"
    NormalizationSize = "NormalizationSize" 
    SubsetType = "SubsetType"
    Path = "Path"
    PreprocessingType = "PreprocessingType"
    TransformerTokenizer = "TransformerTokenizer"
