from random import shuffle

VALUES = "A23456789XJQK"
COLORS = "SHCD"


class Card:
    def __init__(self, value, color):
        assert value in VALUES and color in COLORS, "Invalid Value or Color"
        self.value = value
        self.color = color

    def __str__(self):
        return self.color + self.value


class DeckCards:
    def __init__(self):
        self.cards = [Card(v, c) for c in COLORS for v in VALUES]

    def shuffle_cards(self):
        shuffle(self.cards)

    def draw_card(self):
        # assert len(self.cards) > 0, "No more cards!"
        return self.cards.pop(0)

    def __str__(self):
        s = ''
        for idx, i in enumerate(self.cards):
            if idx % 13 == 0 and idx != 0:
                s += '\n'
            s += str(i) + ' '
        return s


deck = DeckCards()
print("Ordered")
print(deck)

print()
print("Shuffled")
deck.shuffle_cards()
print(deck)

print()
for _ in range(10):
    print("Drawn Card:", deck.draw_card())

print()
print(deck)