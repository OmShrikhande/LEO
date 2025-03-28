import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as input source
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    audio = recognizer.listen(source)  # Listen for speech

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)  # Using Google Speech Recognition
    
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Error with the speech recognition service.")
