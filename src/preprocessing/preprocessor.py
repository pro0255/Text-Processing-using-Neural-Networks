import nltk
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import \
    remove_stopwords as remove_stopwords_gensim
from gensim.parsing.preprocessing import stem_text as stem_text_gensim
from gensim.parsing.preprocessing import \
    strip_multiple_whitespaces as strip_multiple_whitespaces_gensim
from gensim.parsing.preprocessing import strip_numeric as strip_numeric_gensim
from gensim.parsing.preprocessing import \
    strip_punctuation as strip_punctuation_gensim
from gensim.parsing.preprocessing import strip_short as strip_short_gensim
from gensim.parsing.preprocessing import strip_tags as strip_tags_gensim
from nltk.stem import WordNetLemmatizer

BLACKLIST = ["CHAPTER"]


class TextPreprocessor:
    def __init__(self) -> None:
        self.strip_short_default = self.create_strip_short_method(3)
        self.lemma_text = self.create_lemma_text()

    def strip_tags(self, text):
        return strip_tags_gensim(text)

    def strip_upper_words(self, text):
        return [word for word in text.split(" ") if word.upper() != word]

    def remove_when_blacklisted(self, text):
        current_text = set(text.split(" "))
        blacklist = set(BLACKLIST)

        l = len(current_text.intersection(blacklist))

        if l > 0:
            return ""

        return text

    def strip_punctuation(self, text):
        return strip_punctuation_gensim(text)

    def strip_multiple_whitespaces(self, text):
        return strip_multiple_whitespaces_gensim(text)

    def strip_numeric(self, text):
        return strip_numeric_gensim(text)

    def strip_stopwords(self, text):
        return remove_stopwords_gensim(text)

    def strip_short(self, text, minsize=3):
        return strip_short_gensim(text, minsize)

    def strip_short(self, text):
        return strip_short_gensim(text)

    def create_strip_short_method(self, minsize=3):
        # TODO: fix
        print(f"Creating shorting method with min = {minsize}")

        def strip_short(text, minsize=minsize):
            return strip_short_gensim(text, minsize)

        return strip_short

    def stem_text(self, text):
        return stem_text_gensim(text)

    def to_lowercase(self, text):
        return text.lower()

    def create_lemma_text(self):
        instance = WordNetLemmatizer()
        print(f"Creating lemma method with instance {instance}")

        def lemma_text(text):
            word_list = nltk.word_tokenize(text)
            return " ".join([instance.lemmatize(word) for word in word_list])

        return lemma_text

    def create_preprocess_string_func(self, filters, tokenized=False):
        def preprocess_func(text):
            result = preprocess_string(text, filters)
            return result if tokenized else " ".join(result)

        return preprocess_func

    def default_preprocessing(self):
        return self.create_preprocess_string_func(
            [
                self.remove_when_blacklisted,
                self.to_lowercase,
                self.strip_punctuation,
                self.strip_tags,
                self.strip_multiple_whitespaces,
                self.strip_numeric,
                self.strip_stopwords,
                self.strip_short,
                self.lemma_text,
            ]
        )

    def default_lowerinterpunction(self):
        return self.create_preprocess_string_func(
            [
                self.remove_when_blacklisted,
                self.to_lowercase,
                self.strip_punctuation,
                self.strip_multiple_whitespaces,
                self.strip_numeric,
            ]
        )
