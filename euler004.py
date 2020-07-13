def is_palindromic(n):
    return str(n) == str(n)[::-1]


def palindromes(n_digit=3):
    palindrome_list = []
    for i in range(10 ** (n_digit - 1), 10 ** n_digit):
        for j in range(10 ** (n_digit - 1), 10 ** n_digit):
            if is_palindromic(i * j):
                palindrome_list.append(i * j)
    return palindrome_list


print(max(palindromes()))
