def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def truncated_digits(n):
    numbers = set()
    numbers.add(n)

    s = str(n)
    for i in range(1, len(s)):
        numbers.add(int(s[i:]))
        numbers.add(int(s[:i]))
    return numbers


def has_even_digit(n):
    return any([c in str(n) for c in '24680'])


def is_truncatable_prime(n):
    if n // 10 != 2 and has_even_digit(n):
        return False
    else:
        return is_prime(n) and all([is_prime(i) for i in truncated_digits(n)])


def truncatable_primes():
    return [p for p in range(11, 1000000, 2) if is_truncatable_prime(p)]


print(sum(truncatable_primes()))
