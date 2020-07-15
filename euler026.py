import math


# Adapted from https://en.wikipedia.org/wiki/Repeating_decimal#Algorithm_for_positive_bases
def repeating_decimal_repetend_length(q):
    occurs = {}
    s = ''
    pos = 0
    p = 1
    while p not in occurs:
        occurs[p] = pos
        z = math.floor(10 * p / q)
        p = p * 10 - z * q
        if p == 0:
            return 0
        s += str(z)
        pos += 1
    return pos - occurs[p]


answer = max(range(1, 1000), key=repeating_decimal_repetend_length)
print(answer)
