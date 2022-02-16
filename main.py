
import imp
from src.data_preparing.build.gutenberg_builder import GutenbergBuilder
from src.app.project_setup import ProjectSetup
from src.data_preparing.split.run_split_deps_on_stats import run_split_deps_on_stats_same_dir
from src.utils.create_path_to_gutenberg import create_path_to_gutenberg_sentence_authors_sentence, create_path_to_gutenberg_authors
from src.utils.create_test_dataset_from import create_test_dataset_from
from src.data_preparing.split.run_split_deps_on_stats import run_split_deps_on_stats_same_dir
from src.utils.create_path_to_gutenberg import create_path_to_gutenberg_sentence_authors_sentence
from src.config.config import PATH_TO_DATASET_FOLDER_TEST, PATH_TO_DATASET_FOLDER_TEST, AUTHORS_FILE_NAME

from src.tokenizers.prepare_dataset_from_tokenizer import prepare_dataset_from_tokenizer
from src.tokenizers.transformer_tokenizer import TransformerTokenizer
import tensorflow as tf
from src.encoder.create_encoder_from_path import create_encoder_from_path
from src.testing.get_testing_dataset import dataset
from src.data_loading.get_dataset_object_from import get_dataset_object_from_path
from src.utils.create_path_to_gutenberg import get_paths_to_gutenberg

#path = create_path_to_gutenberg_sentence_authors_sentence(10, 3)
#run_split_deps_on_stats_same_dir(path)

#g_builder = GutenbergBuilder()
#g_builder.build_dataset(3, 10)

#setup = ProjectSetup()
#setup.setup_datasets()


#create_test_dataset_from(10, 3, 100)

#test_path = create_path_to_gutenberg_sentence_authors_sentence(10, 3, PATH_TO_DATASET_FOLDER_TEST)
#run_split_deps_on_stats_same_dir(test_path)


# path_data, path_authors = get_paths_to_gutenberg(10, 3, PATH_TO_DATASET_FOLDER_TEST)
# dataset = get_dataset_object_from_path(path_data, ';', None)

# model_name = "bert-base-uncased"

# tokenizer = TransformerTokenizer(
#     model_name, 
#     create_encoder_from_path(
#         path_authors
#     )
# )

# for x in dataset:
#     print(x)
#     break

# for x in prepare_dataset_from_tokenizer(dataset, tokenizer).batch(10):
#     print(x)
#     break



from src.data_preparing.split.run_split_deps_on_stats import run_split_deps_on_stats_same_dir
from src.utils.create_path_to_gutenberg import create_path_to_gutenberg_sentence_authors_sentence

path = create_path_to_gutenberg_sentence_authors_sentence(10, 3)

run_split_deps_on_stats_same_dir(path, False, 100)