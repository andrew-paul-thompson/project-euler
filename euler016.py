def sum_digits(n):
    return sum(map(int, str(n)))


def sum_digits_of_two_to_the_nth_power(n):
    return sum_digits(2 ** n)


print(sum_digits_of_two_to_the_nth_power(1000))
