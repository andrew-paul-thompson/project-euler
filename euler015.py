from math import factorial


def number_of_paths(N, M):
    return factorial(N + M) // (factorial(N) * factorial(M))


N, M = 20, 20
print(number_of_paths(N, M))
