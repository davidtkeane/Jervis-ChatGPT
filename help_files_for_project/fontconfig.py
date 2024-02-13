#!/usr/bin/env python3
# Created by Ranger

# Usage information
# python fontconfig.py

# What this script does:
# Check the operating system and set the Fontconfig directory accordingly.
# Print a message if Fontconfig is installed or not installed.
# The script uses the os module to run shell commands and manage child processes.
# The script uses the platform module to get the operating system information.

# Import required modules
import os
import platform

os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 1.0.0\n")

# Check the operating system and set the Fontconfig directory accordingly
if platform.system() == 'Windows':
    FONTCFG_DIR = r"C:\Users\david\fontconfig"
elif platform.system() == 'Linux':
    FONTCFG_DIR = '/etc/fonts/'
else:
    FONTCFG_DIR = None

if FONTCFG_DIR and os.path.exists(FONTCFG_DIR):
    print("Fontconfig is installed.")
else:
    print("Fontconfig is not installed.")
    if platform.system() == 'Windows':
        print("To install Fontconfig on Windows, you can use a package manager like Cygwin or MSYS2.")
    elif platform.system() == 'Linux':
        print("To install Fontconfig on Linux, you can use a package manager like apt or yum. For example: sudo apt install fontconfig")
print("\n")