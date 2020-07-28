def is_palindromic(n):
    return str(n) == str(n)[::-1]


def reverse_and_add(n):
    return n + int(str(n)[::-1])


def is_lychrel_number(n):
    for i in range(50):
        n = reverse_and_add(n)
        if is_palindromic(n):
            return False
    return True


def main():
    print(sum(1 for i in range(1, 10000) if is_lychrel_number(i)))


if __name__ == '__main__':
    main()
