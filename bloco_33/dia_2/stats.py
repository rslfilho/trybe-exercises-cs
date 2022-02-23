from statistics import mean, median, mode


class Stats:
    @classmethod
    def average(numbers):
        return mean(numbers)

    @classmethod
    def median(numbers):
        return median(numbers)

    @classmethod
    def mode(numbers):
        return mode(numbers)
