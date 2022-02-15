from src.config.config import PROJECT_CSV_DELIMITER

def preprocess_delimiter(document: str) -> str:
    return document.replace(PROJECT_CSV_DELIMITER, '')