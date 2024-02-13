

# 📝 Jervis-ChatGPT with ElevenLabs and MongoDB

This Python script is for a voice interface chatbot named Jervis. It uses OpenAI's GPT-3.5-turbo-instruct model to respond to user input. The user can interact with the chatbot through speech, and the chatbot responds with text and/or speech. The conversation can be saved as an MP3 file and emailed to a specified address. The conversation is also logged to a MongoDB database.


![PowerShell](https://img.shields.io/badge/-PowerShell-black?style=flat-square&logo=powershell)
![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/jervis-ChatGPT?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/jervis-ChatGPT?style=flat-square)

<p align="center">
  <img src="https://user-images.githubusercontent.com/49094051/227788148-a8ff8e06-86a4-41a6-aa53-8b7d6855360c.png"/>
  <span style=color:grey> <i>image by MidJourney AI </i> </span>
</p>

The script supports two types of voices: the local system's voice and a voice from ElevenLabs. The user can specify the voice, speech rate, and volume through command-line arguments. The script also supports sending the conversation via email and saving the conversation to an MP3 file.

The script uses several libraries, including pyttsx3 for text-to-speech, speech_recognition for speech-to-text, openai for the GPT-3.5-turbo-instruct model, pymongo for MongoDB interaction, and smtplib for sending emails.

The script logs errors and exceptions to a file and also logs the conversation history to a MongoDB database. The MongoDB connection details are fetched from environment variables.
The script also includes a function to send emails with an optional attachment, which can be used to send the conversation history as an MP3 file.
The script starts with a conversation loop where it listens for user input, processes the input, generates a response, and speaks the response. The conversation continues until the user says "goodbye".

#

