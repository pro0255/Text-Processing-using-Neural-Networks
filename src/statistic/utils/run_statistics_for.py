
from src.statistic.create_statistics_from import create_statistics_from
from src.statistic.build_input_for_statistics import build_input_for_statistics
from src.utils.create_path_to_gutenberg import get_path_to_gutenberg_sets
from src.config.config import get_current_folder
from src.preprocessing.preprocessing_factory import PreprocessingFactory
from src.types.processing_type import PreprocessingType
from src.statistic.instances.statistic_description import StatisticDescription
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName
from src.statistic.DEFAULT_INSTANCES import build_statistic_instances
import itertools


def get_subset_path_index(subset_type):
    dic = {
        SubsetType.Train: 0,
        SubsetType.Valid: 1,
        SubsetType.Test: 2
    }
    return dic[subset_type]

def run_statistics_for(
    authors,
    sentences,
    preprocessing_types=[PreprocessingType.Default],
    subset_types=[SubsetType.Train.value]
):
    number_of_authors_start, number_of_authors_end, step_authors = authors
    number_of_sentences_start, number_of_sentences_end, step_sentences = sentences

    combs = (
        list(
            itertools.product
            (
                list(range(number_of_authors_start, number_of_authors_end, step_authors)), 
                list(range(number_of_sentences_start, number_of_sentences_end, step_sentences)),
                preprocessing_types,
                subset_types
            )
        )
    )


    for author_number, sentence_number, preprocessing, subset in combs:
        print(f"Statistics for author={author_number} sentence={sentence_number} preprocessing={preprocessing} subset={subset}")
        current_folder = get_current_folder()

        paths_data, _ = get_path_to_gutenberg_sets(
            author_number, 
            sentence_number,
            current_folder
        )


        current_index = get_subset_path_index(subset)
        current_path = paths_data[current_index]

        factory = PreprocessingFactory()

        stat_description = StatisticDescription(
            number_of_authors=author_number,
            number_of_sentences=sentence_number,
            subset_type=subset.value,
            path=current_path,
            preprocessing_type=preprocessing.value,
            transformer_tokenizer=TransformerName.BertBaseUncased.value
        )

        metric_instance = create_statistics_from(
            *build_input_for_statistics(
                current_path,
                ';', 
                stat_description,
                build_statistic_instances(TransformerName.BertBaseUncased.value), 
                factory.create(preprocessing),
                True
            )
        )
