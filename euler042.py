def load_words():
    with open('input/p042_words.txt', 'r') as file:
        return file.read()[1:-1].split('","')


def letter_value(letter):
    return ord(letter.upper()) - ord('A') + 1


def word_value(word):
    return sum(letter_value(letter) for letter in word)


def triangular_numbers():
    return [n * (n + 1) // 2 for n in range(30)]


print(len([word for word in load_words() if word_value(word) in triangular_numbers()]))
