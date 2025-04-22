import pygame

from game import Game
from utils import cursor_appearance, draw_card, draw_centered_text

pygame.init()

WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

background = pygame.image.load("assets/images/bjtable.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
card_back_img = pygame.image.load("assets/images/cardbg.png")
card_back_img = pygame.transform.scale(card_back_img, (60, 90))
card_bg = pygame.Rect(0, 0, 60, 0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 128, 50)
DARKGREEN = (0, 100, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont("Arial", 30, bold=True)
big_font = pygame.font.SysFont("Arial", 50, bold=True)

button_width = 200
button_height = 50
hit_button = pygame.Rect(
    WIDTH // 4 - button_width // 2,
    HEIGHT - 100,
    button_width,
    button_height,
)
stand_button = pygame.Rect(
    3 * WIDTH // 4 - button_width // 2,
    HEIGHT - 100,
    button_width,
    button_height,
)
play_again_button = pygame.Rect(
    2 * WIDTH // 4 - button_width // 2,
    HEIGHT - 100,
    button_width,
    button_height,
)
start_button = pygame.Rect(
    WIDTH // 2 - button_width // 2,
    HEIGHT // 2 - button_height // 2,
    button_width,
    button_height,
)

game = Game()
game_started = False

running = True
while running:
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    if not game_started:
        cursor_appearance(mouse_pos, [start_button])
    elif not game.game_over:
        cursor_appearance(mouse_pos, [hit_button, stand_button])
    else:
        cursor_appearance(mouse_pos, [play_again_button])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                if start_button.collidepoint(event.pos):
                    game_started = True
            else:
                if not game.game_over:
                    if hit_button.collidepoint(event.pos):
                        game.player_hit()
                    elif stand_button.collidepoint(event.pos):
                        game.player_stand()
                else:
                    if play_again_button.collidepoint(event.pos):
                        game.reset()

    if not game_started:
        pygame.draw.rect(screen, DARKGREEN, start_button)
        start_text = font.render("START GAME", True, WHITE)
        screen.blit(
            start_text,
            (
                start_button.centerx - start_text.get_width() // 2,
                start_button.centery - start_text.get_height() // 2,
            ),
        )
    else:
        player_score = game.calculate_score(game.player.hand)
        x_start = WIDTH // 2 - 80
        y = 470
        spacing = 80
        for i, card in enumerate(game.player.hand):
            card_str = str(card)
            if card.suit in ["Hearts", "Diamonds"]:
                text_color = RED
            else:
                text_color = BLACK
            draw_card(
                screen,
                x_start + i * spacing,
                y,
                card_str,
                font,
                WHITE,
                text_color,
                center=(WIDTH // 2, HEIGHT // 2),
            )

        score_text = f"YOU: {player_score}"
        draw_centered_text(screen, score_text, font, WHITE, center=(WIDTH // 2, y - 40))

        dealer_score = game.calculate_score(game.dealer.hand)
        x_start = WIDTH // 2 - 80
        y = 100
        spacing = 80
        for i, card in enumerate(game.dealer.hand):
            if i == 0 and not game.dealer_reveal:
                screen.blit(card_back_img, (x_start + i * spacing, y))
            else:
                card_str = str(card)
                if card.suit in ["Hearts", "Diamonds"]:
                    text_color = RED
                else:
                    text_color = BLACK
                draw_card(
                    screen,
                    x_start + i * spacing,
                    y,
                    card_str,
                    font,
                    WHITE,
                    text_color,
                    center=(WIDTH // 2, HEIGHT // 2),
                )

        dealer_score_text = f"DEALER: {dealer_score if game.dealer_reveal else '*'}"
        draw_centered_text(
            screen, dealer_score_text, font, WHITE, center=(WIDTH // 2, y + 120)
        )

        if not game.game_over:
            pygame.draw.rect(screen, GREEN, hit_button)
            pygame.draw.rect(screen, RED, stand_button)

            hit_text = font.render("HIT", True, WHITE)
            stand_text = font.render("STAND", True, WHITE)
            screen.blit(
                hit_text,
                (
                    hit_button.centerx - hit_text.get_width() // 2,
                    hit_button.centery - hit_text.get_height() // 2,
                ),
            )
            screen.blit(
                stand_text,
                (
                    stand_button.centerx - stand_text.get_width() // 2,
                    stand_button.centery - stand_text.get_height() // 2,
                ),
            )
        else:
            result_display = font.render(game.result_text, True, RED)
            draw_centered_text(
                screen,
                game.result_text,
                big_font,
                WHITE,
                center=(WIDTH // 2, HEIGHT // 2 - 50),
            )

            pygame.draw.rect(screen, GREEN, play_again_button)
            playagain_text = "PLAY AGAIN"
            draw_centered_text(
                screen,
                playagain_text,
                font,
                WHITE,
                center=play_again_button.center,
            )

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
