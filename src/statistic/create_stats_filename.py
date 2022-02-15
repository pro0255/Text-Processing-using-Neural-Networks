
from src.config.config import NAME_OF_STATISTICS_FILE
from src.utils.add_suffix import add_suffix
from src.types.suffix import Suffix
from src.utils.generate_random_stamp import generator_random_stamp


def create_stats_filename(name_of_file: str) -> str:
    return add_suffix(
        f'{NAME_OF_STATISTICS_FILE}{name_of_file}_stamp={generator_random_stamp()}', 
        Suffix.XLSX
    )





