import tensorflow as tf

BATCH_SIZE = 128
LEARNING_RATE = 2e-5
EPOCHS = 10
TRANSFORMER_EPOCHS = 3
METRIC = tf.keras.metrics.SparseCategoricalAccuracy("accuracy")
LOSS = tf.keras.losses.SparseCategoricalCrossentropy()


# TRANSFORMER_LR = [
#     0.001,
#     5e-5, 
#     4e-5, 
#     3e-5, 
#     2e-5    
# ]

