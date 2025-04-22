import pygame

from dealer import Dealer
from deck import Deck
from player import Player
from utils import calculate_score


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("YOU")
        self.dealer = Dealer("DEALER")
        self.game_over = False
        self.result_text = ""
        self.dealer_reveal = False

        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    def player_hit(self):
        if not self.game_over:
            self.player.add_card(self.deck.deal())
            if self.calculate_score(self.player.hand) > 21:
                self.check_winner()
                self.game_over = True
            elif self.calculate_score(self.player.hand) == 21:
                self.check_winner()
                self.game_over = True

    def player_stand(self):
        if not self.game_over:
            self.dealer_reveal = True
            while self.calculate_score(self.dealer.hand) < 17:
                self.dealer.add_card(self.deck.deal())
            self.check_winner()

    def check_winner(self):
        player_score = self.calculate_score(self.player.hand)
        dealer_score = self.calculate_score(self.dealer.hand)

        win_sound = pygame.mixer.Sound("assets/sounds/win.mp3")
        win_sound.set_volume(0.5)
        lose_sound = pygame.mixer.Sound("assets/sounds/lost.mp3")
        lose_sound.set_volume(0.5)

        if dealer_score > 21:
            self.result_text = "Dealer busted! You win!".upper()
            win_sound.play()
        elif player_score > 21:
            self.result_text = "You busted! Dealer wins.".upper()
            lose_sound.play()
        elif player_score == 21:
            self.result_text = "Blackjack! You win!".upper()
            win_sound.play()
        elif dealer_score == 21:
            self.result_text = "Dealer has Blackjack! Dealer wins.".upper()
            lose_sound.play()
        elif player_score > dealer_score:
            self.result_text = "You win!".upper()
            win_sound.play()
        elif player_score < dealer_score:
            self.result_text = "Dealer wins!".upper()
            lose_sound.play()
        else:
            self.result_text = "It's a tie!".upper()
        self.game_over = True

    def reset(self):
        pygame.mixer.stop()
        self.__init__()

    def calculate_score(self, hand):
        return calculate_score(hand)
