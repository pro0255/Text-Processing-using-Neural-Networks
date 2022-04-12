import typing
from src.analysis.stats.create_records import create_records
from src.types.processing_type import PreprocessingType
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName


def process_path(
    parent_path: str, norm_values: typing.List[int], preprocessing_types:typing.List[PreprocessingType], subset_type: typing.List[SubsetType], transformer_names: typing.List[typing.Union[None, TransformerName]]
):
    return create_records(
        parent_path, norm_values, preprocessing_types, subset_type, transformer_names
    )
