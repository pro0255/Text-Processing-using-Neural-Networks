import os

from src.types.suffix import Suffix

"""
Global project configuration. These variables was used around all project. Specific description is situated next to varible.
"""


#Size of automatic stamp value
STAMP_SIZE = 5

#Name of whole dataset
FILE_DATA_NAME = f"data{Suffix.CSV.value}"

#Name of file with statistics
NAME_OF_STATISTICS_FILE = "stats_"

#Specific file for statistics
SPECIFIC_DIRECTORY_FOR_STATISTICS = None

#Subdirectory for statistics
STATISTICS_SUBDIRECTORY = "statistics"

#Name of file where are saved sizes of train, test, valid sets
NAME_OF_FILE_WITH_SUBSET_SIZES = f"subset_sizes{Suffix.CSV.value}"

#Name of file with logs for nn
NAME_OF_LEARNING_LOGS = f"logs{Suffix.CSV.value}"

#Variables which describes ROOT of project
# ROOT = "C:\\Users\\Vojta\\Desktop\\diploma"
ROOT = "/home/usp/pro0255/diploma"

#Variable which describes where all authors.csv is downloaded. This file is created with .R script.
PATH_TO_ALL_AUTHORS = os.sep.join([ROOT, "gutenberg_downloaded\\authors\\authors.csv"])

#Delimited used in authors.csv
ALL_AUTHORS_DELIMITER = ","

#Delimiter used in other .csv files
PROJECT_CSV_DELIMITER = ";"

#Varible which describes where should be lib properties downloaded (for NLTK library)
NLTK_PATH = os.path.sep.join([ROOT, "nltk_data"])

#Name of file where are exceptions during dataset building process saved
LOG_FILE_NAME = "log.csv"


PATH_TO_DATASET_FOLDER_TEST = os.sep.join([ROOT, "data_test"])
TEST_DIR = PATH_TO_DATASET_FOLDER_TEST + os.path.sep + "gutenberg"

#Size of train set
TRAIN_SIZE = 0.7

#Size of validation set
VALIDATION_SIZE = 0.15

#Size of test set
TEST_SIZE = 0.15

#Directory where all datasets are saved ... \gutenberg\{NumberOfAuthors}Authors\Sentence{NumberOfSentences}
PATH_TO_DATASET_FOLDER = os.path.sep.join([ROOT, "data"])


#Directory where are all .json files donwloaded
real_dir = os.path.sep.join([ROOT, "gutenberg_downloaded\\data"])

#Directory where are all .json files donwloaded
GUTENBERG_DOWNLOADED_DIRECTORY = real_dir

#Pattern which will be used when iterates over directory
PATTERN = f"*{Suffix.JSON.value}"

#Name of authors.csv file
AUTHORS_FILE_NAME = f"authors{Suffix.CSV.value}"

#Directory where should be saved gutenberg datasets
GUTENBERG_DIRECTORY_TO_SAVE_BUILDED_DATASETS = os.path.sep.join(
    [ROOT, "data\\gutenberg"]
)

#Directory where should be saved all experiments
EXPERIMENT_RESULTS_DIRECTORY = os.path.sep.join([ROOT, "experiment_results"])

#Directory where should be saved whole nn model
MODEL_SAVE_DIRECTORY = "model"


#Name of file where is saved result (Confusion Matrix)
FILENAME_CONFUSION_MATRIX = f"confusion_matrix{Suffix.CSV.value}"

#Name of file where is saved result (Metrics .. Acuracy, Recall)
FILENAME_METRICS = f"metrics{Suffix.CSV.value}"

#Name of file where is saved description (ExperiementDescription)
FILENAME_DESCRIPTION = f"description{Suffix.CSV.value}"

#Name of file where is saved summarization (ExperimentSummarization)
FILENAME_SUMMARIZATION = f"summarization{Suffix.CSV.value}"

#Name of file where is saved log (CSVLogger)
FILENAME_LOGS = f"logs{Suffix.CSV.value}"

#Delimiter used in log
LOG_SEP = ";"


#Variable which should be empty will have value Nada
BLANK_DESCRIPTION = "Nada"


def get_current_folder(testing=False):
    return PATH_TO_DATASET_FOLDER_TEST if testing else PATH_TO_DATASET_FOLDER


#Name of column from DataFrame where is text situated
TEXT_COLUMN = "text"

#Name of column from DataFrame where is label situated
LABEL_COLUMN = "label"

#Suffix which should be used when creating undersampled .csv files train, test, valid.. in the end not used in project
NORMALIZATION_SUFFIX = "Labels"

#Random state which is used for shuffling, splitting. With this approach all models worked with same data.
RANDOM_STATE = 7

#Name of file where should be saved beste weights (ModelCheckpoint)
BEST_WEIGHTS_NAME = "weights.best.hdf5"

#Name of file where should be logged all output messages which are generated in jupyter output
JUPYTER_LOG_NAME = "jupyter_log.txt"
