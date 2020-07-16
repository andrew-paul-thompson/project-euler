def create_spiral(size):
    arr = [[0 for _ in range(size)] for _ in range(size)]

    if size % 2 == 1:
        i = size // 2
        j = size // 2
    else:
        i = size // 2 - 1
        j = size // 2 - 1

    count = 1
    arr[i][j] = count

    for level in range(2, size + 1):
        # Over by one.
        count += 1
        i += (-1) ** (level % 2)
        arr[i][j] = count

        # Down/up the outside
        for _ in range(1, level):
            count += 1
            j += (-1) ** (level % 2)
            arr[i][j] = count

        # Left/right across the bottom or top
        for _ in range(1, level):
            count += 1
            i += (-1) ** (level % 2 + 1)
            arr[i][j] = count

    return arr


def get_diagonal_numbers(spiral):
    arr = []
    for i in range(len(spiral)):
        arr.append(spiral[i][i])
        arr.append(spiral[i][len(spiral) - i - 1])
    arr.remove(1)
    return arr


def calculate_diagonal_sum(size):
    total = 1
    i = 1
    jump_length = 2
    while i <= size * size - 1:
        total += 4 * i + 10 * jump_length
        i += jump_length * 4
        jump_length += 2
    return total


print(calculate_diagonal_sum(1001))
