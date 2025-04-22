from utils import calculate_score


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_score(self):
        return calculate_score(self.hand)
