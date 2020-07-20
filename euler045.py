import cmath
import numpy as np


def triangular_number(n):
    return n * (n + 1) // 2


def pentagonal_number(n):
    return n * (3 * n - 1) // 2


def hexagonal_number(n):
    return n * (2 * n - 1)


def has_positive_integer_root(a, b, c):
    polynomial = np.poly1d([a, b, c])
    for root in polynomial.r:
        if root > 0 and abs(round(root) - root) < 0.000001:
            return True
    return False


# Find whether there is an integer solution to show that Pn is a pentagonal number.
# 0 = (1.5)*(n^2) + (-0.5)*n + (-Pn)
def is_pentagonal_number(pn):
    return has_positive_integer_root(1.5, -0.5, -1 * pn)


# Find whether there is an integer solution to show that Tn is a triangular number.
# 0 = (0.5)*(n^2) + (0.5)*n + (-Tn)
def is_triangular_number(tn):
    return has_positive_integer_root(0.5, 0.5, -1 * tn)


# Find whether there is an integer solution to show that Hn is a hexagonal number.
# 0 = (2)*(n^2) + (-1)*n + (-Hn)
def is_hexagonal_number(hn):
    return has_positive_integer_root(2, -1, -1 * hn)


def pentagonal_numbers():
    n = 0
    while True:
        n += 1
        yield pentagonal_number(n)


def triangular_numbers():
    n = 0
    while True:
        n += 1
        yield triangular_number(n)


def hexagonal_numbers():
    n = 0
    while True:
        n += 1
        yield hexagonal_number(n)


def find_triangular_pentagonal_hexagonal_number():
    for t in triangular_numbers():
        if t > 40755 and is_pentagonal_number(t) and is_hexagonal_number(t):
            return t


print(find_triangular_pentagonal_hexagonal_number())
