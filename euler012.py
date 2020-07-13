from operator import mul
from functools import reduce


def triangular_numbers():
    total = 0
    number = 0
    while True:
        number += 1
        total += number
        yield total


def factorize(n):
    factors = []
    p = 2
    while n >= p * p:
        if n % p == 0:
            factors.append(p)
            n = n // p
        else:
            p += 1
    factors.append(n)
    return factors


def count_of_divisors(n):
    if n == 1:
        return 1
    f = factorize(n)
    d = {factor: f.count(factor) for factor in f}
    return reduce(mul, [x + 1 for x in d.values()])


for t in triangular_numbers():
    if count_of_divisors(t) > 500:
        print(t)
        break
