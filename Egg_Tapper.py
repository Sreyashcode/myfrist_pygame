import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egg Tapper")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Egg properties
egg_radius = 50
egg_x = WIDTH // 2
egg_y = HEIGHT // 2
tap_count = 0
cracked = False

# Font
font = pygame.font.Font(None, 36)

# Egg images (replace with your own)
egg_image = pygame.Surface((egg_radius * 2, egg_radius * 2), pygame.SRCALPHA)
pygame.draw.ellipse(egg_image, WHITE, (0, 0, egg_radius * 2, egg_radius * 2))

cracked_image = pygame.Surface((egg_radius * 2, egg_radius * 2), pygame.SRCALPHA)
pygame.draw.ellipse(cracked_image, GRAY, (0, 0, egg_radius * 2, egg_radius * 2))
pygame.draw.line(cracked_image, BLACK, (0,0), (egg_radius*2,egg_radius*2), 5)
pygame.draw.line(cracked_image, BLACK, (egg_radius*2,0), (0,egg_radius*2), 5)

# Troll text
troll_text = font.render("Troll!", True, BLACK)
troll_rect = troll_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if (egg_x - egg_radius < mouse_pos[0] < egg_x + egg_radius and
                egg_y - egg_radius < mouse_pos[1] < egg_y + egg_radius and not cracked):
                tap_count += 1
                if tap_count >= 100:
                    cracked = True

    screen.fill(WHITE)

    if not cracked:
        screen.blit(egg_image, (egg_x - egg_radius, egg_y - egg_radius))
        tap_text = font.render(f"Taps: {tap_count}", True, BLACK)
        tap_rect = tap_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(tap_text, tap_rect)
    else:
        screen.blit(cracked_image, (egg_x - egg_radius, egg_y - egg_radius))
        screen.blit(troll_text, troll_rect)

    pygame.display.flip()

pygame.quit()