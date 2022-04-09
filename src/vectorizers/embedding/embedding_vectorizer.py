import gensim.downloader
import numpy as np


class EmbeddingVectorizer:
    def __init__(self, embedding_type):
        self.embedding_type = embedding_type.value
        self.missed = 0
        self.counter = 0
        self.embedding_size = 0
        self.setup()

    def setup(self):
        self.vectors = gensim.downloader.load(self.embedding_type)
        self.embedding_size = len(self.vectors["king"])

    def get_from_vectors(self, key_vectors, key):
        self.counter += 1
        try:
            return key_vectors[key]
        except:
            self.missed += 1
            return np.zeros(shape=(self.embedding_size,))

    def get_state(self):
        missed, counter, accuracy = (
            self.missed,
            self.counter,
            100 * (self.missed / self.counter),
        )
        print(f"Missed={missed}, counter={counter}, accuracy={accuracy}")
        return missed, counter, accuracy

    def get_mean(self, corpus):
        return [np.mean(sent, axis=0) for sent in corpus]

    def fit_transform(self, X):
        self.missed = 0
        self.counter = 0

        corpus = []

        for sentence in X:
            tokens = sentence.split(" ")
            sentence_embedding = []
            for token in tokens:
                embedding_of_token = self.get_from_vectors(self.vectors, token)
                sentence_embedding.append(embedding_of_token)
            corpus.append(np.array(sentence_embedding))

        return self.get_mean(corpus)

