import tensorflow as tf

text = ['Hello i am', 'I like NLP', 'Test here hate']
labels = [12, 15, 20]
dataset = tf.data.Dataset.from_tensor_slices((text, labels))