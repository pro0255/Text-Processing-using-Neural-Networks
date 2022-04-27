import tensorflow as tf

"""
Variables which helped in implementation. According to this dataset was implemented big part of methods. Tokenization, run of experiments, vectorizers etc.
"""

text = ["Hello i am", "I like NLP", "Test here hate"]
labels = [12, 15, 20]
dataset = tf.data.Dataset.from_tensor_slices((text, labels))
