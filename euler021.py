def proper_divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]


def sum_of_proper_divisors(n):
    return sum(proper_divisors(n))


def is_amicable(a):
    return sum_of_proper_divisors(sum_of_proper_divisors(a)) == a and sum_of_proper_divisors(a) != a


amicable_numbers = [a for a in range(1, 10000) if is_amicable(a)]
print(sum(amicable_numbers))
