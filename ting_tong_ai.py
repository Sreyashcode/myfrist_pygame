import pygame
import pyttsx3
import time

def speak(text, voice_id):
    """Speaks the given text using the specified voice."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)  # Set the voice
    engine.say(text)
    engine.runAndWait()

def main():
    """Main function to speak the facts and voicemail."""

    # Initialize Pygame for event handling (if you need it)
    pygame.init()

    # Initialize the TTS engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Choose a male voice (adjust index as needed)
    male_voice_id = 0  # Adjust if needed. You may have to iterate through voices to find the correct male voice.
    for index, voice in enumerate(voices):
        if voice.gender == 'VoiceGenderMale':
            male_voice_id = index
            break

    # Choose a female voice (adjust index as needed)
    female_voice_id = 1 #default female voice, adjust if needed.
    for index, voice in enumerate(voices):
        if voice.gender == 'VoiceGenderFemale':
            female_voice_id = index
            break

    # Speak the introduction
    speak("Hi Mahi, Adu. This is Ting Tong AI.", male_voice_id)

    # Facts about Mahi
    speak("Facts about Mahi. She is a 10 year old. She likes studying. She likes fish. She is a Bengali and Bihari origin. Speaks English and has a sweet little brother. Rides a BSA Butterfly cycle. Has an aunt Juli Masi. To know more, dial 100.", female_voice_id)

    # Facts about Adu
    speak("Facts about Adu. He is an 8 year old. Speaks English. Plays Roblox. To know more, dial 911 from Ama Adu Mahi association.", male_voice_id)

    # Voicemail from Sreyash
    speak("It is a voicemail from Sreyash. I will guide you how to find Sreyash. First, go to the kitchen. You will find a note. Read it and come back here.", male_voice_id)

    pygame.quit()

if __name__ == "__main__":
    main()