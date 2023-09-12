import random
from functools import partial

def number_of_natural_dividers(num: int) -> int:
    """
    count the number of the natural dividers
    example:
    1. input - 1, output = 1 (len([1] = 1)
    2. input - 5, output = 2 (len([1, 5] = 2)
    3. input - 6, output = 4  (len([1, 2, 3, 6] = 4)
    4. input - 10, output = 4 (len([1, 2, 5, 10] = 4)
    5. input - 20, output = 6 (len([1, 2, 4, 5, 10, 20] = 6)
    """

    check_if_a_devide_by_b_without_remnant = lambda a, b: a % b == 0

    dividers = filter(partial(check_if_a_devide_by_b_without_remnant, num), range(1, num + 1))
    return len(list(dividers))


result = {i: number_of_natural_dividers(i) for i in range(20)}
for i, v in result.items():
    if v >= 4:
        print(i, v)

list(map(print, filter(lambda x: str(x) == str(x)[::-1], map(lambda y: y[0] * y[1], filter(lambda c: c[1] > 2, {a: len(str(a)) for a in filter(lambda q: str(q) == str(q)[::-1], range(10000))}.items())))))

palindromes = filter(lambda q: str(q) == str(q)[::-1], range(10000))

lengths = {a: len(str(a)) for a in palindromes}

filtered_lengths = filter(lambda c: c[1] > 2, lengths.items())

products = map(lambda y: y[0] * y[1], filtered_lengths)

filtered_products = filter(lambda x: str(x) == str(x)[::-1], products)

list(map(print, filtered_products))
