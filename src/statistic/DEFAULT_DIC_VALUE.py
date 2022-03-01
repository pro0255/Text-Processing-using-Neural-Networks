from src.statistic.types.avg_max_min import Stat


DEFAULT_DIC_VALUE = {
    Stat.Avg.value: 0,
    Stat.Min.value: float("inf"),
    Stat.Max.value: float("-inf"),
}
