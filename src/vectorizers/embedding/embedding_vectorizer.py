import typing

import gensim.downloader
import numpy as np

from src.config.loaded_models import loaded_models
from src.types.downloaded_embeddings_type import DownloadedEmbeddingType


class EmbeddingVectorizer:
    def __init__(
        self, embedding_type: DownloadedEmbeddingType, run_on_init: bool = False
    ) -> None:
        self.embedding_type = embedding_type.value
        self.missed = 0
        self.counter = 0
        self.embedding_size = 0
        self.vectors = None
        self.embedding_size = None
        if run_on_init:
            self.setup()

    def setup(self):
        """According to specified embedding type will be downloaded vectors.
        """
        if self.vectors is None or self.embedding_size is None:
            print(f"Downloading model {self.embedding_type}!")
            if self.embedding_type in loaded_models:
                print(f"Already loaded model={self.embedding_type}")
                self.vectors = loaded_models[self.embedding_type]
            else:
                print(f"Loading model={self.embedding_type}")
                self.vectors = gensim.downloader.load(self.embedding_type)
            self.embedding_size = len(self.vectors["king"])
            print(f"Current embedding size is {self.embedding_size}")
        else:
            print("Already downloaded")

    def get_from_vectors(self, key_vectors: typing.Dict, key: str):
        """Will try to get vector for word. If word does exists in embedding, then empty vector will be returned.

        Args:
            key_vectors (typing.Dict): Dictionary of vectors.
            key (str): Current word.

        Returns:
            _type_: Vector of embedding size. Empty if word does not exist.
        """
        self.counter += 1
        try:
            return key_vectors[key]
        except:
            self.missed += 1
            return np.zeros(shape=(self.embedding_size,))

    def get_state(self):
        """Get state of vectorize process. Number of missed and not missed words.

        Returns:
            (int, int, float): State of embedding process.
        """
        missed, counter, accuracy = (
            self.missed,
            self.counter,
            100 * (self.missed / self.counter),
        )
        print(f"Missed={missed}, counter={counter}, accuracy={accuracy}")
        return missed, counter, accuracy

    def get_mean(self, corpus):
        return [np.mean(sent, axis=0) for sent in corpus]

    def fit_transform(self, X: typing.List[typing.List[str]]):
        """Run setup of vectorizer. Process of download vectors.

        Sentence is splitted to tokens. After loop is every sentence (document) transformer to numeric vector.

        Args:
            X (typing.List[typing.List[str]]): List of lists where are situated sentences.

        Returns:
            list[float[]]: Array of mean which represents documents.
        """
        self.setup()

        self.missed = 0
        self.counter = 0
        print(f"Transforming {len(X)}, {self.missed} {self.counter}")

        corpus = []

        for sentence in X:
            tokens = sentence.split(" ")
            sentence_embedding = []
            for token in tokens:
                embedding_of_token = self.get_from_vectors(self.vectors, token)
                sentence_embedding.append(embedding_of_token)
            corpus.append(np.array(sentence_embedding))

        return self.get_mean(corpus)
