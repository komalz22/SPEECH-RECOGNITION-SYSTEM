import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# Set up the GPIO pin (e.g., controlling an LED on GPIO 18)
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech and execute commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Please say a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognizing speech using Google Web Speech API (can be replaced with offline libraries)
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")

        # Example commands to control devices
        if "turn on the light" in command:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Light turned ON")
        elif "turn off the light" in command:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("Light turned OFF")
        else:
            print("Command not recognized")

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

# Main loop to keep listening
try:
    while True:
        listen_for_commands()
        time.sleep(2)

except KeyboardInterrupt:
    print("Program terminated.")
    GPIO.cleanup()