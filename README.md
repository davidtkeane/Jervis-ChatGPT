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

## Advanced Summary:

The script continues with MongoDB integration for storing conversation logs, modifying the send_email function to use environment variables for email credentials and to handle attachments. It then enters a conversation loop, using speech recognition to convert user speech to text and processing it. The script handles various commands and exceptions, including a 'goodbye' command to end the conversation. It also includes error handling and logging, with the capability to test error logging by raising an exception.

The script initializes environment variables, sets up logging, and configures a speech engine. It includes an argument parser for command-line options and integrates with OpenAI and ElevenLabs APIs for voice synthesis. The script also contains a function to process user input using GPT, handle voice output (either through ElevenLabs or pyttsx3), and log conversations. Email credentials are retrieved from environment variables, and a function to log conversations and save audio data is defined. The script is prepared to handle text-to-speech, speech recognition, and email functionalities, with provisions for command-line arguments to customize behaviour.

The script continues with MongoDB integration for storing conversation logs, modifying the `send_email` function to use environment variables for email credentials and to handle attachments. It then enters a conversation loop, using speech recognition to convert user speech to text and processing it. The script handles various commands and exceptions, including a 'goodbye' command to end the conversation. It also includes error handling and logging, with the capability to test error logging by raising an exception.

🆘 Help

<h2>Installation instructions:</h2>

<p>Read the <b>README.md</b> file for more information on how to use the program. You will have to sign up to Prerequisites for keys, ID@s and API keys, see below and README.txt. Read the extra files in the <b>help_files</b> folder for helps on connecting to MongoDB and Gmail. Read the file in the <b>help_files</b> folder called <b>singel_python_setup_files_for_project.md</b>. This file has extra setup information on the different parts from Mongo, Gmal, Elevenlabs. I added as much details as I can to help setting up each section as easy as possible.</p>

<p>Read the other instructions in the code for more information on how to use the program in the instructions folder.</p>

<h2>Files required to run the program located in help_files_for_project folder:</h2>

<p>Read the <b>help_files_for_project</b> folder for the required files to run the program. Read the <b>.env</b> file for the environment variables required to run the program. Read the <b>requirements.txt</b> file inside the instructions folder to install the required libraries and versions to run the program. There is a setup guide for Gmail and MongoDB Atlas in the instructions folder. There is a file called <b>jervis_project_creation_stages.md</b> that outlines the stages of the project creation. Use this as a guide to create your own project. There is a file called <b>instructions_help_files_for_project_explained.md</b> that explains the help files for the project in the folder help_files_for_project.</p>

<h2>3 ways to install the required libraries to run the program:</h2>

<ol>
  <li>Option 1: Install using the requirements.txt file for the required libraries and versions to run the program. <code>pip install -r requirements.txt</code></li>
  <li>Option 2: Run the install_jervis.bat file to install the required libraries and versions to run the program. <code>install_jervis.bat</code></li>
  <li>Option 3: Run the install_jervis.py file to install the required libraries and versions to run the program. <code>python install_jervis.py</code></li>
</ol>

<ol>
  <li>chatbot</li>
  <li>voice-interface</li>
  <li>openai</li>
  <li>gpt-3.5-turbo</li>
  <li>python</li>
  <li>speech-recognition</li>
  <li>text-to-speech</li>
  <li>mongodb</li>
  <li>email</li>
  <li>mp3</li>
  <li>pyttsx3</li>
  <li>argparse</li>
  <li>logging</li>
  <li>dotenv</li>
  <li>pymongo</li>
  <li>smtplib</li>
  <li>elevenlabs</li>
  <li>speech-to-text</li>
  <li>audio-processing</li>
  <li>api-integration</li>
</ol>
