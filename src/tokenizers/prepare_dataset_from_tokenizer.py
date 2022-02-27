import tensorflow as tf

def prepare_dataset_from_tokenizer(dataset, tokenizer):
    return dataset.map(tokenizer.ty_py_func, num_parallel_calls=tf.data.AUTOTUNE).map(tokenizer.to_model_input,num_parallel_calls=tf.data.AUTOTUNE)

