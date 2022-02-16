from src.data_preparing.split.run_split_deps_on_stats import run_split_deps_on_stats_same_dir
from src.utils.create_path_to_gutenberg import create_path_to_gutenberg_sentence_authors_sentence


#TODO: please calculate stats before :]
def run_split_with_normalization(
    number_of_authors, 
    number_of_sentences,
    f,
    t,
    step
):
    path = create_path_to_gutenberg_sentence_authors_sentence(number_of_authors, number_of_sentences)

    for normalized_value in range(f, t, step):
        run_split_deps_on_stats_same_dir(path, False, normalized_value)
