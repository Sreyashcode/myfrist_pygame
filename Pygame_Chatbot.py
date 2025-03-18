import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Chatbot")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)

# Chat log
chat_log = []

# Input box
input_box = pygame.Rect(20, HEIGHT - 60, WIDTH - 40, 40)
input_text = ""
active = False

# Simple chatbot responses (expand as needed)
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye!"
    elif "what is your name" in user_input:
        return "I'm a simple Pygame chatbot."
    else:
        return "I don't understand. Please try again."

def draw_chat_log():
    y = 20
    for line in chat_log:
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (20, y))
        y += 30

def draw_input_box():
    pygame.draw.rect(screen, GRAY, input_box, 2)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

def main():
    global active, input_text, chat_log

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        chat_log.append("You: " + input_text)
                        response = get_response(input_text)
                        chat_log.append("Bot: " + response)
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill(WHITE)
        draw_chat_log()
        draw_input_box()
        pygame.display.flip()

if __name__ == "__main__":
    main()