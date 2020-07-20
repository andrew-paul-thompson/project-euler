def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def sieve(n=120000):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]


def get_consecutive_prime_sum():
    max_item = (0, 0)
    for length in range(1, 10000):
        for offset in range(0, len(primes) - length):
            total = sum(primes[offset:offset + length])
            if total >= 1000000:
                break
            if length > max_item[1] and is_prime(total):
                max_item = (total, length)
    return max_item[0]


primes = sieve(1000000)
print(get_consecutive_prime_sum())
