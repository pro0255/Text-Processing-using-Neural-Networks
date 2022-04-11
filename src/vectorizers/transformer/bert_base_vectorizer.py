from src.types.transformer_name import TransformerName
from src.vectorizers.transformer.transformer_vectorizer import TransformerVectorizer
from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy


class BertBaseUncasedVectorizer(TransformerVectorizer):
    def __init__(
        self,
        transformer_pooling_type=TransformerPooling.Pooler,
        path_authors=None,
        encoder=None,
        max_len=None,
        preprocess_pipeline=None,
        transformer_pooling_strategy=TransformerPoolingStrategy.Blank,
        transformer_start_index=-1,
        transformer_end_index=-1,
    ):
        super().__init__(
            TransformerName.BertBaseUncased,
            transformer_pooling_type,
            path_authors=path_authors,
            encoder=encoder,
            max_len=max_len,
            preprocess_pipeline=preprocess_pipeline,
            transformer_pooling_strategy=transformer_pooling_strategy,
            transformer_start_index=transformer_start_index,
            transformer_end_index=transformer_end_index,
        )

    def verify(
        self,
        transformer_pooling,
        transformer_pooling_strategy,
        transformer_start_index,
        transformer_end_index,
    ):
        return True
