from enum import Enum


class DataSetType(Enum):
    """Type of dataset segmentation. After all was implemented only sentence mechanism."""

    Sentence = "Sentence"
    Article = "Article"
