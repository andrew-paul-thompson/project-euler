def wordify(n):
    mapping = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
               12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
               16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
               70: 'seventy', 80: 'eighty', 90: 'ninety',
               10 ** 2: 'hundred',
               10 ** 3: 'thousand'}
    word = ''
    if n == 0:
        return mapping[n]
    if n >= 10 ** 3:
        word += f'{wordify(n // 1000)} {mapping[1000]}'
        if n % 1000 != 0:
            word += ' '
        n -= n // 1000 * 1000
    if n >= 100:
        word += f'{wordify(n // 100)} {mapping[100]}'
        if n % 100 != 0:
            word += ' and '
        n -= n // 100 * 100
    if n > 19:
        word += f'{mapping[n // 10 * 10]}'
        if n % 10 != 0:
            word += '-'
        n -= n // 10 * 10
    if n > 0:
        word += f'{mapping[n]}'
    return word


def count_letters(s):
    return len([c for c in s if c.isalpha()])


print(sum([count_letters(wordify(i)) for i in range(1, 1001)]))
