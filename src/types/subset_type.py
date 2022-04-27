from enum import Enum


class SubsetType(Enum):
    """Subset types which are used in project.
    """
    Train = "train"
    Test = "test"
    Valid = "valid"
    All = "all"
