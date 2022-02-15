import tensorflow as tf
from src.types.transformer_pooling import TransformerPooling

class BertPoolingLayer(tf.keras.layers.Layer):

    def call(self, inputs, pooling_type):
        if pooling_type == TransformerPooling.LastHiddenState:
            last_hidden_state = inputs[TransformerPooling.LastHiddenState.value]
            return tf.reduce_mean(last_hidden_state, axis=1)
            
        if pooling_type == TransformerPooling.Pooler:
            pooler = inputs[TransformerPooling.Pooler.value]
            return pooler
                
        if pooling_type == TransformerPooling.HiddenStates:
            #TODO: deal with hidden state - bugs here! does not work!
            selector = inputs[TransformerPooling.HiddenStates.value]
            
            layers = tf.convert_to_tensor(selector)[-1]
            
            if tf.shape(tf.shape(layers)) > 3:
                layers = tf.reduce_mean(layers, axis=0, keepdims=False)
                #cls = layers[:, 0, :]
                average_sentence_words = tf.reduce_mean(layers[:, 1:tf.shape(layers)[1]-1, :], axis=1)
                return average_sentence_words
            else:
                #cls = layers[:, 0, :]
                average_sentence_words = tf.reduce_mean(layers[:, 1:tf.shape(layers)[1]-1, :], axis=1)
                return average_sentence_words