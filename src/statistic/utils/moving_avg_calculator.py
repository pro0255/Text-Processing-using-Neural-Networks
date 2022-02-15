
#https://nestedsoftware.com/2018/03/20/calculating-a-moving-average-on-streaming-data-5a7k.22879.html thanks <3

class MovingAverageCalculator:
    def __init__(self) -> None:
        self.count = 0
        self.mean = 0
    
    def update(self, value):
        self.count += 1

        diff = (value - self.mean) / self.count

        new_mean = self.mean + diff

        self.mean = new_mean
