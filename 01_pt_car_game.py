import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car properties
car_width = 50
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Obstacle properties
obstacle_width = 50
obstacle_height = 80
obstacle_speed = 7
obstacles = []  # List to store obstacles

# Game loop
running = True
clock = pygame.time.Clock()

def create_obstacle():
    obstacle_x = random.randint(0, WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    obstacles.append([obstacle_x, obstacle_y])

create_obstacle() #Create the first obstacle.

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move car
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Keep car within screen boundaries
    car_x = max(0, min(car_x, WIDTH - car_width))

    # Move obstacles and create new ones
    for obstacle in obstacles[:]:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            create_obstacle()

    # Collision detection
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if car_rect.colliderect(obstacle_rect):
            print("Game Over!")
            running = False

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (car_x, car_y, car_width, car_height))

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()