from enum import Enum

class SubsetType(Enum):
    Train = 'train'
    Test = 'test'
    Valid = 'valid'
    All = 'all'