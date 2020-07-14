from itertools import combinations_with_replacement


def proper_divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]


def sum_of_proper_divisors(n):
    return sum(proper_divisors(n))


def is_abundant_number(n):
    return sum_of_proper_divisors(n) > n


abundant_numbers = [i for i in range(28124) if is_abundant_number(i)]
numbers_that_are_the_sum_of_two_abundant_numbers = set(
    [sum(c) for c in combinations_with_replacement(abundant_numbers, 2)])
answer = sum([item for item in range(1, 28124) if item not in numbers_that_are_the_sum_of_two_abundant_numbers])
print(answer)
