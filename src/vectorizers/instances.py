from src.vectorizers.classic.bow_vectorizer import BoWVectorizer
from src.vectorizers.classic.tfidf_vectorizer import TFIDFVectorizer
from src.vectorizers.embedding.glove_vectorizer import GloveVectorizer
from src.vectorizers.embedding.word2vec_vectorizer import Word2VecVectorizer
from src.vectorizers.transformer.bert_base_vectorizer import BertBaseUncasedVectorizer
from src.vectorizers.transformer.distil_bert_base_vectorizer import (
    DistilBertBaseUncasedVectorizer,
)
from src.vectorizers.transformer.electra_small_vectorizer import ElectraSmallVectorizer

CLASSIC = [type(BoWVectorizer()).__name__, type(TFIDFVectorizer()).__name__]
EMBEDDING = [type(GloveVectorizer()).__name__, type(Word2VecVectorizer()).__name__]
TRANSFORMER = [
    type(ElectraSmallVectorizer()).__name__,
    type(BertBaseUncasedVectorizer()).__name__,
    type(DistilBertBaseUncasedVectorizer()).__name__,
]
