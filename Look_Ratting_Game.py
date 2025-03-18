import pygame
import pygame.camera
import cv2
import numpy as np
import random

# Initialize Pygame
pygame.init()
pygame.camera.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Look Rating Game")

# Camera setup
cameras = pygame.camera.list_cameras()
if not cameras:
    print("No camera found.")
    exit()
cam = pygame.camera.Camera(cameras[0], (640, 480))
cam.start()

# Font setup
font = pygame.font.Font(None, 36)

# Face detection (using OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Rating function (placeholder, replace with actual ML model)
def rate_look(face_image):
    # Simulate a rating (replace with your model)
    rating = random.randint(1, 10)
    return rating

def display_text(text, color, position):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def pygame_to_cvimage(pygame_surface):
    """Convert a pygame surface into a cv2 image."""
    pygame_string = pygame.image.tostring(pygame_surface, 'RGB')
    cv_image = np.frombuffer(pygame_string, dtype=np.uint8).reshape(pygame_surface.get_height(), pygame_surface.get_width(), 3)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR) #convert to bgr for opencv
    return cv_image

def cvimage_to_pygame(cv_image):
    """Convert a cv2 image to a pygame surface."""
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    pygame_string = cv_image.tobytes()
    pygame_surface = pygame.image.fromstring(pygame_string, (cv_image.shape[1], cv_image.shape[0]), 'RGB')
    return pygame_surface

running = True
rating = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Capture an image when space is pressed
                pygame_image = cam.get_image()
                cv_image = pygame_to_cvimage(pygame_image)
                gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                if len(faces) > 0:
                    (x, y, w, h) = faces[0]
                    face_roi = cv_image[y:y+h, x:x+w]
                    rating = rate_look(face_roi)
                else:
                    rating = "No face detected"
    # Capture and display the camera feed
    pygame_image = cam.get_image()
    screen.blit(pygame_image, (0, 0))

    if rating is not None:
        if isinstance(rating, int):
            display_text(f"Rating: {rating}/10", (255, 255, 255), (10, 10))
        else:
            display_text(rating, (255, 0, 0), (10, 10))

    pygame.display.flip()

# Clean up
cam.stop()
pygame.quit()