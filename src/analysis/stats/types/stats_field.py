from enum import Enum

class StatsField(Enum):
    Path = "Path"
    NumberOfAuthors = "NumberOfAuthors"
    NumberOfSentences = "NumberOfSentences"
    CalculationTime = "CalculationTime"
    PreprocessingType = "PreprocessingType"
    NormalizationValue = "NormalizationValue"
    SubsetType = "SubsetType"    
    TransformerName = "TransformerName"
    Authors = "Authors"