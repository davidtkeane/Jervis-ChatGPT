#!/usr/bin/env python3
# Created by Ranger

# This works on Windows only. It checks if Visual Studio Code is installed on the system.
# This is a Python script that connects to your MongoDB deployment using the PyMongo driver for testing a connection.

# Usage information
# python powershell_installed_check.py
# This script checks if PowerShell is installed on the system. If not, it downloads and installs the latest version of PowerShell.
# The script works on Windows only.
# The script requires an active internet connection to download the PowerShell installer.
# The script requires administrative privileges to install PowerShell.
# The script uses the requests module to download the PowerShell installer.
# The script uses the subprocess module to run PowerShell commands and install the PowerShell installer.
# The script uses the platform module to get the operating system information and architecture.
# The script uses the os module to remove the downloaded PowerShell installer after installation.


# Import required modules
# The platform module provides an API for getting information about the operating system, including the name, release, and architecture.
# The subprocess module provides an API for running shell commands and managing child processes.
# The os module provides an API for interacting with the operating system, including file operations and environment variables.
# The requests module provides an API for making HTTP requests, including downloading files from the internet.

import platform
import subprocess
import os
import requests

# Clear the console for better readability of the program's output
os.system('cls' if os.name == 'nt' else 'clear') 
# Print welcome banner
print("")
print("Made By David")
print("Version 1.0.0")
print("")

# Function to check if PowerShell is installed
def is_powershell_installed():
    try:
        subprocess.run(["powershell", "-Command", "$PSVersionTable.PSVersion"], check=True, stdout=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

# Function to get Windows architecture and download the appropriate PowerShell version
def download_and_install_powershell(architecture):
    base_url = "https://github.com/PowerShell/PowerShell/releases/download/v7.4.1/"
    file_name = ""
    if architecture == '32bit':
        file_name = "PowerShell-7.4.1-win-x86.msi"
    else:
        file_name = "PowerShell-7.4.1-win-x64.msi"
    
    download_url = base_url + file_name
    local_file_path = file_name
    
    print(f"Downloading PowerShell {file_name}...")
    response = requests.get(download_url)

    if response.status_code == 200:
        with open(local_file_path, 'wb') as file:
            file.write(response.content)
        
        print("Installing PowerShell...")
        subprocess.run(["msiexec.exe", "/i", local_file_path, "/quiet"], check=True)
        os.remove(local_file_path)
        print("Installation complete.")
    else:
        print("Failed to download the PowerShell installer.")

# Main function
def main():
    os_info = platform.system() + " " + platform.release()
    architecture = platform.architecture()[0]
    print(f"You are running {os_info} {architecture} operating system.")

    if not is_powershell_installed():
        user_input = input("PowerShell is not installed. Do you want to install it? (Y/N): ").strip().upper()
        if user_input == "Y":
            download_and_install_powershell(architecture)
        elif user_input == "N":
            print("Installation canceled by the user.")
    else:
        print("PowerShell is already installed.")
        # Add additional logic if needed to check and update PowerShell version

if __name__ == "__main__":
    main()
