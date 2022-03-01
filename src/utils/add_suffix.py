from src.types.suffix import Suffix


def add_suffix(filename, suffix=Suffix.CSV) -> str:
    return f"{filename}{suffix.value}"
