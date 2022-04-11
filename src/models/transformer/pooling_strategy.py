from enum import Enum

from src.types.transformer_pooling import TransformerPooling
from src.types.transformer_pooling_strategy import TransformerPoolingStrategy


class TransformerPoolingStrategySelection(Enum):
    SumAllLayersCLS = "SumAllLayersCLS"
    SumLast4LayersCLS = "SumLast4LayersCLS"
    ConcatLast4LayersCLS = "ConcatLast4LayersCLS"
    LastLayerCLS = "LastLayerCLS"
    FirstLayerCLS = "FirstLayerCLS"
    SumLast2LayersCLS = "SumLast2LayersCLS"
    ConcatLast2LayersCLS = "ConcatLast2LayersCLS"
    SumAllLayersAverage = "SumAllLayersAverage"
    SumLast4LayersAverage = "SumLast4LayersAverage"
    ConcatLast4LayersAverage = "ConcatLast4LayersAverage"
    LastLayerAverage = "LastLayerAverage"
    FirstLayerAverage = "FirstLayerAverage"
    SumLast2LayersAverage = "SumLast2LayersAverage"
    ConcatLast2LayersAverage = "ConcatLast2LayersAverage"
    Pooler = "Pooler"
    LastHidden = "LastHidden"


MAX_FAKE_LAYERS = 12

pooling_strategy_dictionary = {
    TransformerPoolingStrategySelection.SumAllLayersCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.CLS,
        lambda number_of_layers: number_of_layers - 1,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.SumLast4LayersCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.CLS,
        lambda number_of_layers: 3,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.ConcatLast4LayersCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.ConcatCLS,
        lambda number_of_layers: 3,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.LastLayerCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.CLS,
        lambda number_of_layers: 0,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.FirstLayerCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.CLS,
        lambda number_of_layers: number_of_layers - 1,
        lambda number_of_layers: number_of_layers - 1,
    ),
    TransformerPoolingStrategySelection.SumLast2LayersCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.CLS,
        lambda number_of_layers: 1,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.ConcatLast2LayersCLS: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.ConcatCLS,
        lambda number_of_layers: 1,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.SumAllLayersAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.Average,
        lambda number_of_layers: number_of_layers - 1,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.SumLast4LayersAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.Average,
        lambda number_of_layers: 3,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.ConcatLast4LayersAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.ConcatAverage,
        lambda number_of_layers: 3,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.LastLayerAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.Average,
        lambda number_of_layers: 0,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.FirstLayerAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.Average,
        lambda number_of_layers: number_of_layers - 1,
        lambda number_of_layers: number_of_layers - 1,
    ),
    TransformerPoolingStrategySelection.SumLast2LayersAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.Average,
        lambda number_of_layers: 1,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.ConcatLast2LayersAverage: (
        TransformerPooling.HiddenStates,
        TransformerPoolingStrategy.ConcatAverage,
        lambda number_of_layers: 1,
        lambda number_of_layers: 0,
    ),
    TransformerPoolingStrategySelection.Pooler: (
        TransformerPooling.Pooler,
        None,
        lambda number_of_layers: -1,
        lambda number_of_layers: -1,
    ),
    TransformerPoolingStrategySelection.LastHidden: (
        TransformerPooling.LastHiddenState,
        None,
        lambda number_of_layers: -1,
        lambda number_of_layers: -1,
    ),
}
