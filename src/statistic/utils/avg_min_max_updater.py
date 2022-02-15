from src.statistic.types.avg_max_min import Stat
from src.statistic.utils.moving_avg_calculator import MovingAverageCalculator

class AvgMaxMinUpdate:
    def __init__(self) -> None:
        self.moving_avg_calc = MovingAverageCalculator()

    def update(self, current_dic, value):
        updated_dic = current_dic.copy()

        current_min = current_dic[Stat.Min.value]
        current_max = current_dic[Stat.Max.value]

        if value < current_min:
            updated_dic[Stat.Min.value] = value

        if value > current_max:
            updated_dic[Stat.Max.value] = value

        self.moving_avg_calc.update(value)

        updated_dic[Stat.Avg.value] = self.moving_avg_calc.mean 
        
        return updated_dic