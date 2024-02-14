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

# 🆘 Help on Install:

## ⚾ Installation Help Files:

<p> 1. Read the files in the <b>help_files</b> folder before hammering away to make this script work! Use the files in the <b>singel_python_setup_files_for_project</b> and use these one at a time to get working first, once all files work and return 'connection established' then you are ready to go, remember to add all keys to the .env file</p>

<p>2. This is the **README.md** file to provide more information on how to use the program. You will have to sign up to Prerequisites for keys, ID's and API keys, see below for more details.</p>

<p>3. Read the extra help files in the **help_files** folder for help with connecting to MongoDB and Gmail. The file **singel_python_setup_files_for_project.md** has extra setup information on the different parts from Mongo, Gmal, Elevenlabs, it can help you to connect to each service and test connection to Gmail, Elevenlabs and MongoDB if you have the correct API keys.</p>

<p>4. Add the keys to the .env file insdie the folder **singel_python_setup_files_for_project** and leave the structure as it is.</p>

<p>Read the other instructions in the <b>help_files</b> for more information on how to use the program.</p>

## 💻 Modules Installation instructions:

<ol>
  <p>3 ways to install the required libraries to run the program:</p>
  <li>Option 1: Install using the requirements.txt file for the required libraries and versions to run the program. <code>pip install -r requirements.txt</code></li>
  <li>Option 2: Run the install_jervis.bat file to install the required libraries and versions to run the program. <code>install_jervis.bat</code></li>
  <li>Option 3: Run the install_jervis.py file to install the required libraries and versions to run the program. <code>python install_jervis.py</code></li>
  <li> All modules listed below will be installed with either of the 3 files</li>
</ol

## 🍔 Pip Modules to Install

1. pyttsx3
2. speech_recognition
3. openai
4. requests
5. pymongo
6. pydub
7. pyaudio
8. wave

## 🥷Prerequisites:

### 🏀 Signup to Gmail, Elevenlabs, MongDB:

<p>There are instsructions in the <b>help_files</b> folder and the file called <b># Jervis Install instructions in more detail.md</b> will have more detailed instructions on how to connect to gmail and mongdb

<p>You will have to sign up to:</p>

<ul>
  <li>OpenAI - <a href="https://platform.openai.com/">https://platform.openai.com/</a> - This has a small charge everytime, but 5 USD lasts me a month with normal usage, if you go mad, it can get expensive.</li>
  <li>MongoDB Online Database - <a href="https://www.mongodb.com/">https://www.mongodb.com/</a> - This is free</li>
  <li>ElevenLabs - <a href="https://elevenlabs.io/">https://elevenlabs.io/</a> - There is a free version with voices or pay and clone your own to use.</li>
  <li>Gmail - <a href="https://www.google.com/gmail/">https://www.google.com/gmail/</a> - This is free</li>
</ul>

<p>You will need to get API keys and Voice Id and put them into the .env file. Just replace Your with your info. Leave the structure the way it is, just replace the Your sections. In the test files, you will have to enter the API''s manually, as there is no .env key in this folder and the scripts do not look for this file to check for private information. Once all the test files are working and all API info entered into the .env file, we are ready to rumble.</p>

# 🚀 Installation Steps

1. Clone this repository to your local machine using `git clone <repo-link>`.
2. Go to the folder you have the github project saved and enter it.
3. Next we install the modules for the script to work.
4. Install the modules pip install -m requirements.txt
5. python install_jervis.py
6. install_jervis.bat
7. Now signup or sign back into Prerequisites.
8. Once you have all the required keys, then move on to testing them with the scripts i made in the `<b>`singel_python_setup_files_for_project `</b>` folder.
9. Go into the folder `<b>`singel_python_setup_files_for_project `</b>` and go through each one to test your connection is established and working, if you have your api keys, then you don't have to do this.
10. Add all keys to the .env file inside the `<b>`singel_python_setup_files_for_project `</b>` folder as you go along.
11. Once you have tested all the files, and added the keys and stuff into the .env file.
12. Copy the .env file into the main folder `<b>jervis_ChatGPT</b>` then we are ready to run the jervis.py

# 📖 Usage of --switches

## Examples:

<h2>Command Switches:</h2>

<table>
  <tr>
    <th>Switch</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>--welcome</td>
    <td>Show welcome message</td>
  </tr>
  <tr>
    <td>--voice</td>
    <td>Voice to use ("local" or "elevenlabs")</td>
  </tr>
  <tr>
    <td>--rate</td>
    <td>Speech rate (words per minute)</td>
  </tr>
  <tr>
    <td>--volume</td>
    <td>Speech volume (0.0 to 1.0)</td>
  </tr>
  <tr>
    <td>--save</td>
    <td>Save conversation to an MP3 file</td>
  </tr>
  <tr>
    <td>--email-n</td>
    <td>Do not email the conversation</td>
  </tr>
  <tr>
    <td>--help</td>
    <td>Show help message</td>
  </tr>
  <tr>
    <td>--version</td>
    <td>Show version message</td>
  </tr>
</table>

<h2>Command Examples:</h2>

<ul>
  <li><code>python main.py --voice elevenlabs</code> or <code>python main.py --voice local --save --email-n</code> - This will save the conversation to an MP3 file and won't email the conversation to a specified email address.</li>
  <li><code>python main.py --voice elevenlabs</code> or <code>python main.py --voice local --save</code> - This will use the local computers voice and save the conversation to an MP3 file and email the conversation to a specified email address.</li>
  <li><code>python main.py --voice elevenlabs</code> or <code>python main.py --voice local</code> - This will use the local computers voice and won't save the conversation to an MP3 file and will email the conversation to a specified email address.</li>
  <li><code>python main.py --voice elevenlabs</code> or <code>python main.py --voice elevenlabs</code> - This will use the ElevenLabs voice and won't save the conversation to an MP3 file and will email the conversation to a specified email address.</li>
  <li><code>python main.py --help</code> - This will display the help message.</li>
</ul>
