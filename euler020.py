def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def sum_of_digits(n):
    return sum([int(c) for c in str(n)])


print(sum_of_digits(factorial(100)))
