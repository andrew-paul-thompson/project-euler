import itertools


def is_pandigital(n):
    return ''.join(sorted(str(n))) == ''.join([str(i) for i in range(1, len(str(n)) + 1)])


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def pandigital_primes():
    primes = set()
    for n in range(1, 10):
        for perm in itertools.permutations(''.join([str(i) for i in range(1, n + 1)])):
            num = int(''.join(perm))
            if is_prime(num):
                primes.add(num)
    return primes


print(max(pandigital_primes()))
