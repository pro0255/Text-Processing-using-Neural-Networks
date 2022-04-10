import gensim.downloader as api
from src.models.embedding.load_model import load_model

def load_from_gensim(model_name):
    print(f"Loading model={model_name}")
    #loaded_model_path = api.load(model_name, return_path=True)
    embedding_dictionary = api.load(model_name)

    return embedding_dictionary



