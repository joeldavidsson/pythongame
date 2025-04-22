from player import Player
from utils import calculate_score


class Dealer(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def play_turn(self, deck):
        while calculate_score(self.hand) < 17:
            self.add_card(deck.deal())

    def show_hand(self, hide_first=False):
        if hide_first:
            hand_display = ["[Hidden card]"] + [str(card) for card in self.hand[1:]]
        else:
            hand_display = [str(card) for card in self.hand]
        return f"{', '.join(hand_display)}"
