def alphabetical_value(s):
    return sum([ord(c) - ord('A') + 1 for c in s.upper()])


with open('input/p022_names.txt', 'r') as file:
    names = [s.replace('"', '') for s in file.read().split(',')]
print(sum([alphabetical_value(s) * (i + 1) for i, s in enumerate(sorted(names))]))
