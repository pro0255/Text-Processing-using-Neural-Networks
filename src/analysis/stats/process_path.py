from src.analysis.stats.create_records import create_records


def process_path(
    parent_path, norm_values, preprocessing_types, subset_type, transformer_names
):
    return create_records(
        parent_path, norm_values, preprocessing_types, subset_type, transformer_names
    )
