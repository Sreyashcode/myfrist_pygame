import pygame
import cv2
import numpy as np

def motion_beep(camera_index=0, sensitivity=30, min_area=500, beep_frequency=440, beep_duration=500):
    """
    Detects motion using a connected camera and plays a beep sound when motion is detected.

    Args:
        camera_index (int): Index of the camera to use.
        sensitivity (int): Threshold for motion detection.
        min_area (int): Minimum area of detected motion.
        beep_frequency (int): Frequency of the beep sound in Hz.
        beep_duration (int): Duration of the beep sound in milliseconds.
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
    pygame.display.set_caption("Motion Beep")

    # Initialize sound
    pygame.mixer.init()
    beep_sound = pygame.mixer.Sound(pygame.mixer.Sound(np.sin(np.arange(44100 * beep_duration / 1000) * beep_frequency * 2 * np.pi / 44100).astype(np.float32)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        if motion_detected:
            print("Motion Detected!")
            beep_sound.play()

        # Convert OpenCV frame to Pygame surface
        frame_rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        frame_rgb = np.rot90(frame_rgb)
        frame_rgb = np.flipud(frame_rgb)
        frame_surface = pygame.surfarray.make_surface(frame_rgb)

        # Display frame
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()

        # Update previous frame
        gray1 = gray2.copy()

    # Release resources
    cap.release()
    pygame.quit()

if __name__ == "__main__":
    motion_beep()