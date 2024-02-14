#!/usr/bin/env python3

# Created by Ranger (Feb 2024)
# Title: ChatGPT Voice Interface
# Version: 2.0

# Description: This is a simple chatbot that uses the OpenAI gpt-3.5-turbo-instruct model to respond to user input.
# This is jervis.py file for the ChatGPT Voice Interface program.

# Installation instructions:

# Read the README.md file for more information on how to use the program.
# You will have to sign up to Prerequisites for keys, ID@s and API keys, see below and README.txt.
# Read the extra files in the help_files folder for helps on connecting to MongoDB and Gmail.
# Read the file in the help_files folder called singel_python_setup_files_for_project.md. 
    # This file has extra setup information on the different parts from Mongodb, Gmail, Elevenlabs.
    # I added as much details as I can to help setting up each section as easy as possible. 

# Read the other instructions in the code for more information on how to use the program in the instructions folder.

# Files required to run the program located in help_files_for_project folder.
# Read the help_files_for_project folder for the required files to run the program.
# Read the .env file for the environment variables required to run the program.
# Read the requirements.txt file inside the instructions folder to install the required libraries and versions to run the program.
# There is a setup guide for Gmail and MongoDB Atlas in the instructions folder.
# There is a file called jervis_project_creation_stages.md that outlines the stages of the project creation. Use this as a guide to create your own project.
# There is a file called instructions_help_files_for_project_explained.md that explains the help files for the project in the folder help_files_for_project.

# 3 ways to install the required libraries to run the program:
# Option 1: Install using the requirements.txt file for the required libraries and versions to run the program. 
# pip install -r requirements.txt
# Option 2: Run the install_jervis.bat file to install the required libraries and versions to run the program. 
# install_jervis.bat
# Option 3: Run the install_jervis.py file to install the required libraries and versions to run the program. 
# python install_jervis.py

# Prerequisites:

# You will have to sign up to.
# OpenAI - https://platform.openai.com/ - This has a small charge everytime, but 5 USD lasts me a month with normal usage, if you go mad, it can get expensive.
# MongoDB Online Database - https://www.mongodb.com/ - This is free
# ElevenLabs - https://elevenlabs.io/ - There is a free version with voices or pay and clone your own to use.
# Gmail - https://www.google.com/gmail/ - This is free
# You will need to get API keys and Voice Id and put them into the .env file
# Just replace Your with your info. Leave the structure the way it is, just replace the Your sections.
# In the test files, you will have to enter the API''s manually, as there is no .env key in this folder and the scripts do not look for this file to check for private information.
# Once all the test files are working and all API info entered into the .env file, we are ready to rumble.

# Description:

# What the script does:
# This is a simple chatbot that uses the OpenAI gpt-3.5-turbo-instruct model to respond to user input. 
# This can be changed to any other model if necessary. Code may need to be modified to handle different models.
# The user can speak to the chatbot and the chatbot will respond with text and/or speech.
# The user can also save the conversation to an MP3 file and email the conversation to a specified email address.
# The conversation is also logged to a MongoDB database.
# The user can specify the voice to use (either "local" or "elevenlabs") and the speech rate and volume.
# The user can also specify whether to save the conversation to an MP3 file and whether to email the conversation.
# The user can also specify whether to show the welcome message.
# The user can also specify whether to show the help message.
# The user can also specify whether to show the version message.

# Usage information after gathering the required files API's and ID's and install of environment variables:
# Within the folder run the main.py file using these 'Switches' to control the program. Examples Below.

# Switches:

# --welcome: Show welcome message
# --voice: Voice to use ("local" or "elevenlabs")
# --rate: Speech rate (words per minute)
# --volume: Speech volume (0.0 to 1.0)
# --save: Save conversation to an MP3 file
# --email-n: Do not email the conversation
# --help: Show help message
# --version: Show version message

# Examples:

# "python main.py --voice elevenlabs" or "python main.py --voice local --save --email-n" 
#  This will save the conversation to an MP3 file and won't email the conversation to a specified email address.

# "python main.py --voice elevenlabs" or "python main.py --voice local --save" 
#  This will use the local computers voice and save the conversation to an MP3 file and email the conversation to a specified email address.

# "python main.py --voice elevenlabs" or "python main.py --voice local" 
#  This will use the local computers voice and won't save the conversation to an MP3 file and will email the conversation to a specified email address.

# "python main.py --voice elevenlabs" or "python main.py --voice elevenlabs"
#  This will use the ElevenLabs voice and won't save the conversation to an MP3 file and will email the conversation to a specified email address.

# "python main.py --help"
#  This will display the help message.


# Import the required libraries
import pyttsx3
import speech_recognition as sr
import openai
import datetime
import os
import argparse
import json
import requests
import sys
import io
import time
import logging
import smtplib
import re

from time import sleep
from tqdm import tqdm
from pydub import AudioSegment
from pydub.playback import play
from speech_recognition import Recognizer, RequestError, UnknownValueError
from alive_progress import alive_bar
from colorama import Fore, Style
from termcolor import colored
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from pydub import AudioSegment
from pydub.playback import play
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pymongo.mongo_client import MongoClient

load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv('OPENAI_API_KEY')

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Check if the directory exists, and if not, create it
# log_dir = 'C:\\Users\\david\\OneDrive\\Documents\\WindowsPowerShell\\Scripts\\rgpt\\elevenlabs\\log'
log_dir = 'log' 
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging configuration
log_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
log_file = os.path.join(log_dir, 'error.log')

# Create a custom logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.ERROR)

# Create handlers
handler = logging.StreamHandler()
error_handler = logging.FileHandler(log_file)

# Set formatter for handlers
handler.setFormatter(log_formatter)
error_handler.setFormatter(log_formatter)

# Add handlers to the logger
logger.addHandler(handler)
logger.addHandler(error_handler)

# Welcome Banner
print ("")
print("Processing...............")
print ("")
sleep(2.02) 
print("Welcome to the ChatGPT Voice Interface!")
print("This is Version 2.0")
print ("")
print(colored("Created by David", 'green'))
sleep(2.02) 
for i in tqdm(range(100), ncols=80, bar_format='{l_bar}{bar}|'):
    sleep(0.02)  # simulate a download

# print(sys.path)

# Create the ArgumentParser object
parser = argparse.ArgumentParser(
    prog='Your Program Name',
    usage='%(prog)s [options]',
    description='''
    ChatGPT with ElevenLabs Voice.    
    Copyright (C) 2023.
    Developed by Ranger.
    ''',
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

# Parse arguments
parser.add_argument('--welcome', action='store_true', help='Show welcome message')
parser.add_argument('--voice', type=str, default='local', help='Voice to use ("local" or "elevenlabs")')
parser.add_argument('--rate', type=int, default=150, help='Speech rate (words per minute)')
parser.add_argument('--volume', type=float, default=0.8, help='Speech volume (0.0 to 1.0)')
parser.add_argument('--save', action='store_true', help='Save conversation to an MP3 file')
parser.add_argument('--email-n', action='store_true', help='Do not email the conversation')
args = parser.parse_args()

print(f"Voice argument received: {args.voice}")  # Add this line

# Display welcome banner if --welcome switch is used
if args.welcome:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("                     Hello and welcome to the chat app!")
    print('+-------------------------------------------------------------------------------+')
    print('| Openai-ElevenLabs. Copyright (C) 2023, Contact: rangersmyth.74@gmail.com      |')
    print('| Version: 1.0                                                                  |')
    print('|                                                                               |')
    print('| This program comes with ABSOLUTELY NO WARRANTY.                               |')
    print('| This is free software, and you are welcome to redistribute it.                |')
    print('+-------------------------------------------------------------------------------+')

try:
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Display welcome banner
    if args.voice:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("                     Hello and welcome to the chat app!")
        print('+-------------------------------------------------------------------------------+')
        print('| Openai-ElevenLabs. Copyright (C) 2023, Contact: rangersmyth.74@gmail.com      |')
        print('| Version: 1.0                                                                  |')
        print('|                                                                               |')
        print('| This program comes with ABSOLUTELY NO WARRANTY.                               |')
        print('| This is free software, and you are welcome to redistribute it.                |')
        print('+-------------------------------------------------------------------------------+')

    print(f"Voice argument received: {args.voice}")

    CHUNK_SIZE = 1024

    # Define the ElevenLabs API details if necessary
    if args.voice == 'elevenlabs':
        url = os.getenv('ELEVENLABS_URL')
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": os.getenv('ELEVENLABS_API_KEY')
        }
        data = {
            "text": "",
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

    # Set up conversation variables
    conversation_history = ""
    user_name = "Ranger"
    bot_name = "Jervis"

    # Define the OpenAI GPT model
    model = "gpt-3.5-turbo-instruct"

    # Function to process and respond to user input
    def process_input(user_input):
        global conversation_history
        prompt = f"{user_name}: {user_input}\n{bot_name}: "
        conversation_history += prompt
        response = openai.Completion.create(
            engine=model,
            prompt=conversation_history,
            max_tokens=2048,
            temperature=0.9
        )
        response_text = response.choices[0].text.strip()
        conversation_history += response_text + "\n"
        print(f"{bot_name}: {response_text}")
        
        if args.voice == 'elevenlabs':
            data['text'] = response_text
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
            audio_data = response.content
            song = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
            play(song)
        else:
            engine.say(response_text)
            engine.runAndWait()
            audio_data = None  # No audio data when using pyttsx3
        log_conversation(user_input, response_text, audio_data)

    # Set the voice speed
    rate = engine.getProperty('rate')   # Getting current speed rate
    engine.setProperty('rate', 150)      # Setting up new voice rate. You can adjust the rate to your preference.

    # Set the voice volume
    volume = engine.getProperty('volume')   # Getting current volume level (0.0 to 1.0)
    engine.setProperty('volume', 0.8)       # Setting up volume level between 0.0 to 1.0

    # Initialize the speech recognizer and microphone
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Rest of your logging and conversation code follows here...
        
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')

    # Function to log the conversation to a text file
    def log_conversation(user_input, bot_response, audio_data=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log conversation to text file
        with open("chatgpt_voice.txt", "a", encoding='utf8') as f:
            f.write(f"{timestamp} {user_name}: {user_input}\n")
            f.write(f"{timestamp} {bot_name}: {bot_response}\n")

        # Save audio data if available and specified by the args
        if audio_data and args.save:
            folder_name = "mp3"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Replace whitespace with underscore in user_input for filename
            sanitized_input = re.sub(r'\s+', '_', user_input)
            filename = f"chatgpt_voice_{sanitized_input}.mp3"

            audio_file_path = os.path.join(folder_name, f"chatgpt_voice_{sanitized_input}.mp3")

            # Import AudioSegment and io modules above this method
            audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
            audio.export(os.path.join(folder_name, filename), format="mp3")

            if not args.email_n:
                send_email("Conversation", f"{user_name}: {user_input}\n{bot_name}: {bot_response}\n", "proxybusterburg@gmail.com", from_email=EMAIL_USER, from_password=EMAIL_PASS, attachment_path=audio_file_path)

        # Connect to MongoDB Atlas
        client = MongoClient(os.getenv('MONGO_DB_URI'))

        # Get a reference to a database
        db = client[os.getenv('MONGO_DB_NAME')]
        # Parse the line into a document

        # Prepare the document
        document = {
            "timestamp": timestamp,
            "user_name": user_name,
            "user_input": user_input,
            "bot_name": bot_name,
            "bot_response": bot_response,
        }

        # Insert the document into a collection
        collection_name = os.getenv('MONGO_DB_COLLECTION').split('.')[-1]
        db[collection_name].insert_one(document)

        
    # Modify the send_email function to handle attachments
    def send_email(subject, message_body, to_email, from_email=EMAIL_USER, from_password=EMAIL_PASS, attachment_path=None):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach message body directly
        msg.attach(MIMEText(message_body, 'plain'))

        # Attach the file if path is not None
        if attachment_path is not None:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()

    # Start the conversation loop
    engine.say("Ranger, you can ask a question now!")
    engine.runAndWait()
    print("🤖 Listening...")
    conversation_active = True
    while conversation_active:
        with mic as source:
            audio = r.listen(source)
            print("🤖 You can ask your question now...")
            print("")
            print("🤖 Computing your answer...")
            print("")
            print("🤖 Please wait...")
            print("")
        try:
            # Convert speech to text
            user_input = r.recognize_google(audio)
            print(f"{user_name}: {user_input}")
            
            # Handling the 'goodbye' command
            if user_input.lower() == "goodbye":
                print("Goodbye Ranger!")
                engine.say("Goodbye Ranger!")
                engine.runAndWait()

                engine.runAndWait()
                conversation_active = False
                
            elif user_input.lower() == "pause":
                seconds = input("How many seconds do you want to pause for? ")
                try:
                    seconds_int = int(seconds)
                    print(f"Pausing for {seconds_int} seconds... (Press space bar to resume)")
                    # Wait for the specified amount of time or until the space bar is pressed
                    for i in range(seconds_int):
                        if keyboard.is_pressed('space'):
                            print("Resuming now!")
                            break
                        time.sleep(1)  # Wait for 1 second at a time
                except ValueError:
                    print("Please enter a valid number.")
                print("Pause complete!")

            # Assuming that process_input is a defined function that handles the bot's response        
            process_input(user_input)
        
            # Prompt the user to continue the conversation
            bot_prompt = "Do you need another question answered ?"
            print(bot_prompt)
            engine.say(bot_prompt)  # speak the prompt using pyttsx3
            engine.runAndWait()

        except sr.UnknownValueError:
            # Handle unrecognized speech
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            # Handle API errors
            print("Could not request results; check your network connection.")
        except sr.UnknownValueError:
            # If speech is unintelligible, print a message and prompt the user to try again
            print("I'm sorry Ranger, I didn't understand what you said. Please try again.")
        except sr.RequestError as e:
            # If there's an issue with the speech recognizer, print an error message
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print("Exception occurred: {0}".format(e))
        pass

        # To test the error logging, you can raise an exception:
        # raise ValueError("This is a test error")

except Exception as e:
    logger.error("Exception occurred", exc_info=True)

def print_welcome_banner():
    print("")
    print("\033[34m" + "***********************************************")
    print("*                  Made with Love             *             ")
    print("***********************************************" + "\033[0m")
print_welcome_banner()

print("")
print("")

def print_colored_banner():
    print("\033[34m" +
    """
            ____  ___    _   __________________       _____ __  _____  __________  __
           / __ \/   |  / | / / ____/ ____/ __ \     / ___//  |/  /\ \/ /_  __/ / / /
          / /_/ / /| | /  |/ / / __/ __/ / /_/ /_____\__ \/ /|_/ /  \  / / / / /_/ /
         / _, _/ ___ |/ /|  / /_/ / /___/ _, _/_____/__/ / /  / /   / / / / / __  /
        /_/ |_/_/  |_/_/ |_/\____/_____/_/ |_|     /____/_/  /_/   /_/ /_/ /_/ /_/
        
""" + "\033[0m")
print_colored_banner()