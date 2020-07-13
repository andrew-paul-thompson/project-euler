from math import gcd
from functools import reduce


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


print(lcm(range(1, 21)))
