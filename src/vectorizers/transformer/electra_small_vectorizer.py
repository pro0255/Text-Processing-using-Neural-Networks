import typing

from sklearn.preprocessing import LabelEncoder

from src.types.transformer_name import TransformerName
from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy
from src.vectorizers.transformer.transformer_vectorizer import \
    TransformerVectorizer


class ElectraSmallVectorizer(TransformerVectorizer):
    def __init__(
        self,
        transformer_pooling_type: TransformerPooling = TransformerPooling.LastHiddenState,
        path_authors: typing.Union[None, str] = None,
        encoder: typing.Union[None, typing.Type[LabelEncoder]] = None,
        max_len: typing.Union[None, int] = None,
        preprocess_pipeline=typing.Union[None, typing.Callable[[str], str]],
        transformer_pooling_strategy: TransformerPoolingStrategy = TransformerPoolingStrategy.Blank,
        transformer_start_index: typing.Union[int, typing.Callable[[int], int]] = -1,
        transformer_end_index: typing.Union[int, typing.Callable[[int], int]] = -1,
    ):
        if transformer_pooling_type == TransformerPooling.Pooler:
            assert Exception(
                f"Cannot use electra with pooling={transformer_pooling_type.value}!"
            )
        super().__init__(
            TransformerName.ElectraBase,
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
