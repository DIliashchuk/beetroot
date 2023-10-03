class Mathematician:
    @staticmethod
    def square_nums(numbers):
        return [x ** 2 for x in numbers]

    @staticmethod
    def remove_positives(numbers):
        return [x for x in numbers if x <= 0]

    @staticmethod
    def filter_leaps(years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]


m = Mathematician()


assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
