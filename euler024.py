from itertools import permutations, islice

print(''.join([str(x) for x in next(islice(permutations(list(range(10))), 999999, None))]))
