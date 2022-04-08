import itertools
from src.analysis.stats.create_record import create_record

def create_records(parent_path, norm_values, preprocessing_types, subset_types, transformer_names):
    records = [create_record(*conf) for conf in itertools.product([parent_path], norm_values, preprocessing_types, subset_types, transformer_names)]
    return records