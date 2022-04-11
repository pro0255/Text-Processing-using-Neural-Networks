from src.types.suffix import Suffix


def add_suffix(filename:str, suffix:Suffix =Suffix.CSV) -> str:
    return f"{filename}{suffix.value}"
