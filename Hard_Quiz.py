import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extreme Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 48)

# Quiz data (extreme questions)
quiz_data = [
    {
        "question": "What is the theoretical maximum number of dimensions in string theory?",
        "options": ["10", "11", "26", "Infinite"],
        "answer": "26",
    },
    {
        "question": "What is the approximate age of the universe in years?",
        "options": ["1.38 billion", "13.8 billion", "138 billion", "1.38 trillion"],
        "answer": "13.8 billion",
    },
    {
        "question": "What is the Chandrasekhar limit, approximately, in solar masses?",
        "options": ["0.44", "1.44", "4.44", "14.4"],
        "answer": "1.44",
    },
    {
        "question": "Which mathematical problem, if solved, would break most public-key cryptography?",
        "options": ["Riemann Hypothesis", "P vs NP", "Goldbach's Conjecture", "The Collatz Conjecture"],
        "answer": "P vs NP",
    },
    {
        "question": "What is the approximate Schwarzschild radius of a black hole with the mass of the Sun?",
        "options": ["3 km", "30 km", "300 km", "3000 km"],
        "answer": "3 km",
    },
    {
        "question": "Which particle is theorized to give mass to other particles?",
        "options": ["Photon", "Gluon", "Higgs Boson", "Neutrino"],
        "answer": "Higgs Boson",
    },
    {
        "question": "What is the approximate number of stars in the observable universe?",
        "options": ["10^11", "10^23", "10^40", "10^80"],
        "answer": "10^23",
    },
    {
        "question": "What is the approximate speed of gravitational waves?",
        "options": ["Speed of sound", "Half the speed of light", "Speed of light", "Twice the speed of light"],
        "answer": "Speed of light",
    },
    {
        "question": "What is the approximate entropy of a supermassive black hole in bits?",
        "options": ["10^10", "10^40", "10^90", "10^120"],
        "answer": "10^90",
    },
    {
        "question": "Which paradox is related to the information loss in black holes?",
        "options": ["Twin Paradox", "Grandfather Paradox", "Fermi Paradox", "Information Paradox"],
        "answer": "Information Paradox",
    }
]

# Game variables
current_question = 0
score = 0
game_over = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def display_question(question_data):
    screen.fill(BLACK)
    draw_text(question_data["question"], font, WHITE, screen, 50, 50)
    for i, option in enumerate(question_data["options"]):
        draw_text(f"{i + 1}. {option}", font, WHITE, screen, 100, 150 + i * 50)

def display_score(score):
    draw_text(f"Score: {score}", large_font, GREEN, screen, WIDTH // 2 - 50, 10)

def display_game_over(score):
    screen.fill(BLACK)
    draw_text("Game Over!", large_font, RED, screen, WIDTH // 2 - 100, HEIGHT // 2 - 50)
    draw_text(f"Final Score: {score}", font, WHITE, screen, WIDTH // 2 - 80, HEIGHT // 2 + 20)
    draw_text("Press SPACE to restart.", font, WHITE, screen, WIDTH//2-120, HEIGHT//2 + 60)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if quiz_data[current_question]["options"][0] == quiz_data[current_question]["answer"]:
                        score += 1
                    current_question += 1
                elif event.key == pygame.K_2:
                    if quiz_data[current_question]["options"][1] == quiz_data[current_question]["answer"]:
                        score += 1
                    current_question += 1
                elif event.key == pygame.K_3:
                    if quiz_data[current_question]["options"][2] == quiz_data[current_question]["answer"]:
                        score += 1
                    current_question += 1
                elif event.key == pygame.K_4:
                    if quiz_data[current_question]["options"][3] == quiz_data[current_question]["answer"]:
                        score += 1
                    current_question += 1

                if current_question >= len(quiz_data):
                    game_over = True
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_over = False
                    current_question = 0
                    score = 0
                    random.shuffle(quiz_data)

    if not game_over:
        if current_question < len(quiz_data):
            display_question(quiz_data[current_question])
            display_score(score)
        else:
            game_over = True
    else:
        display_game_over(score)

    pygame.display.flip()

pygame.quit()
sys.exit()