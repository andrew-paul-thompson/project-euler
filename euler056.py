def digital_sum(n):
    return sum([int(d) for d in str(n)])


def main():
    print(max(digital_sum(a ** b) for a in range(1, 100) for b in range(1, 100)))


if __name__ == '__main__':
    main()
