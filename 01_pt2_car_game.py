import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fast Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car properties (Player)
car_width = 50
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 7

# Obstacle properties (Multiple Cars)
obstacle_width = 50
obstacle_height = 80
obstacle_speed = 12  # Increased speed
obstacles = []

# Game loop
running = True
clock = pygame.time.Clock()

def create_obstacle():
    obstacle_x = random.randint(0, WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    obstacles.append([obstacle_x, obstacle_y])

def spawn_multiple_obstacles():
    if random.randrange(0, 100) < 5: #adjust to spawn more or less cars.
        create_obstacle()

create_obstacle() #create the first obstacle.

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
    car_x = max(0, min(car_x, WIDTH - car_width))

    for obstacle in obstacles[:]:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)

    spawn_multiple_obstacles() #spawn multiple cars.

    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if car_rect.colliderect(obstacle_rect):
            print("Game Over!")
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (car_x, car_y, car_width, car_height))

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

