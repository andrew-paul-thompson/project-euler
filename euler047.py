def unique_factorize(n):
    factors = set()
    p = 2
    while n >= p * p:
        if n % p == 0:
            factors.add(p)
            n = n // p
        else:
            p += 1
    factors.add(n)
    return factors


def distinct_prime_factors():
    n = 4
    distinct_prime_factor = {1: len(unique_factorize(1)), 2: len(unique_factorize(2)), 3: len(unique_factorize(3)),
                             4: len(unique_factorize(4))}
    while True:
        n += 1
        distinct_prime_factor[n] = len(unique_factorize(n))
        if [distinct_prime_factor[n] for n in range(n - 3, n + 1)] == [4, 4, 4, 4]:
            return n - 3


print(distinct_prime_factors())
