import itertools
import pandas as pd
import typing

from src.analysis.stats.create_record import create_record
from src.types.processing_type import PreprocessingType
from src.types.subset_type import SubsetType
from src.types.transformer_name import TransformerName


def create_records(
    parent_path: str,
    norm_values: typing.List[int],
    preprocessing_types: typing.List[PreprocessingType],
    subset_types: typing.List[SubsetType],
    transformer_names: typing.List[typing.Union[TransformerName, None]],
) -> typing.List[typing.Type[pd.DataFrame]]:
    records = [
        create_record(*conf)
        for conf in itertools.product(
            [parent_path],
            norm_values,
            preprocessing_types,
            subset_types,
            transformer_names,
        )
    ]
    return records
