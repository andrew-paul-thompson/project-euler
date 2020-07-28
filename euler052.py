def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))


def main():
    found = False
    x = 0
    while not found:
        x += 1
        found = all(same_digits(x, n * x) for n in range(2, 7))
    print(x)


if __name__ == '__main__':
    main()
