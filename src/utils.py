import pygame


def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        if card.value in ["J", "Q", "K"]:
            score += 10
        elif card.value == "A":
            score += 11
            aces += 1
        else:
            score += int(card.value)

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def draw_centered_text(surface, text, font, color, center):
    render_text = font.render(text, True, color)
    text_rect = render_text.get_rect(center=center)
    surface.blit(render_text, text_rect)


def draw_card(surface, x, y, text, font, color, text_color, center, padding=10):
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect()

    card_width = max(text_rect.width + 2 * padding, 60)
    card_height = max(text_rect.height + 2 * padding, 90)
    card_rect = pygame.Rect(x, y, card_width, card_height)

    pygame.draw.rect(surface, color, card_rect)

    text_rect.center = card_rect.center
    surface.blit(text_surf, text_rect)


def cursor_appearance(mouse_pos, buttons):
    for button in buttons:
        if button.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
