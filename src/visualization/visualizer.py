import itertools

import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud

from src.config.config import LABEL_COLUMN, TEXT_COLUMN


class Visualizer:
    def __init__(self):
        pass

    def create_max_min_mean_len(self, tuples):
        res = pd.DataFrame()

        for name, data in tuples:
            x = data.copy()
            x["len"] = x[TEXT_COLUMN].apply(len)
            x = x.groupby(LABEL_COLUMN).len.agg(["mean", "min", "max"])

            together = pd.DataFrame.from_dict(
                {
                    "together": {
                        "mean": np.mean(x["mean"]),
                        "min": np.min(x["min"]),
                        "max": np.max(x["max"]),
                    }
                },
                orient="index",
            )

            x = pd.concat([together, x])
            x = x.reset_index()
            x = pd.melt(x, id_vars=["index"], var_name="value_type", value_name="value")
            x["df_type"] = name

            res = pd.concat([res, x])

        return res

    def show_mean(self, dataframe):
        return self.show_type(dataframe, "mean")

    def show_max(self, dataframe):
        return self.show_type(dataframe, "max")

    def show_min(self, dataframe):
        return self.show_type(dataframe, "min")

    def show_type(self, dataframe, spe_type):
        return px.bar(
            dataframe[dataframe.value_type == spe_type],
            x="df_type",
            y="value",
            color="index",
            barmode="group",
        )

    def seq_dist(self, dataframe):
        x = dataframe.copy()
        x["len"] = x[TEXT_COLUMN].apply(len)
        return px.histogram(x, x="len", color="label", title="")

    def create_all_words(self, dataframe):
        x = dataframe.copy()
        all_words = list(
            itertools.chain.from_iterable(
                [sentence.split(" ") for sentence in x[TEXT_COLUMN]]
            )
        )
        dist = nltk.FreqDist(all_words)
        return dist

    def generate_top_words(self, dataframe):
        x = dataframe.copy()
        res = {}

        for current_label in np.unique(x.label.values):
            subframe = x[x.label == current_label]
            res[current_label] = self.show_top_words(subframe)

        res["all"] = self.show_top_words(x)

        return res

    def show_top_words(self, dataframe, n=10):
        dist = self.create_all_words(dataframe)
        df = pd.DataFrame.from_dict(dict(dist), orient="index").reset_index()
        df.columns = ["word", "freq"]
        df = df.sort_values(by="freq", ascending=False)
        first_n = df.iloc[0:n, :]
        return px.bar(
            first_n, x="word", y="freq", color="word", title=f"{n} most freq words"
        )

    def show_wordcloud(self, wordcloud):
        plt.figure(figsize=[10, 10])
        plt.axis("off")
        x = plt.imshow(wordcloud, interpolation="bilinear")
        return x

    def generate_wordclouds(self, dataframe):
        # result = vis.generate_wordclouds(test) test
        x = dataframe.copy()
        res = {}

        for current_label in np.unique(x.label.values):
            subframe = x[x.label == current_label]
            res[current_label] = self.wordcloud(subframe)

        res["all"] = self.wordcloud(x)

        return res

    def wordcloud(self, dataframe, max_words=100):
        x = dataframe.copy()
        current_text = " ".join(x.text.values)
        wordcloud = WordCloud(
            max_font_size=50, max_words=100, background_color="white"
        ).generate(current_text)
        return wordcloud
