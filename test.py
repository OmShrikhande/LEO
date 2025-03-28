import speech_recognition as sr
from twilio.rest import Client
from location import get_location
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Twilio credentials (Replace with actual credentials)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = "424389cd565b9c74f9794a0a525379eb"
twilio_number = "+17755743807"  # Your Twilio phone number
emergency_number = "+918766535742"  # Number to call

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, auth_token)

# Load victim's name from user data JSON file
with open("user_data.json", "r") as file:
    user_data = json.load(file)
victim_name = user_data.get("name", "Unknown")  # Default to "Unknown" if name is missing

# Get location
location = get_location()

recognizer = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_sphinx(audio)  # Offline speech recognition
            print("You said:", text)
            handle_emergency(text)  # Pass recognized text to emergency handler
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Could not process the audio.")

def handle_emergency(recognized_text):
    """Handle emergency by sending SMS or making a call."""
    try:
        # Send SMS
        message = client.messages.create(
            body=f"Emergency Alert! My name is {victim_name}. I said: '{recognized_text}'. I am at {location}.",
            from_=twilio_number,
            to=emergency_number
        )
        print(f"🚨 SMS sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")
        # If SMS fails, make an emergency call
        make_emergency_call(recognized_text)

def make_emergency_call(recognized_text):
    """Function to make an emergency call with a critical female voice in English."""
    try:
        twiml_message = f"""
            <Response>
                <Say voice="female" language="en-US">
                    This is an emergency call. My name is {victim_name}. 
                    I said: '{recognized_text}'. I am currently at {location}. 
                    Please send help immediately.
                </Say>
                <Pause length="3"/>
                <Say voice="female" language="en-US">
                    We have also sent an audio and video file to your email. 
                    Please take immediate action.
                </Say>
            </Response>
        """

        call = client.calls.create(
            to=emergency_number,
            from_=twilio_number,
            twiml=twiml_message.strip()  # Ensuring clean XML formatting
        )

        print(f"🚨 Emergency call initiated! Call SID: {call.sid}")

    except Exception as e:
        print(f"❌ Error initiating the call: {e}")

# Run speech-to-text
speech_to_text()