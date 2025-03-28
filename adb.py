import os
import time

PHONE_NUMBER = "8956514172"
AUDIO_FILE = "/sdcard/emergency_audio.wav"

def check_adb():
    """Check if the phone is connected via ADB"""
    devices = os.popen("adb devices").read()
    if "device" not in devices:
        print("No phone detected! Ensure USB Debugging is ON and connected.")
        exit(1)
    print("Phone connected successfully.")

def record_audio(duration=10):
    """Record audio using Termux"""
    print("Recording emergency audio on phone...")
    os.system(f"adb shell termux-microphone-record -d {duration} -f {AUDIO_FILE}")
    time.sleep(duration + 2)
    print("Audio saved on phone:", AUDIO_FILE)

def send_sms():
    """Send an emergency SMS"""
    message = "Emergency Alert! Audio recorded and saved."
    print("Sending emergency SMS...")
    os.system(f'adb shell termux-sms-send -n {PHONE_NUMBER} "{message}"')
    print("SMS sent to:", PHONE_NUMBER)

if __name__ == "__main__":
    check_adb()
    record_audio(10)
    send_sms()
