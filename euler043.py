import itertools


def extract_three_digits(number, index):
    return int(str(number)[index - 1:index + 2])


def is_substring_divisible(n):
    indexes = [2, 3, 4, 5, 6, 7, 8]
    primes = [2, 3, 5, 7, 11, 13, 17]
    return all(extract_three_digits(n, indexes[i]) % primes[i] == 0 for i in range(7))


def substring_divisible_pandigital_numbers():
    matching_numbers = set()
    for perm in itertools.permutations('0123456789'):
        num = int(''.join(perm))
        if is_substring_divisible(num):
            matching_numbers.add(num)
    return matching_numbers


print(sum(substring_divisible_pandigital_numbers()))
