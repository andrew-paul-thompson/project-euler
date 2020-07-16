def nth_power_digit_sum(number, power):
    return sum(int(d) ** power for d in str(number))


def is_valid(n):
    return n == nth_power_digit_sum(n, 5)


print(sum(i for i in range(2, 1000000) if is_valid(i)))
