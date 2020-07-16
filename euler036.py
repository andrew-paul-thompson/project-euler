def is_palindrome(s):
    return s == s[::-1]


def is_palindromic_number(n, base=10):
    if base == 2:
        s = bin(n)[2:]
    elif base == 8:
        s = oct(n)[2:]
    elif base == 10:
        s = str(n)
    elif base == 16:
        s = hex(n)[2:]
    else:
        raise ValueError('Unsupported base {base}')
    return is_palindrome(s)


def palindromic_numbers_in_base10_and_base2():
    palindromic_numbers = set()
    for i in range(1, 1000000):
        if is_palindromic_number(i) and is_palindromic_number(i, 2):
            palindromic_numbers.add(i)
    return palindromic_numbers


print(sum(palindromic_numbers_in_base10_and_base2()))
