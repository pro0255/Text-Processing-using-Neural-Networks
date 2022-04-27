from src.config.config import PROJECT_CSV_DELIMITER


def preprocess_delimiter(document: str) -> str:
    """Method which helps to remove used delimiter in text segmentation.

    Args:
        document (str): document

    Returns:
        str: transformer document
    """
    return document.replace(PROJECT_CSV_DELIMITER, "")
