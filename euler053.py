import math


def n_choose_r(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def main():
    print(sum([1 for n in range(1, 101) for r in range(0, n + 1) if n_choose_r(n, r) > 1000000]))


if __name__ == '__main__':
    main()
