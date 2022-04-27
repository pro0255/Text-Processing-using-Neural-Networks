def preprocess_newlines(document: str) -> str:
    """Method which helps with transformation of document. From input are removed all newlines.

    Args:
        document (str): document

    Returns:
        str: document where are replaced newlines
    """
    return document.replace("\n", "")
