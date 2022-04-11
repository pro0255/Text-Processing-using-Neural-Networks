import tensorflow as tf


def load_files(path: str):
    return tf.data.Dataset.list_files(path, shuffle=False)
