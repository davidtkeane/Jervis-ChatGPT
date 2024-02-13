#!/usr/bin/env python3
# Created by Ranger

# Usage information
# python elevenlabs-connection_test.py

# This is what the code does:
# 1. Test the connection to the Elevenlabs API
# 2. Play the audio response
# 3. Exit

# Import the subprocess module to run commands
import requests  # Import the requests library to make HTTP requests
import os  # Import os module to interact with the operating system

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

# Define the size of each chunk of data to write to the file as it is downloaded
CHUNK_SIZE = 1024  

# URL to the ElevenLabs text-to-speech API endpoint
url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID_HERE"

# Headers to be sent with the API request
headers = {
  "Accept": "audio/mpeg",  # Accepts audio in MPEG format from the server
  "Content-Type": "application/json",  # Data sent will be in JSON format
  "xi-api-key": "YOUR_OPENAI_API_KEY"  # Your ElevenLabs API key
}

# The data payload that contains the text to convert and the voice settings
data = {
  "text": "If you can hear this then you have made the connection!!",  # Text to be converted into speech
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,  # Stability setting for the voice synthesis
    "similarity_boost": 0.5  # Similarity boost setting for the voice synthesis
  }
}

# Send a POST request to the ElevenLabs API with the specified URL, headers, and data
response = requests.post(url, json=data, headers=headers)  

# Create a directory named 'test' if it doesn't exist to store the downloaded audio file
test_file_path = 'test'
if not os.path.exists(test_file_path):
    os.makedirs(test_file_path)

# Create the path for the new file including the directory and file name
filename = os.path.join(test_file_path, 'elevenlabs_test.mp3')

# Open the file in binary write mode and write chunks of data into the file
with open(filename, 'wb') as f:
  for chunk in response.iter_content(chunk_size=CHUNK_SIZE):  # Read the response in chunks
    if chunk:  # Check if the chunk has content
      f.write(chunk)  # Write the non-empty chunk to the file

# Open the downloaded .mp3 file in the default audio program and play it
if os.name == 'nt':  # If the operating system is Windows
  os.startfile(filename)  # Opens the file in the associated application
elif os.name == 'posix':  # If the operating system is Linux or macOS
  os.system('xdg-open ' + filename)  # Opens the file using the default app

print ("")
print('Connection to Elevenlabs successful!')  # Print a success message after playing the audio
