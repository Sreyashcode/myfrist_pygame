import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 100, 200)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Quiz")

# Quiz data (questions, answers, correct answer indices)
quiz_data = [
    {
        "question": "What is the capital of France?",
        "answers": ["London", "Paris", "Berlin", "Rome"],
        "correct_answer": 1,
    },
    {
        "question": "What is 2 + 2?",
        "answers": ["3", "4", "5", "6"],
        "correct_answer": 1,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": 1,
    },
    # Add more questions as needed
]

current_question = 0
score = 0
button_rects = []

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def draw_button(rect, color, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def check_answer(answer_index):
    global score, current_question
    if answer_index == quiz_data[current_question]["correct_answer"]:
        score += 1
    current_question += 1

def main():
    global current_question, score, button_rects
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(button_rects):
                        if rect.collidepoint(mouse_pos):
                            check_answer(i)

        screen.fill(WHITE)

        if current_question < len(quiz_data):
            question = quiz_data[current_question]["question"]
            answers = quiz_data[current_question]["answers"]

            draw_text(question, FONT, BLACK, screen, 50, 50)

            button_rects = []
            for i, answer in enumerate(answers):
                button_rect = pygame.Rect(50, 150 + i * 50, 300, 40)
                button_rects.append(button_rect)

                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    draw_button(button_rect, BUTTON_HOVER_COLOR, answer)
                else:
                    draw_button(button_rect, BUTTON_COLOR, answer)

        else:
            draw_text(f"Quiz complete! Your score: {score}/{len(quiz_data)}", FONT, BLACK, screen, 50, 50)
            button_rects = [] #clear button rects so they are not accidently clicked.
            draw_text("Press ESC to exit.", FONT, BLACK, screen, 50, 100)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()