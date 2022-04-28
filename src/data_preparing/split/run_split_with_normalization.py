from src.data_preparing.split.run_split_deps_on_stats import \
    run_split_deps_on_stats_same_dir
from src.utils.create_path_to_gutenberg import \
    create_path_to_gutenberg_sentence_authors_sentence


def run_split_with_normalization(
    number_of_authors: int, number_of_sentences: int, f: int, t: int, step: int
):
    """
    Run split with automatic normalization.

    This methods was not in the end used in project.
    
    Args:
        number_of_authors (int): number of authors
        number_of_sentences (int): number of sentences
        f (int): where should normalization start
        t (int): where should normalization end
        step (int): step which shoud be made
    """
    path = create_path_to_gutenberg_sentence_authors_sentence(
        number_of_authors, number_of_sentences
    )

    for normalized_value in range(f, t, step):
        run_split_deps_on_stats_same_dir(path, False, normalized_value)
