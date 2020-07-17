from functools import reduce
from operator import mul


def champernowne_constant_digits():
    i = 0
    while True:
        i += 1
        for c in str(i):
            yield int(c)


def get_expression_value():
    powers = [10 ** n for n in range(7)]
    digits = []
    for i, digit in enumerate(champernowne_constant_digits()):
        if i + 1 in powers:
            digits.append(digit)
        if i == 10 ** 6:
            break
    return reduce(mul, digits)


print(get_expression_value())
