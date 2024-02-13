#!/usr/bin/env python3
# Created by Ranger

# Usage information
# python file_creation_test.py

# This is what the code does:
# This script checks if you can create a file in a specific directory.
# The script is written in Python and should work on Windows, macOS, and Linux.
# Test script to check file writing capabilities
# The script checks if a file can be created in a specific directory
# If the file can be created, it prints a success message
# If the file cannot be created, it prints a permission error message

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")


# Set the path for the file to be written to.
test_file_path = 'test/test_write.txt'

# Attempt to open and write to the file inside a try block to catch any permission-related errors.
try:
    # Open the file specified by test_file_path in write mode ('w').
    with open(test_file_path, 'w') as test_file:
        # Write a string to the file.
        test_file.write("Testing write permissions.")
    # If the file write is successful, print a confirmation message.
    print(f"File written to successfully: {test_file_path}")

# Catch any PermissionError that occurs during the file write operation.
except PermissionError as e:
    # Print a permission error message along with the exception details.
    print(f"Permission error: {e}")
