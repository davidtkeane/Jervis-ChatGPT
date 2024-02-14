# 📝 Jervis-ChatGPT with ElevenLabs and MongoDB

This Python script is for a voice interface chatbot named Jervis. It uses OpenAI's GPT-3.5-turbo-instruct model to respond to user input. The user can interact with the chatbot through speech, and the chatbot responds with text and/or speech. The conversation can be saved as an MP3 file and emailed to a specified address. The conversation is also logged to a MongoDB database.

![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)
![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/jervis-ChatGPT?style=flat-square)

<p align="center">
  <img src="https://user-images.githubusercontent.com/49094051/227788148-a8ff8e06-86a4-41a6-aa53-8b7d6855360c.png"/>
  <br>
  <i>Image by MidJourney AI</i>
  <br>
  <a href="https://github.com/gia-guar/JARVIS-ChatGPT/tree/main">This is the URL to the image</a>
  <br>
  This is another version of Jervis called Jarvis by Gia-Guar, similar but a little different
</p>

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=for-the-badge)

# 🧐 About:

The script supports two types of voices: the local system's voice and a voice from ElevenLabs. The user can specify the voice, speech rate, and volume through command-line arguments. The script also supports sending the conversation via email and saving the conversation to an MP3 file.

The script uses several libraries, including pyttsx3 for text-to-speech, speech_recognition for speech-to-text, openai for the GPT-3.5-turbo-instruct model, pymongo for MongoDB interaction, and smtplib for sending emails.

The script logs errors and exceptions to a file and also logs the conversation history to a MongoDB database. The MongoDB connection details are fetched from environment variables.

The script also includes a function to send emails with an optional attachment, which can be used to send the conversation history as an MP3 file.

The script starts with a conversation loop where it listens for user input, processes the input, generates a response, and speaks the response. The conversation continues until the user says "goodbye".

## 🍔 Advanced Summary:

The script continues with MongoDB integration for storing conversation logs, modifying the send_email function to use environment variables for email credentials and to handle attachments. It then enters a conversation loop, using speech recognition to convert user speech to text and processing it. The script handles various commands and exceptions, including a 'goodbye' command to end the conversation. It also includes error handling and logging, with the capability to test error logging by raising an exception.

The script initializes environment variables, sets up logging, and configures a speech engine. It includes an argument parser for command-line options and integrates with OpenAI and ElevenLabs APIs for voice synthesis. The script also contains a function to process user input using GPT, handle voice output (either through ElevenLabs or pyttsx3), and log conversations. Email credentials are retrieved from environment variables, and a function to log conversations and save audio data is defined. The script is prepared to handle text-to-speech, speech recognition, and email functionalities, with provisions for command-line arguments to customize behaviour.

The script continues with MongoDB integration for storing conversation logs, modifying the `send_email` function to use environment variables for email credentials and to handle attachments. It then enters a conversation loop, using speech recognition to convert user speech to text and processing it. The script handles various commands and exceptions, including a 'goodbye' command to end the conversation. It also includes error handling and logging, with the capability to test error logging by raising an exception.

# 🆘 Help

## ⚾ Installation Help Files:

<p>This is the <b>README.md</b> file to provide more information on how to use the program. You will have to sign up to Prerequisites for keys, ID's and API keys, see below for more details.</p>
<p></p>
<p>Read the extra help files in the <b>help_files</b> folder for help with connecting to MongoDB and Gmail. The file <b>singel_python_setup_files_for_project.md</b> has extra setup information on the different parts from Mongo, Gmal, Elevenlabs, it can help you to connect to each service and test connection to Gmail, Elevenlabs and MongoDB if you have the correct API keys.</p>
<p></p>
<p> Add the keys to the .env file insdie the folder <b>singel_python_setup_files_for_project</b> and leave the structure as it is.</p>
<p> One file might need you to add you key to the top of the script, but also add it to the .env file as the jervis.py reads all keys from the .env file in the main section</b>
<p></p>
<p> I added as much details as I can to help setting up each section as easy as possible.</p>

<p>Read the other instructions in the <b>help_files</b> for more information on how to use the program.</p>

## 💻 Modules Installation instructions:

<ol>
  <p>3 ways to install the required libraries to run the program:</p>
  <li>Option 1: Install using the requirements.txt file for the required libraries and versions to run the program. <code>pip install -r requirements.txt</code></li>
  <li>Option 2: Run the install_jervis.bat file to install the required libraries and versions to run the program. <code>install_jervis.bat</code></li>
  <li>Option 3: Run the install_jervis.py file to install the required libraries and versions to run the program. <code>python install_jervis.py</code></li>
</ol>

## 🚀 Installation Steps

1. Clone this repository to your local machine using `git clone <repo-link>`.
2. 
3.
