import tensorflow as tf

BATCH_SIZE = 32
LEARNING_RATE = 2e-5
EPOCHS = 1
METRIC = tf.keras.metrics.SparseCategoricalAccuracy('accuracy') 
LOSS = tf.keras.losses.SparseCategoricalCrossentropy()
