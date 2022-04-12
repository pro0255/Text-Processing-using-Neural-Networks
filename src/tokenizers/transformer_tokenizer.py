import typing
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from transformers import AutoTokenizer

from src.types.transformer_input import TransformerInput


class TransformerTokenizer:
    def __init__(
        self, name: str, encoder: typing.Union[LabelEncoder, None]=None, max_len: typing.Union[None, int]=None, preprocess_pipeline: typing.Union[None, typing.Callable[[str], str]]=None
    ) -> None:
        self.name = name
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.preprocess_pipeline = preprocess_pipeline
        self.max_len = max_len
        self.encoder = encoder
        print(f"Tokenizer with max len = {str(self.max_len)}")

    def tokenize(self, text, label):
        text = bytes.decode(text.numpy())
        label = label.numpy()

        if self.preprocess_pipeline is not None:
            text = self.preprocess_pipeline(text)

        tokenized = self.tokenizer(
            text,
            return_tensors="tf",
            max_length=self.max_len,
            add_special_tokens=True,
            return_attention_mask=True,
            return_token_type_ids=False,
            padding="max_length",
            truncation=True,
        )

        label = (
            self.encoder.transform([label])[0] if self.encoder is not None else label
        )
        return (
            tokenized[TransformerInput.input.value][0],
            tokenized[TransformerInput.mask.value][0],
            label,
        )

    def ty_py_func(self, text, label):
        return tf.py_function(
            self.tokenize, [text, label], [tf.int32, tf.int32, tf.int32]
        )

    def to_model_input(self, input_ids, attention_mask, label):
        return {"input_ids": input_ids, "attention_mask": attention_mask}, label
