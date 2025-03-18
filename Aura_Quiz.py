import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions (smaller)
WIDTH, HEIGHT = 320, 240
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aura Quiz")

# Colors (Black and White)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Font (Smaller)
font = pygame.font.Font(None, 20)
small_font = pygame.font.Font(None, 16)

# Questions (Indian Memes - 2024 - Fill in the Blank)
meme_questions = [
    {"question": "Meme: 'Bhai, kya chal raha hai? ... chal raha hai.'", "answer": "Sab"},
    {"question": "Meme: 'Aaj toh ... mood hai.'", "answer": "Chill"},
    {"question": "Meme: 'Yeh kya ... dekh liya!'", "answer": "Bakwaas"},
    {"question": "Meme: '... ho gaya!'", "answer": "Viral"},
    {"question": 'Meme: "... bhi nahi pata?"', "answer": "Yeh"},
    {"question": "Meme: '... kar raha hai?'", "answer": "Kya"},
    {"question": "Meme: '... ho tum!'", "answer": "Awesome"},
    {"question": "Meme: '... bolti public!'", "answer": "Kya"},
    {"question": "Meme: '... nahi hua!'", "answer": "Kuch"},
    {"question": "Meme: '... scene hai!'", "answer": "Full"},
    {"question": "Meme: 'Cheem taapak ... dum'", "answer": "dum"},
    {"question": "Meme: 'Juice pila do ... ka'", "answer": "mosambi"},
    {"question": "Meme: 'Kis ... ki chaddi pehne ho?'", "answer": "colour"},
    {"question": "Meme: 'Danis bhai zinda ...'", "answer": "rehte to"},
    {"question": "Meme: 'Elvish ...'", "answer": "bhaai"},
]

math_questions = [
    {"question": "12 * 8?", "answer": "96"},
    {"question": "100 / 4?", "answer": "25"},
    {"question": "15 + 23?", "answer": "38"},
    {"question": "50 - 17?", "answer": "33"},
    {"question": "7 * 9?", "answer": "63"},
]

science_questions = [
    {"question": "Water symbol?", "answer": "H2O"},
    {"question": "Largest planet?", "answer": "Jupiter"},
    {"question": "Plants absorb?", "answer": "Carbon dioxide"},
    {"question": "Plant food process?", "answer": "Photosynthesis"},
    {"question": "Light speed?", "answer": "299792458 m/s"},
]

# Game variables
score = 0
question_index = 0
current_questions = []
user_answer = ""
question_type_counts = {"meme": 15, "math": 5, "science": 5}
used_meme_questions = []
used_math_questions = []
used_science_questions = []

def generate_questions():
    global current_questions, question_index, used_meme_questions, used_math_questions, used_science_questions
    current_questions = []
    question_index = 0
    used_meme_questions = []
    used_math_questions = []
    used_science_questions = []

    for _ in range(question_type_counts["meme"]):
        available_questions = [q for q in meme_questions if q not in used_meme_questions]
        if not available_questions:
            break
        question = random.choice(available_questions)
        current_questions.append(question)
        used_meme_questions.append(question)

    for _ in range(question_type_counts["math"]):
        available_questions = [q for q in math_questions if q not in used_math_questions]
        if not available_questions:
            break
        question = random.choice(available_questions)
        current_questions.append(question)
        used_math_questions.append(question)

    for _ in range(question_type_counts["science"]):
        available_questions = [q for q in science_questions if q not in used_science_questions]
        if not available_questions:
            break
        question = random.choice(available_questions)
        current_questions.append(question)
        used_science_questions.append(question)

def display_question(question_data):
    text = font.render(question_data["question"], True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text, text_rect)

def display_status_bar():
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - 30, WIDTH, 30))
    score_text = small_font.render(f"Score: {score} / 250", True, BLACK)
    score_rect = score_text.get_rect(midleft=(5, HEIGHT - 15))
    screen.blit(score_text, score_rect)
    question_num_text = small_font.render(f"Q: {question_index + 1} / {len(current_questions)}", True, BLACK)
    question_num_rect = question_num_text.get_rect(center=(WIDTH // 2, HEIGHT - 15))
    screen.blit(question_num_text, question_num_rect)

def display_end_screen():
    screen.fill(WHITE)
    end_text = font.render(f"Game Over! Score: {score} / 250", True, BLACK)
    end_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(end_text, end_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

# Game loop
running = True
generate_questions()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if question_index < len(current_questions):
                    if user_answer.lower() == current_questions[question_index]["answer"].lower():
                        score += 10
                    user_answer = ""
                    question_index += 1
                    if question_index >= len(current_questions):
                        display_end_screen()
                        running = False
            elif event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]
            else:
                user_answer += event.unicode

    screen.fill(WHITE)

    if question_index < len(current_questions):
        display_question(current_questions[question_index])
        answer_text = font.render(user_answer, True, BLACK)
        answer_rect = answer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(answer_text, answer_rect)
    display_status_bar()

    pygame.display.flip()

pygame.quit()