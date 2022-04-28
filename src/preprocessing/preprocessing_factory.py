import typing

from src.preprocessing.preprocessor import TextPreprocessor
from src.types.processing_type import PreprocessingType


class PreprocessingFactory:
    """Class which helps with preprocessing. According to defined types are inputs transformed (preprocessed)."""

    def __init__(self) -> None:
        self.preprocessor: typing.Type[TextPreprocessor] = TextPreprocessor()
        self.build_dic()

    def build_dic(self):
        self.dic: typing.Dict[
            PreprocessingType, typing.Union[None, typing.Callable[[str], str]]
        ] = {
            PreprocessingType.Default: self.preprocessor.default_preprocessing(),
            PreprocessingType.Lowercase: self.preprocessor.create_preprocess_string_func(
                [self.preprocessor.to_lowercase]
            ),
            PreprocessingType.Raw: lambda x: x,
            PreprocessingType.CaseInterpunction: self.preprocessor.default_lowerinterpunction(),
            PreprocessingType.Blank: None,
        }

    def create(self, preprocessing_type: PreprocessingType):
        return self.dic[preprocessing_type]
