import tensorflow as tf


def load_files(path: str):
    """Load all files from path.

    Args:
        path (str): path which should be loaded

    Returns:
        _type_: generator of dataset objects
    """
    return tf.data.Dataset.list_files(path, shuffle=False)
