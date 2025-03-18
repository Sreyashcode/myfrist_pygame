import pygame
import speech_recognition as sr
import pyttsx3
import threading
import time

# --- Pygame Setup ---
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Voice Controlled Assistant")
font = pygame.font.Font(None, 36)
text_surface = font.render("", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# --- Text-to-Speech Setup ---
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# --- Speech Recognition Setup ---
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def process_command(command):
    global text_surface, text_rect
    if "hello" in command:
        response = "Hello! How can I assist you?"
    elif "what is your name" in command:
        response = "I am your voice assistant."
    elif "exit" in command or "quit" in command:
        response = "Goodbye!"
        speak(response)
        pygame.quit()
        exit()
    elif "draw a circle" in command:
        response = "Drawing a circle."
        pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 50)
        pygame.display.flip()
    elif "clear screen" in command:
        response = "Clearing the screen."
        screen.fill((0,0,0))
        pygame.display.flip()
    elif "show time" in command:
        current_time = time.strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
    else:
        response = "I'm sorry, I don't understand that command."

    speak(response)
    text_surface = font.render(response, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# --- Main Game Loop ---
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    pygame.quit()

def listen_thread():
    while True:
        command = listen()
        if command:
            process_command(command)

# --- Start Threads ---
listen_thread_instance = threading.Thread(target=listen_thread)
listen_thread_instance.daemon = True #close thread when main program exits
listen_thread_instance.start()
main()