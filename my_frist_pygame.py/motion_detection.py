import pygame
import cv2
import numpy as np
import random

def motion_detection(camera_index=0, sensitivity=30, min_area=500):
    """
    Detects motion using a connected camera and Pygame for display.
    """

    pygame.init()

    # Initialize camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Get initial frame and convert to grayscale
    ret, frame1 = cap.read()
    if not ret:
        print("Error: Could not read first frame.")
        cap.release()
        return

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

    # Pygame setup
    width, height = frame1.shape[1], frame1.shape[0]
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Red Light Green Light")

    running = True
    game_started = False
    red_light = False # True = Red light, False = Green Light
    motion_detected = False
    win = False

    # Button setup
    button_rect = pygame.Rect(width // 2 - 75, height // 2 + 50, 150, 50)
    button_color = (0, 128, 0)  # Green button
    button_text = "Start Camera"
    font = pygame.font.Font(None, 36)

    # Welcome Screen
    welcome_text = font.render("Welcome! Red Light Green Light", True, (255, 255, 255))
    text_rect = welcome_text.get_rect(center=(width // 2, height // 2 - 50))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
                if button_rect.collidepoint(event.pos):
                    game_started = True
                    red_light = random.choice([True, False]) # Randomize initial light

        if not game_started:
            screen.fill((0, 0, 0))  # Black background
            screen.blit(welcome_text, text_rect)
            pygame.draw.rect(screen, button_color, button_rect)
            button_text_render = font.render(button_text, True, (255, 255, 255))
            button_text_rect = button_text_render.get_rect(center=button_rect.center)
            screen.blit(button_text_render, button_text_rect)
            pygame.display.flip()
            continue

        # Capture next frame
        ret, frame2 = cap.read()
        if not ret:
            break

        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

        # Calculate difference between frames
        diff = cv2.absdiff(gray1, gray2)
        thresh = cv2.threshold(diff, sensitivity, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < min_area:
                continue
            motion_detected = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if motion_detected and red_light:
            print("Motion Detected during Red Light!")
            #Game over condition here, or some punishment.
            game_started = False;
            win = False;
        elif not motion_detected and red_light:
            win = True;
        # Convert OpenCV frame to Pygame surface
        frame_rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        frame_rgb = np.rot90(frame_rgb)
        frame_rgb = np.flipud(frame_rgb)
        frame_surface = pygame.surfarray.make_surface(frame_rgb)

        # Display frame
        screen.blit(frame_surface, (0, 0))

        #Display Red or green circle.
        if red_light:
            pygame.draw.circle(screen, (255,0,0), (50,50), 25)
        else:
            pygame.draw.circle(screen, (0,255,0), (50,50), 25)

        if win:
          win_text = font.render("You Win!", True, (0,255,0))
          win_rect = win_text.get_rect(center = (width//2, 50))
          screen.blit(win_text, win_rect)

        pygame.display.flip()

        # Update previous frame
        gray1 = gray2.copy()

        #Change lights every 30 seconds.
        if pygame.time.get_ticks() % 30000 == 0: #Change light every 30 seconds.
          red_light = random.choice([True, False])
          win = False;

    # Release resources
    cap.release()
    pygame.quit()

if __name__ == "__main__":
    motion_detection()