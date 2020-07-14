from math import factorial


def number_of_paths(n, m):
    return factorial(n + m) // (factorial(n) * factorial(m))


N, M = 20, 20
print(number_of_paths(N, M))
