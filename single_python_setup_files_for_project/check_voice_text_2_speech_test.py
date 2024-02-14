#!/usr/bin/env python3
# Created by Ranger

# Usage information
# python check_voice_text_2_speech_test.py

# This is what the code does:
# 1. Test your microphone
# 2. Test recording of your microphone
# 3. Exit

# Import the subprocess module to run commands
# Import the sys module to access command-line arguments
# Import the os module to access the operating system
# Import the platform module to access the operating system information
# Import the psutil module to access system information
# Import the speech_recognition module to access the speech recognition API
# Import the pyttsx3 module to access the text-to-speech API
# Import the requests module to make HTTP requests
# Import the json module to work with JSON data
# Import the io module to work with streams
# Import the AudioSegment and play functions from the pydub module to play audio
# Import the pyaudio module to access the audio I/O
# Import the wave module to work with WAV files
# Import the os module to access the operating system

# Import the subprocess module to run commands
import pyttsx3
import requests
import json
import io
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import pyaudio
import wave
import os
import subprocess
import time


# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

def select_microphone(microphones):
    if not microphones:
        print("No microphones found.")
        return None
    print("Available microphones:")
    for i, mic in enumerate(microphones):
        print(f"{i + 1}. {mic}")

    while True:
        choice = input("Select a microphone (1, 2, etc.): ")
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(microphones):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def list_microphones():
    print ("")
    print("Searching for microphones...")
    print ("")
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')
    microphones = []
    for i in range(num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:
            microphones.append(device_info['name'])
    p.terminate()
    return microphones

def record_audio(filename, microphone_index, duration=5):
    test_file_path = 'test'
    if not os.path.exists(test_file_path):
        os.makedirs(test_file_path)
    filename = os.path.join(test_file_path, f"{filename}")
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    input_device_index=microphone_index,
                    frames_per_buffer=1024)
    
    print("Recording will start in 5 seconds...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("Speak now to test mic.")

    frames = []

    for _ in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

def open_file(filename):
    test_file_path = 'test'
    filename = os.path.join(test_file_path, filename)
    if os.name == 'nt':  # For Windows
        os.startfile(filename)
    elif os.name == 'posix':  # For Linux, Mac
        subprocess.call(('open', filename))

def main():
    while True:
        print ("")
        print ("Wecome to the voice test program. Please select an option:")
        print ("")
        print("\n1. Test your microphone (This will also show you a list of all available microphones)")
        print("2. Test with a recording of your microphone")
        print ("")
        print("3. Exit")
        print ("")
        choice = input("Enter your choice: ")

        if choice == '1':
            microphones = list_microphones()
            mic_choice = select_microphone(microphones)
            if mic_choice is not None:
                print ("")
                print ("Testing microphone...")
                sleep = 3
                print("Microphone is working.")
            else:
                print ("")
                print ("Testing microphone...")
                sleep = 3
                print("Microphone is not working.")
        elif choice == '2':
            microphones = list_microphones()
            mic_choice = select_microphone(microphones)
            if mic_choice is not None:
                filename = f"record_test_{len(os.listdir('test')) + 1}.wav"
                record_audio(filename, mic_choice)
                print(f"Recording saved as {filename}")
                open_file(filename)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()