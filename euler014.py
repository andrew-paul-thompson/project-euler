def collatz_sequence(start):
    n = start
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


class Memoize:

    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]


@Memoize
def collatz_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_length(n // 2)
    else:
        return 1 + collatz_length(3 * n + 1)


max_len = 0
best_start = -1
for i in range(1, 1000000):
    seq_len = collatz_length(i)
    if seq_len > max_len:
        max_len = seq_len
        best_start = i
print(best_start)
