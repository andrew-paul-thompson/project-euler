def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def goldbachs_other_conjecture_holds(n):
    if n % 2 == 0 or is_prime(n):
        return True
    i = 1
    while True:
        if n - 2 * i ** 2 <= 0:
            return False
        elif is_prime(n - 2 * i ** 2):
            return True
        i += 1


def check_goldbachs_other_conjecture():
    n = 1
    while True:
        n += 2
        if not goldbachs_other_conjecture_holds(n):
            print(n)
            break


check_goldbachs_other_conjecture()
