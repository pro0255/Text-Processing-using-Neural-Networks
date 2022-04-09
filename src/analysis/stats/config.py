from src.config.config import PATH_TO_DATASET_FOLDER, AUTHORS_FILE_NAME, FILE_DATA_NAME
from src.types.subset_type import SubsetType
from src.types.processing_type import PreprocessingType
from src.types.transformer_name import TransformerName

START_DIRECTORY = PATH_TO_DATASET_FOLDER
FILENAMES = [AUTHORS_FILE_NAME, FILE_DATA_NAME]
NORMALIZATION_VALUES = [15000]
PREPROCESSING_TYPES = list(
    filter(lambda x: x != PreprocessingType.Blank, list(PreprocessingType))
)
SUBSETS = [SubsetType.All]
TRANSFORMER_NAMES = [TransformerName.BertBaseUncased]
