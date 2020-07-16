import itertools


def is_pandigital(n):
    return set(int(d) for d in str(n)) == set(range(1, len(str(n)) + 1))


# Brute force approach
def sum_of_pandigital_products_brute():
    products = set()
    multiplier_set = [number for number in range(10000) if len(set(str(number))) == len(str(number))]
    for a in multiplier_set:
        for b in multiplier_set:
            product = a * b
            identity = str(a) + str(b) + str(product)
            if len(identity) == 9 and is_pandigital(int(identity)):
                products.add(product)
    return sum(products)


# Look at all 9-digit pandigital numbers, then split digits apart and check that the identity holds.
# Product must be 4 digits, and the multiplied numbers can be either 1 digit and 4 digits, or 2 digits and 3 digits.
def sum_of_pandigital_products():
    products = set()
    for perm in itertools.permutations('123456789'):
        identity = int(''.join(perm))
        product = identity % 10 ** 4
        if (identity // 10 ** 8) * (identity // 10 ** 4 % 10 ** 4) == product:
            products.add(product)
        elif (identity // 10 ** 7) * (identity // 10 ** 4 % 10 ** 3) == product:
            products.add(product)
    return sum(products)


print(sum_of_pandigital_products())
