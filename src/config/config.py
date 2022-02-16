from src.types.suffix import Suffix
import os

STAMP_SIZE = 5

USE_TESTING_DATASET_FOLDER = True

FILE_DATA_NAME = f'data{Suffix.CSV.value}'

NAME_OF_STATISTICS_FILE = 'stats_'
SPECIFIC_DIRECTORY_FOR_STATISTICS = None
STATISTICS_SUBDIRECTORY = "statistics"


NAME_OF_FILE_WITH_SUBSET_SIZES = f"subset_sizes{Suffix.CSV.value}" 
NAME_OF_LEARNING_LOGS = f'logs{Suffix.CSV.value}'

ROOT = "C:\\Users\\Vojta\\Desktop\\diploma"
#ROOT = "/home/usp/pro0255/diploma"

PATH_TO_ALL_AUTHORS = os.sep.join([ROOT, "gutenberg_downloaded\\authors\\authors.csv"])
ALL_AUTHORS_DELIMITER = ","

PROJECT_CSV_DELIMITER = ";"

NLTK_PATH = os.path.sep.join([ROOT, "nltk_data"])
LOG_FILE_NAME = 'log.csv'


PATH_TO_DATASET_FOLDER_TEST = os.sep.join([ROOT, "data_test"])
TEST_DIR = PATH_TO_DATASET_FOLDER_TEST + os.path.sep + "gutenberg"


TRAIN_SIZE = 0.7
VALIDATION_SIZE = 0.15
TEST_SIZE = 0.15

PATH_TO_DATASET_FOLDER = os.path.sep.join([ROOT, "data"])


real_dir = os.path.sep.join([ROOT, "gutenberg_downloaded\\data"])
testing_dir = os.path.sep.join([ROOT, "gutenberg_test"])

GUTENBERG_DOWNLOADED_DIRECTORY = real_dir
PATTERN = f"*{Suffix.JSON.value}"
AUTHORS_FILE_NAME = f'authors{Suffix.CSV.value}'
GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS = os.path.sep.join([ROOT, "data\\gutenberg"])


EXPERIMENT_RESULTS_DIRECTORY = os.path.sep.join([ROOT, "experiment_results"])
MODEL_SAVE_DIRECTORY = "model"

FILENAME_CONFUSION_MATRIX = f"confusion_matrix{Suffix.CSV.value}"
FILENAME_METRICS = f"metrics{Suffix.CSV.value}"
FILENAME_DESCRIPTION = f"description{Suffix.CSV.value}"
FILENAME_SUMMARIZATION = f"summarization{Suffix.CSV.value}"

LOG_SEP = ';'

BLANK_DESCRIPTION = "Nada"

#"/home/usp/pro0255/diploma"

def get_current_folder(testing=USE_TESTING_DATASET_FOLDER):
    return PATH_TO_DATASET_FOLDER_TEST if testing else PATH_TO_DATASET_FOLDER

TEXT_COLUMN = "text"
LABEL_COLUMN = "label"
