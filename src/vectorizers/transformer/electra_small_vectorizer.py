from src.types.transformer_name import TransformerName
from src.vectorizers.transformer.transformer_vectorizer import TransformerVectorizer

class ElectraSmallVectorizer(TransformerVectorizer):
    def __init__(
        self, 
        transformer_pooling_type,
        path_authors=None,
        encoder=None, 
        max_len=512, 
        preprocess_pipeline=None,
    ):
        super().__init__(
            TransformerName.ElectraSmall,         
            transformer_pooling_type,
            path_authors=path_authors,
            encoder=encoder, 
            max_len=max_len, 
            preprocess_pipeline=preprocess_pipeline
        )