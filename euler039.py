import math


# Adapted from Euclid's formula for producing Pythagorean triplets
# Returns dictionary of pythagorean triplets, indexed by sum of a+b+c, with a+b+c <= p
def pythagorean_triplets(p):
    triplets = {}
    for m in range(1, 100):
        for n in range(1, m):
            if not (m % 2 == 1 and n % 2 == 1) and math.gcd(m, n) == 1:
                for k in range(1, 100):
                    a = k * (m ** 2 - n ** 2)
                    b = k * (2 * m * n)
                    c = k * (m ** 2 + n ** 2)
                    if a + b + c <= p:
                        if a + b + c not in triplets:
                            triplets[a + b + c] = set()
                        triplets[a + b + c].add(tuple(sorted([a, b, c])))
    return triplets


triplets = pythagorean_triplets(1000)
print(max(triplets, key=lambda x: len(triplets[x])))
