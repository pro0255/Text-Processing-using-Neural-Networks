import tensorflow as tf

def get_dataset_object_from_path(csv_filename, delim, text_pipeline_func=None):
    print(f"Loading dataset from={csv_filename}")
    dataset = tf.data.TextLineDataset(filenames=csv_filename)
    
    def parse_csv(line):
        csv_line = bytes.decode(line.numpy())
        text, author = csv_line.split(delim)
        if text_pipeline_func is not None:
            text = text_pipeline_func(text)
        return text, int(author) 

    dataset = dataset.map(lambda tpl: tf.py_function(parse_csv, [tpl], [tf.string, tf.int32]))
    return dataset



def get_datasets(csv_filenames, delim, text_pipeline_func=None):
    datasets = [
        get_dataset_object_from_path(
            csv_filename, delim, 
            text_pipeline_func) for csv_filename in csv_filenames
    ]
    return datasets




