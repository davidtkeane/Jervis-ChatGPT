# Jervis Install instructions in more detail 

## The README.md has the basic instructions on how to install and other information required, but sometime they don't add the little things to get the project working as they expect people to know what they are doing, and I don't!! 

Here is information about each file and what it does, the modules needed for it to work, and it should help to understand what your doing, like me, I am new this to programming game.

## instructions for the test python files.

## About the files and folder and what they mean.

The files in the folder help_files_for_project are there for you to sign-up to the option like OpenAI and the others one by one, so you can collect the tokens, id's and API keys. Then enter the keys into the .env file inside the help_files_for_project.

You can then test each script and get it to works for you, there will be a notification saying connection established.

If this is your first time learning about python then using Google's Gemini, ChatGPT, then when you are successful, you can add the API key and other information needed to file the .env file.

[https://platform.openai.com/]()
[https://chat.openai.com/]()
[https://gemini.google.com/app]()
[https://www.mongodb.com/]()
[https://elevenlabs.io/]()
[https://myaccount.google.com/]()

The .env files is there to protect users passwords and others so the script if copied can't use your keys, as someone might run up your bill by accident. 

1. These files can be used to test each function on your computer before the main.py script runs
2. To install the modules needed run the requirements.txt file. pip install -r requirements.txt
3. You can also install the modules using the file install_jervis.py
4. You will most likely have module errors, do not fear, they just need to be installed.
5. pip install module name should do it, as I could have missed one when making this.
6. If you feel like it you can use the files in the help_files_for_project to test each function the main script uses.
7. The Main script is long, so testing each function before hand will save time.

## You will have to sign up to these sites to combine the script.

9. Powershell Newist Release - https://github.com/PowerShell/PowerShell/releases/tag/v7.4.1
10. OpenAI - https://platform.openai.com/ - This has a small charge everytime, but 5 USD lasts me a month with normal usage, if you go mad, it can get expensive.
11. MongoDB Online Database - https://www.mongodb.com/ - This is free
12. ElevenLabs - https://elevenlabs.io/ - There is a free version with voices or pay and clone your own to use.
13. You will need to get API keys and Voice Id and put them into the .env file
14. Just replace Your with your info. Leave the structure the way it is, just replace the Your sections.
15. In the test files, you will have to enter the API''s manually, as there is no .env key in this folder and the scripts do not look for this file to check for private information.
16. Once all the test files are working and all API info entered into the .env file, we are ready to rumble.
16. Gmail - https://www.google.com/gmail/ - This is free

# Testing and Setting up Gmail.

## Setting up Gmail to allow unsecure apps to use googles system.

Google won't allow regular passwords to be used on scripts like this die to security so they have another way called an App Password. This is needed for the script to email you the transcript and audio recordings.

1. This is easy to setup, it might take a few minutes as google has lots of pages and options.
2. To use Gmail's SMTP server, you need to generate an App Password. 
3. This is a 16-character password that you provide instead of your regular email password. 
4. This provides a more secure login.

Here are the steps to generate an App Password:

1. Go to your Google Account.
2. Select Security.
3. Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because:
   - 2-Step Verification is not set up for your account.
   - 2-Step Verification is only set up for security keys.
   - Your account is through work, school, or other organization.
   - You turned on Advanced Protection.
4. At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
5. Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
6. Select Done.

Once you have generated the App Password, you can use it in your script where you need to provide the Gmail password.

Remember, do not share this App Password with anyone else. Google will never ask for this information.

## python gmail.py

### Output expected on the terminal.

The options given.

Enter the recipient's email address: Add here the email you want to send to
Enter your Gmail address: Your email address 
Enter your Gmail password: The none secure password is needed here
Enter your subject: This is the New Subject my friend!!!
Enter your message: How are you doing?

Email sent successfully.

### What this script does: 

1. Sends emails from the terminal to someone
2. This the code break down
3. Modify the send_email function to handle attachments.
4. The script requires an active internet connection to send the email.
5. The script requires a Gmail address and password to send the email.

6. Import required modules
7. The os module provides an API for interacting with the operating system, including file operations and environment variables.
8. The smtplib module provides an API for sending emails using the Simple Mail Transfer Protocol (SMTP).
9. The email.mime.multipart module provides an API for creating MIME objects for sending emails with attachments.
10. The email.mime.text module provides an API for creating MIME objects for sending plain text emails.
11. The email.mime.base module provides an API for creating MIME objects for sending emails with attachments.
12. The email module provides an API for creating and sending emails.

# Modules for checking files Explained.

## Checks is Visual Code is installed

### python vs_code_install_check.py

1. Import the subprocess module to run the command line.
2. The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
3. The check_call function runs the command described by args. It will raise a CalledProcessError if the return code is non-zero.
4. The FileNotFoundError exception is raised when a file or directory is requested but cannot be found.
5. The is_vscode_installed function checks if Visual Studio Code is installed on the system.
6. It uses the subprocess module to run the code.cmd --version command.
7. If the command is successful, the function returns True. Otherwise, it returns False.
8. The if __name__ == "__main__": block is used to check if the script is being run directly.
9. If the script is run directly, it calls the is_vscode_installed function and prints the result.
10. If Visual Studio Code is installed, it prints "Visual Studio Code is installed." Otherwise, it prints "Visual Studio Code is not installed."
11. You can use this script to check if Visual Studio Code is installed on a Windows system.
12. If you want to check for other operating systems, you may need to modify the script to use different commands or paths.

## Checks if the BurntToast module is installed

### python check_burnt_toast_module.py

1. Check if the BurntToast module is installed.
2. Usage information: python check_burnt_toast_module.py.
3. The script checks if the BurntToast module is installed.
4. The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
5. The run function runs the command described by args. It will raise a CalledProcessError if the return code is non-zero.
6. The check_burnt_toast_module function checks if the BurntToast module is installed.
7. It uses the subprocess module to run the Get-Module -ListAvailable -Name BurntToast command.
8. If the BurntToast module is not installed, the function asks the user if they want to install it.
9. If the user chooses to install the module, the function runs the Install-Module -Name BurntToast -Scope CurrentUser -Force -Confirm:$false command.
10. If the user chooses not to install the module, the function prints "Installation canceled by the user."
11. If the BurntToast module is already installed, the function prints "BurntToast module is already installed."
12. The if __name__ == "__main__": block is used to check if the script is being run directly.
13. If the script is run directly, it calls the check_burnt_toast_module function.
14. You can use this script to check if the BurntToast module is installed on a Windows system.
15. If you want to check for other operating systems, you may need to modify the script to use different commands or paths.

## Checks if Visual Studio Code is installed on the system.

### python powershell_installed_check.py

1. Run the script with: python powershell_installed_check.py.
2. This script checks if PowerShell is installed on the system. If not, it downloads and installs the latest version of PowerShell.
3. The script works on Windows only.
4. The script requires an active internet connection to download the PowerShell installer.
5. The script requires administrative privileges to install PowerShell.
6. The script uses the requests module to download the PowerShell installer.
7. The script uses the subprocess module to run PowerShell commands and install the PowerShell installer.
8. The script uses the platform module to get the operating system information and architecture.
9. The script uses the os module to remove the downloaded PowerShell installer after installation.
10. Import required modules.
11. The platform module provides an API for getting information about the operating system, including the name, release, and architecture.
12. The subprocess module provides an API for running shell commands and managing child processes.
13. The os module provides an API for interacting with the operating system, including file operations and environment variables.
14. The requests module provides an API for making HTTP requests, including downloading files from the internet.

## Checks if you can connect to the OpenAI API.

### python openai_api_test.py

1. Usage information: python openai_api_test.py.
2. This script checks if the OpenAI API is working by sending a test request to the API.
3. The script requires an active internet connection to connect to the OpenAI API.
4. The script requires an OpenAI API key to authenticate the requests.
5. The script uses the openai module to interact with the OpenAI API.
6. The script uses the os module to get the OpenAI API key from the environment variables.
7. The script uses the platform module to get the operating system information and architecture.
8. The script uses the subprocess module to run shell commands and manage child processes.
9. Import required modules.
10. The platform module provides an API for getting information about the operating system, including the name, release, and architecture.
11. The subprocess module provides an API for running shell commands and managing child processes.
12. The os module provides an API for interacting with the operating system, including file operations and environment variables.
13. The requests module provides an API for making HTTP requests, including downloading files from the internet.

## This script checks if Python and Anaconda are installed and offers to install or update them if necessary.

### which_python_conda_check.py

Verify Python and pip versions
Upgrade Python and pip to their latest versions (if possible)
Install Python if it's not found
Offer to install Anaconda if Python is not installed
Check if there are updates for Anaconda or Miniconda

1. Run the script with: python which_python_conda_check.py.
2. This script checks if Python and Anaconda are installed and offers to install or update them if necessary.
3. It also checks for pip and offers to upgrade it if it's installed.
4. The script is written in Python and should work on Windows, macOS, and Linux.
5. The run_command function executes a command and returns its output.
6. The check_command function verifies if a command exists.
7. The get_version function gets the version of a program.
8. The upgrade_packages function attempts to upgrade pip and python packages to the latest versions using pip.
9. The offer_python_installation function prompts the user to install Python if it's not present.
10. The offer_anaconda_installation function prompts the user to install Anaconda if desired.
11. The main function checks installations and offers updates or installs.
12. The if __name__ == '__main__': block is used to check if the script is being run directly.
13. If the script is run directly, it calls the main function.
14. Import the subprocess module to run commands.
15. Import the sys module to access command-line arguments.
16. Import the os module to access the operating system.
17. Import the platform module to access the operating system information.
18. Import the psutil module to access system information.

## This script checks if you can create a file in a specific directory.

### python file_creation_test.py

Set the path for the file to be written to.
test_file_path = 'test_write.txt'

1. Run the script with: python file_creation_test.py.
2. This script checks if you can create a file in a specific directory.
3. The script is written in Python and should work on Windows, macOS, and Linux.
4. This is a test script to check file writing capabilities.
5. The script checks if a file can be created in a specific directory.
6. If the file can be created, it prints a success message.
7. If the file cannot be created, it prints a permission error message.

## This script checks if you can connect to ElevenLabs

### python elevenlabs-connection_test.py

2. This is what the code does:
3. Test the connection to the Elevenlabs API
4. Play the audio response
5. Exit
6. Import the requests module to make HTTP requests
7. Import the os module to access the operating system

## This script checks and tests your microphone with a sample recording.

### python check_voice_text_2_speech_test.py

1. python check_voice_text_2_speech_test.py
2. This is what the code does:
3. Test your microphone
4. Test recording of your microphone
5. Exit
6. Import the subprocess module to run commands
7. Import the sys module to access command-line arguments
8. Import the os module to access the operating system
9. Import the platform module to access the operating system information
10. Import the psutil module to access system information
11. Import the speech_recognition module to access the speech recognition API
12. Import the pyttsx3 module to access the text-to-speech API
13. Import the requests module to make HTTP requests
14. Import the json module to work with JSON data
15. Import the io module to work with streams
16. Import the AudioSegment and play functions from the pydub module to play audio
17. Import the pyaudio module to access the audio I/O
18. Import the wave module to work with WAV files
19. Import the os module to access the operating system

## This script checks if FontConfig is installed

### python check_voice_text_2_speech_test.py

1. python fontconfig.py
2. What this script does:
3. Check the operating system and set the Fontconfig directory accordingly.
4. Print a message if Fontconfig is installed or not installed.
5. The script uses the os module to run shell commands and manage child processes.
6. The script uses the platform module to get the operating system information.