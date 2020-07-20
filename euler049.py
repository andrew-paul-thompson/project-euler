def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


primes = [i for i in range(1000, 10000) if is_prime(i)]
for p1 in primes:
    for p2 in [p for p in primes if p > p1 and is_prime(p1 + 2 * (p - p1))]:
        p3 = p1 + 2 * (p2 - p1)
        if p1 != 1487 and p3 < 10000 and set(str(p1)) == set(str(p2)) == set(str(p3)):
            print(f'{p1}{p2}{p3}')
