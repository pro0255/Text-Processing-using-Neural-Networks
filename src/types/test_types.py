from enum import Enum


class TestType(Enum):
    """Type of tests which was implemented. Can be tested run of experiments. All 3 blocks.
    """
    Transformer = "Transformer"
    Classic = "Classic"
    NN = "NN"
