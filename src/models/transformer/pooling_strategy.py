
from enum import Enum
from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy

class TransformerPoolingStrategySelection(Enum):
    SumAll12LayersCLS = "SumAll12LayersCLS"
    SumLast4LayersCLS = "SumLast4LayersCLS"
    ConcatLast4LayersCLS = "ConcatLast4LayersCLS"
    LastLayerCLS = "LastLayerCLS"
    FirstLayerCLS = "FirstLayerCLS"
    SumLast2LayersCLS = "SumLast2LayersCLS"
    ConcatLast2LayersCLS = "ConcatLast2LayersCLS"
    SumAll12LayersAverage = "SumAll12LayersAverage"
    SumLast4LayersAverage = "SumLast4LayersAverage"
    ConcatLast4LayersAverage = "ConcatLast4LayersAverage"
    LastLayerAverage = "LastLayerAverage"
    FirstLayerAverage = "FirstLayerAverage"
    SumLast2LayersAverage = "SumLast2LayersAverage"
    ConcatLast2LayersAverage = "ConcatLast2LayersAverage"




pooling_strategy_dictionary = {
    TransformerPoolingStrategySelection.SumAll12LayersCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.CLS, 12, 0),
    TransformerPoolingStrategySelection.SumLast4LayersCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.CLS, 3, 0),
    TransformerPoolingStrategySelection.ConcatLast4LayersCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.ConcatCLS, 3, 0),
    TransformerPoolingStrategySelection.LastLayerCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.CLS, 0, 0),
    TransformerPoolingStrategySelection.FirstLayerCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.CLS, 12, 12),
    TransformerPoolingStrategySelection.SumLast2LayersCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.CLS, 1, 0),
    TransformerPoolingStrategySelection.ConcatLast2LayersCLS: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.ConcatCLS, 1, 0),

    TransformerPoolingStrategySelection.SumAll12LayersAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.Average, 12, 0),
    TransformerPoolingStrategySelection.SumLast4LayersAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.Average, 3, 0),
    TransformerPoolingStrategySelection.ConcatLast4LayersAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.ConcatAverage, 3, 0),
    TransformerPoolingStrategySelection.LastLayerAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.Average, 0, 0),
    TransformerPoolingStrategySelection.FirstLayerAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.Average, 12, 12),
    TransformerPoolingStrategySelection.SumLast2LayersAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.Average, 1, 0),
    TransformerPoolingStrategySelection.ConcatLast2LayersAverage: (TransformerPooling.HiddenStates, TransformerPoolingStrategy.ConcatAverage, 1, 0),
}
