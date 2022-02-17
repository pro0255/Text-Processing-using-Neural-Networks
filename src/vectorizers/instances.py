from src.vectorizers.classic.bow_vectorizer import BoWVectorizer
from src.vectorizers.classic.tfidf_vectorizer import TFIDFVectorizer
from src.vectorizers.embedding.glove_vectorizer import GloveVectorizer
from src.vectorizers.embedding.word2vec_vectorizer import Word2VecVectorizer
from src.vectorizers.transformer.electra_small_vectorizer import ElectraSmallVectorizer
from src.vectorizers.transformer.bert_base_vectorizer import BertBaseUncasedVectorizer
from src.vectorizers.transformer.distil_bert_base_vectorizer import DistilBertBaseUncasedVectorizer

CLASSIC = [BoWVectorizer(), TFIDFVectorizer()]
EMBEDDING = [GloveVectorizer(), Word2VecVectorizer()]
TRANSFORMER = [ElectraSmallVectorizer(), BertBaseUncasedVectorizer(), DistilBertBaseUncasedVectorizer()]