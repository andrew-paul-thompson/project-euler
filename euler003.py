def factorize(n):
    factors = []
    if n == 1:
        return [1]
    i = 2
    while n >= i*i:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    factors.append(n)
    return factors


print(max(factorize(600851475143)))
