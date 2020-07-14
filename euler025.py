class Fibonacci:

    def __init__(self):
        self.__fibs = {0: 1, 1: 1}

    def __getitem__(self, key):
        if isinstance(key, slice):
            if key.stop is None:
                raise ValueError('Cannot return unbounded slice of infinite sequence.')
            return [self[n] for n in range(
                key.start if key.start is not None else 0,
                key.stop,
                key.step if key.step is not None else 1)]
        if key in self.__fibs:
            return self.__fibs[key]
        else:
            self.__fibs[key] = self[key - 1] + self[key - 2]
            return self.__fibs[key]


fib = Fibonacci()
index = 0
for f in fib:
    index += 1
    if len(str(f)) == 1000:
        break
print(index)
