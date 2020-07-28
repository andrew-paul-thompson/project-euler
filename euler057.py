from fractions import Fraction
import itertools


def square_root_sequence():
    n = 1
    yield Fraction(3, 2)
    while True:
        n += 1
        f = Fraction(5, 2)
        for _ in range(n - 2):
            f = 2 + 1 / f
        yield 1 + 1 / f


def main():
    first_1000_iterations = itertools.islice(square_root_sequence(), 1000)
    print(sum(1 for i in first_1000_iterations if len(str(i.numerator)) > len(str(i.denominator))))


if __name__ == '__main__':
    main()
