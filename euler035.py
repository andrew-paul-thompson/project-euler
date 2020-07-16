def digit_rotations(n):
    s = str(n)
    return {int(s[i:] + s[:i]) for i in range(len(s))}


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def circular_primes():
    primes = set()
    primes.add(2)
    for n in range(3, 1000000):
        s = str(n)
        if n not in primes and all([c not in s for c in '24680']) and is_prime(n):
            rotations = digit_rotations(n)
            if all([is_prime(i) for i in rotations]):
                primes.update(rotations)
    return primes


print(len(circular_primes()))
