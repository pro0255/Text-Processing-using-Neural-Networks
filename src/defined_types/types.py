
# PreprocessingFunc = typing.Union[None, Callable[[str], str]]

import typing
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.neighbors import KNeighborsClassifier
from src.vectorizers.classic.bow_vectorizer import BoWVectorizer
from src.vectorizers.classic.tfidf_vectorizer import TFIDFVectorizer

from src.vectorizers.embedding.glove_vectorizer import GloveVectorizer
from src.vectorizers.embedding.word2vec_vectorizer import Word2VecVectorizer
from src.vectorizers.transformer.bert_base_vectorizer import BertBaseUncasedVectorizer
from src.vectorizers.transformer.distil_bert_base_vectorizer import DistilBertBaseUncasedVectorizer
from src.vectorizers.transformer.electra_small_vectorizer import ElectraSmallVectorizer


PredictionClassesType = typing.Union[str, typing.Type[KNeighborsClassifier], typing.Type[SGDClassifier], typing.Type[GaussianNB], typing.Type[RandomForestClassifier]]


VectorizerClassesType =  typing.Union[str, typing.Type[BoWVectorizer], typing.Type[TFIDFVectorizer], typing.Type[GloveVectorizer], typing.Type[Word2VecVectorizer], typing.Type[BertBaseUncasedVectorizer],typing.Type[DistilBertBaseUncasedVectorizer],typing.Type[ElectraSmallVectorizer]]


#IndexTransformerPoolingFunc = typing.Callable[[int], int]