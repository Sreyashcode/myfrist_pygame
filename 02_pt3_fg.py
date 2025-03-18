import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Fighting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.Font(None, 36)

# Player 1 properties
player1_width = 50
player1_height = 80
player1_x = 100
player1_y = HEIGHT - player1_height
player1_speed = 5
player1_health = 100
player1_power = "fireball"  # Initial power

# Player 2 properties
player2_width = 50
player2_height = 80
player2_x = WIDTH - 150
player2_y = HEIGHT - player2_height
player2_speed = 5
player2_health = 100
player2_power = "lightning"  # Initial power

# Projectile properties
projectile_width = 10
projectile_height = 10
projectile_speed = 10
player1_projectiles = []
player2_projectiles = []

# Game loop
running = True
clock = pygame.time.Clock()

def create_projectile(player, power):
    if player == 1:
        if power == "fireball":
            player1_projectiles.append([player1_x + player1_width, player1_y + player1_height // 2, RED])
        elif power == "iceball":
            player1_projectiles.append([player1_x + player1_width, player1_y + player1_height // 2, BLUE])
    elif player == 2:
        if power == "lightning":
            player2_projectiles.append([player2_x, player2_y + player2_height // 2, YELLOW])
        elif power == "rock":
            player2_projectiles.append([player2_x, player2_y + player2_height // 2, BLACK])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Player 1 shoots
                create_projectile(1, player1_power)
            if event.key == pygame.K_RETURN: # Player 2 shoots
                create_projectile(2, player2_power)
            if event.key == pygame.K_1: #player 1 power change
                player1_power = "fireball"
            if event.key == pygame.K_2: #player 1 power change
                player1_power = "iceball"
            if event.key == pygame.K_3: #player 2 power change
                player2_power = "lightning"
            if event.key == pygame.K_4: #player 2 power change
                player2_power = "rock"

    keys = pygame.key.get_pressed()

    # Player 1 movement
    if keys[pygame.K_a]:
        player1_x -= player1_speed
    if keys[pygame.K_d]:
        player1_x += player1_speed
    player1_x = max(0, min(player1_x, WIDTH // 2 - player1_width))

    # Player 2 movement
    if keys[pygame.K_LEFT]:
        player2_x -= player2_speed
    if keys[pygame.K_RIGHT]:
        player2_x += player2_speed
    player2_x = max(WIDTH // 2, min(player2_x, WIDTH - player2_width))

    # Projectile movement
    for projectile in player1_projectiles[:]:
        projectile[0] += projectile_speed
        if projectile[0] > WIDTH:
            player1_projectiles.remove(projectile)
    for projectile in player2_projectiles[:]:
        projectile[0] -= projectile_speed
        if projectile[0] < 0:
            player2_projectiles.remove(projectile)

    # Collision detection
    player1_rect = pygame.Rect(player1_x, player1_y, player1_width, player1_height)
    player2_rect = pygame.Rect(player2_x, player2_y, player2_width, player2_height)

    for projectile in player1_projectiles[:]:
        projectile_rect = pygame.Rect(projectile[0], projectile[1], projectile_width, projectile_height)
        if player2_rect.colliderect(projectile_rect):
            player2_health -= 10
            player1_projectiles.remove(projectile)

    for projectile in player2_projectiles[:]:
        projectile_rect = pygame.Rect(projectile[0], projectile[1], projectile_width, projectile_height)
        if player1_rect.colliderect(projectile_rect):
            player1_health -= 10
            player2_projectiles.remove(projectile)

    if player1_health <= 0 or player2_health <= 0:
        running = False
        if player1_health <= 0:
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins!")

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player1_x, player1_y, player1_width, player1_height))
    pygame.draw.rect(screen, RED, (player2_x, player2_y, player2_width, player2_height))

    for projectile in player1_projectiles:
        pygame.draw.rect(screen, projectile[2], (projectile[0], projectile[1], projectile_width, projectile_height))
    for projectile in player2_projectiles:
        pygame.draw.rect(screen, projectile[2], (projectile[0], projectile[1], projectile_width, projectile_height))

    # Health bars
    pygame.draw.rect(screen, BLACK, (50, 20, 200, 20))
    pygame.draw.rect(screen, GREEN, (50, 20, player1_health * 2, 20))
    player1_text = font.render(f"Player 1: {player1_power}", True, BLACK)
    screen.blit(player1_text, (50, 45))

    pygame.draw.rect(screen, BLACK, (WIDTH - 250, 20, 200, 20))
    pygame.draw.rect(screen, GREEN, (WIDTH - 250, 20, player2_health * 2, 20))
    player2_text = font.render(f"Player 2: {player2_power}", True, BLACK)
    screen.blit(player2_text, (WIDTH - 250, 45))

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 