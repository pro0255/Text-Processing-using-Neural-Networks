import itertools

def transformer_configuration_generator(
    model_names, 
    pooling_strategies, 
    seq_lengths, 
    trainable,
    settings
    ):
    return itertools.product(model_names, pooling_strategies, seq_lengths, trainable, settings)







