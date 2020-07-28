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


def diagonal_numbers():
    n = 1
    offset = 2
    yield n
    while True:
        for _ in range(4):
            n += offset
            yield n
        offset += 2


def diagonal_numbers_by_side_length(side_length):
    return list(itertools.islice(diagonal_numbers(), (side_length // 2) * 4 + 1))


def main():
    side_length = 7
    gen = diagonal_numbers()
    for _ in range(13):
        next(gen)
    number_count = 13
    prime_count = 8
    while True:
        side_length += 2
        next_numbers = [next(gen) for _ in range(4)]
        number_count += 4
        prime_count += sum([1 for next_num in next_numbers if is_prime(next_num)])
        percentage_prime = prime_count / number_count
        if percentage_prime < 0.1:
            break
    print(side_length)


if __name__ == '__main__':
    main()
