import math


def is_digit_factorial(n):
    return n == sum([math.factorial(int(d)) for d in str(n)])


# If number has 8 or more digits, then the factorial digit sum will always be less than the number.
def digit_factorials():
    return [i for i in range(3, 10000000) if is_digit_factorial(i)]


print(sum(digit_factorials()))
