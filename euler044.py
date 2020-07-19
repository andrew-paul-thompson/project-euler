import itertools
import cmath


def pentagonal_number(n):
    return n * (3 * n - 1) // 2


# Find whether there is an integer solution to show that Pn is a pentagonal number.
# 0 = (1.5)*(n^2) + (-0.5)*n + (-Pn)
def is_pentagonal_number(pn):
    d = (-0.5) ** 2 - 6 * (-1 * pn)

    solutions = [(0.5 - cmath.sqrt(d)) / 3, (0.5 + cmath.sqrt(d)) / 3]
    for solution in solutions:
        if solution.imag == 0 and solution.real == int(solution.real) and solution.real > 0:
            return True
    return False


def pentagonal_numbers():
    n = 0
    while True:
        n += 1
        yield pentagonal_number(n)


def find_maximum_pentagonal_number():
    scores = {}
    for j in range(1, 2500):
        for k in range(j, 2500):
            pj = pentagonal_number(j)
            pk = pentagonal_number(k)
            if is_pentagonal_number(abs(pk - pj)) and is_pentagonal_number(pj + pk):
                scores[(j, k)] = abs(pk - pj)
    return scores[max(scores)]


print(find_maximum_pentagonal_number())
