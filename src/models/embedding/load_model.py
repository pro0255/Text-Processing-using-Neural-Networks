import gzip
import numpy as np

def load_model(File):
    with gzip.open(File, 'r') as f:
        model = {}
        for line in f:        
            splitLines = line.split()
            word = splitLines[0].decode("utf-8")
            wordEmbedding = np.array([float(value) for value in splitLines[1:]])
            model[word] = wordEmbedding
    print(len(model)," words loaded!")
    return model