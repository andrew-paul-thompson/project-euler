ranks = '23456789TJQKA'
suits = 'SHCD'
rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
               'A': 14}


def load_data():
    with open('input/p054_poker.txt', 'r') as file:
        return [line.strip().split(' ') for line in file.readlines()]


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def is_flush(self):
        return all(self.cards[0].suit == self.cards[i].suit for i in range(1, 5))

    def is_straight(self):
        ace_high_values = [rank_values[card.rank] for card in self.cards]
        ace_low_values = [1 if rank == 14 else rank for rank in ace_high_values]
        return any(sorted(v) == list(range(min(v), max(v) + 1)) for v in [ace_high_values, ace_low_values])

    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_four_of_a_kind(self):
        for card in self.cards:
            if len([c for c in self.cards if c.rank == card.rank]) == 4:
                return True
        return False

    def is_three_of_a_kind(self):
        for card in self.cards:
            if len([c for c in self.cards if c.rank == card.rank]) == 3:
                return True
        return False

    def is_full_house(self):
        return (self.cards[0].rank == self.cards[1].rank == self.cards[2].rank) and (
                self.cards[2].rank != self.cards[3].rank) and (self.cards[3].rank == self.cards[4].rank)

    def is_two_pairs(self):
        groups = []
        for card in self.cards:
            groups.append(len([c for c in self.cards if c.rank == card.rank]))
        return groups.count(2) == 4

    def is_one_pair(self):
        groups = []
        for card in self.cards:
            groups.append(len([c for c in self.cards if c.rank == card.rank]))
        return groups.count(2) == 2

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

    def score(self):

        rank_counts = [sum(1 for x in self.cards if rank_values[x.rank] == i) for i in range(2, 15)]
        high_card = 0
        for idx, i in enumerate(reversed(rank_counts)):
            if i > 0:
                high_card = len(rank_counts) - idx - 1

        if self.is_straight_flush():
            score = 0x8 << 20 | (high_card << 16)
        elif self.is_four_of_a_kind():
            four_of_a_kind_card = rank_counts.index(4)
            other_card = rank_counts.index(1)
            score = 0x7 << 20 | (four_of_a_kind_card << 16) | (other_card << 12)
        elif self.is_full_house():
            three_of_a_kind_card = rank_counts.index(3)
            pair_card = rank_counts.index(2)
            score = 0x6 << 20 | (three_of_a_kind_card << 16) | (pair_card << 12)
        elif self.is_flush():
            score = 0x5 << 20 | (high_card << 16)
        elif self.is_straight():
            score = 0x4 << 20 | (high_card << 16)
        elif self.is_three_of_a_kind():
            three_of_a_kind_card = rank_counts.index(3)
            other_cards = [rank_counts.index(1), rank_counts.index(1, rank_counts.index(1) + 1)]
            score = 0x3 << 20 | (three_of_a_kind_card << 16) | (other_cards[1] << 12) | (other_cards[0] << 8)
        elif self.is_two_pairs():
            lower_pair_card = rank_counts.index(2)
            higher_pair_card = rank_counts.index(2, rank_counts.index(2) + 1)
            other_card = rank_counts.index(1)
            score = 0x2 << 20 | (higher_pair_card << 16) | (lower_pair_card << 12) | (other_card << 8)
        elif self.is_one_pair():
            pair_card = rank_counts.index(2)
            other_cards = [idx for idx, i in enumerate(rank_counts) if i == 1]
            score = 0x1 << 20 | pair_card << 16 | other_cards[2] << 12 | other_cards[1] << 8 | other_cards[0] << 4
        else:
            best_cards = [idx for idx, i in enumerate(rank_counts) if i == 1]
            score = 0x0 << 20 | (best_cards[4] << 16) | (best_cards[3] << 12) | (best_cards[2] << 8) | (
                    best_cards[1] << 4) | (best_cards[0])
        return score


def main():
    p1_wins = 0
    data = load_data()
    for hand_data in data:

        player1_hand = Hand([Card(card_data[0], card_data[1]) for card_data in hand_data[:5]])
        player2_hand = Hand([Card(card_data[0], card_data[1]) for card_data in hand_data[5:]])

        p1_score = player1_hand.score()
        p2_score = player2_hand.score()
        if p1_score > p2_score:
            p1_wins += 1

    print(p1_wins)


if __name__ == '__main__':
    main()
