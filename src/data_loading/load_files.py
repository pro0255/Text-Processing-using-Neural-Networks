import tensorflow as tf


def load_files(path):
    return tf.data.Dataset.list_files(path, shuffle=False)
