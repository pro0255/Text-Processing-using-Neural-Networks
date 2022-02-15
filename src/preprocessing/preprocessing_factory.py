
from src.preprocessing.preprocessor import TextPreprocessor
from src.types.processing_type import PreprocessingType

class PreprocessingFactory:
    def __init__(self) -> None:
        self.preprocessor = TextPreprocessor()
        self.build_dic()

    def build_dic(self):
        self.dic = {
            PreprocessingType.Default: self.preprocessor.default_preprocessing(),
            PreprocessingType.Lowercase: self.preprocessor.create_preprocess_string_func(
                [
                    self.preprocessor.to_lowercase
                ]
            ),
            PreprocessingType.Blank: None,
        }

    def create(self, preprocessing_type):
        return self.dic[preprocessing_type]


