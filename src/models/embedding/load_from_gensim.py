import typing

import gensim.downloader as api

from src.config.loaded_models import loaded_models
from src.models.embedding.load_model import load_model


def load_from_gensim(model_name: str) -> typing.Dict:
    if model_name in loaded_models:
        print(f"Already loaded model={model_name}")
        embedding_dictionary = loaded_models[model_name]
    # loaded_model_path = api.load(model_name, return_path=True)
    else:
        print(f"Loading model={model_name}")
        embedding_dictionary = api.load(model_name)

    return embedding_dictionary
