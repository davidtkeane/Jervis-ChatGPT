#!/usr/bin/env python3
# Created by Ranger

# This works on Windows only. 
# It checks if you can connect to the OpenAI API.
# This is a Python script that connects to your OpenAI API deployment for testing a connection.

# Usage information
# python openai_api_test.py

# What this script does:
# This script checks if the OpenAI API is working by sending a test request to the API.
# The script requires an active internet connection to connect to the OpenAI API.
# The script requires an OpenAI API key to authenticate the requests.
# The script uses the openai module to interact with the OpenAI API.
# The script uses the os module to get the OpenAI API key from the environment variables.
# The script uses the platform module to get the operating system information and architecture.
# The script uses the subprocess module to run shell commands and manage child processes.

# Import required modules
# The platform module provides an API for getting information about the operating system, including the name, release, and architecture.
# The subprocess module provides an API for running shell commands and managing child processes.
# The os module provides an API for interacting with the operating system, including file operations and environment variables.
# The requests module provides an API for making HTTP requests, including downloading files from the internet.

import openai
import os

os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 1.0.0\n")

model = "gpt-3.5-turbo-instruct"
prompt ="Create a function that takes a list of strings and returns the longest string in the list." # Replace with your prompt of choice

def setup_openai():
    openai.api_key = os.getenv('OPENAI_API_KEY') # Which is where you added the API key in the .env file.

def get_openai_response(model, prompt):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048,
        temperature=0.9
    )
    return response.choices[0].text.strip()

def ping_openai():
    try:
        openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt="You are a helpful assistant. ping"
        )
        print("")
        print("Connection to OpenAI successful")
        print("")
    except openai.error.AuthenticationError:
        print("API key is invalid or missing. Please check your API key.")
    except openai.error.APIError:
        print("Unable to connect to OpenAI. Please try again later.")

setup_openai()
response = get_openai_response(model, prompt)
ping_openai()
print(response)
