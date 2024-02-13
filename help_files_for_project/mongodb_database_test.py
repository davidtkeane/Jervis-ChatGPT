#!/usr/bin/env python3
# Created by Ranger

# This works on Windows only. It checks if Visual Studio Code is installed on the system.
# This is a Python script that connects to your MongoDB deployment using the PyMongo driver for testing a connection.

# Usage information
# python mongodb_test.py

# Information and instructions about the connection URI:
# The connection URI is used to connect to your MongoDB deployment. It contains the following information:
# Type of connection password is called Password (SCRAM)
# Replace the placeholder values with your own values and run the script using the following command: python mongodb_test.py
# You can get the connection URI from the Connect dialog in the Atlas UI. Make sure to replace myFirstDatabase with the name of the database that connection URI should connect to.

# This is what the code does:
# It connects to your MongoDB deployment using the PyMongo driver.
# The MongoClient class is used to create a new client and connect to the server.
# The ping command is used to confirm a successful connection.
# If the connection is successful, the script prints "Pinged your deployment. You successfully connected to MongoDB!".

# Import the MongoClient class from the pymongo package

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 1.0.0\n")

uri = "mongodb+srv://YOUR_MONGODB_URI_HERE"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

