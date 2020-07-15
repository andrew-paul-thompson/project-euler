def f(n, a, b):
    return n ** 2 + a * n + b


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def count_primes_produced(a, b):
    n = 0
    while is_prime(f(n, a, b)):
        n += 1
    return n


def run_test():
    best_result = (0, 0, 0)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes_produced = count_primes_produced(a, b)
            if primes_produced > best_result[2]:
                best_result = (a, b, primes_produced)
    return best_result


result = run_test()
print(result[0] * result[1])
