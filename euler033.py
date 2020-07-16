from functools import reduce
from math import gcd


def find_digit_cancelling_fractions():
    fractions = []
    for numer in range(10, 100):
        for denom in range(10, 100):
            if numer == denom or numer // denom > 1:
                continue
            numer_digits = [int(digit) for digit in str(numer)]
            denom_digits = [int(digit) for digit in str(denom)]
            for i in range(2):
                if numer_digits[i] in denom_digits and numer_digits[i] != 0:
                    try:
                        reduced_value = numer_digits[i - 1] / denom_digits[denom_digits.index(numer_digits[i]) - 1]
                        if reduced_value == numer / denom:
                            fractions.append((numer, denom))
                    except ZeroDivisionError:
                        pass
    return fractions


def fraction_product(fraction):
    return reduce(lambda x, y: (x[0] * y[0], x[1] * y[1]), fraction)


def reduce_fraction(fraction):
    g = gcd(fraction[0], fraction[1])
    return fraction[0] // g, fraction[1] // g


digit_cancelling_fractions = find_digit_cancelling_fractions()
reduced_product = reduce_fraction(fraction_product(digit_cancelling_fractions))
print(reduced_product[1])
