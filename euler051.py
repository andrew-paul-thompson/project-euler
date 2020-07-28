import itertools


def prime_generator():
    yield 2
    composite_dict = {}
    n = 1
    while True:
        n += 2
        p = composite_dict.pop(n, None)
        if p is not None:
            test = n + 2 * p
            while test in composite_dict:
                test = test + 2 * p
            composite_dict[test] = p
        else:
            composite_dict[n * n] = n
            yield n


def is_prime(n):
    result = True
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        gen = prime_generator()
        for p in gen:
            if p > int(n ** 0.5) + 1:
                break
            if n % p == 0:
                result = False
                break
        gen.close()
    return result


def replace_digits(n, digits, new_digit):
    return n + sum((new_digit * 10 ** digit) - (n // 10 ** digit % 10 * 10 ** digit) for digit in digits)


def generate_digit_replaced_family(n, digits):
    length = len(str(n))
    return [replace_digits(n, digits, new_digit) for new_digit in range(10) if
            new_digit >= 1 or length - 1 not in digits]


def get_biggest_prime_family(n):
    biggest = []
    length = len(str(n))
    for number_of_digits_to_replace in range(1, length):
        for digits_to_replace in itertools.combinations(range(0, length), number_of_digits_to_replace):
            digit_replaced_prime_family = list(filter(is_prime, generate_digit_replaced_family(n, digits_to_replace)))
            biggest = max(biggest, digit_replaced_prime_family, key=len)
    return biggest


def main():
    for prime in prime_generator():
        family = get_biggest_prime_family(prime)
        if prime > 56003 and len(family) == 8:
            print(min(family))
            break


if __name__ == '__main__':
    main()
