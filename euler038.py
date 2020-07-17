def concatenated_product(n, multipliers):
    return int(''.join([str(n * multiplier) for multiplier in multipliers]))


def is_pandigital(n):
    return set(int(d) for d in str(n)) == set(range(1, len(str(n)) + 1))


def pandigital_multiples():
    arr = []
    for i in range(1, 10000):
        for n in range(2, 10):
            prod = concatenated_product(i, (x for x in range(1, n + 1)))
            if len(str(prod)) == 9 and is_pandigital(prod):
                arr.append(prod)
    return arr


print(max(pandigital_multiples()))
