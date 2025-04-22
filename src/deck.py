import random


class Card:
    SYMBOLS = {
        "Hearts": "\u2665",
        "Diamonds": "\u2666",
        "Clubs": "\u2663",
        "Spades": "\u2660",
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}{Card.SYMBOLS[self.suit]}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(s, v) for s in suits for v in values]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
