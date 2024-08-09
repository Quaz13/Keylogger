# Overview:
This project is a simple keylogger written in Python using the pynput library. The keylogger captures and logs every keystroke made on the keyboard and saves them to a log file. Additionally, on macOS, the terminal window is minimized automatically when the script is launched, making it less conspicuous.

# Features:
Keystroke Logging: Captures all keystrokes and saves them to a log file (Keylogger.log).  

Minimizes Terminal Window (macOS): Automatically minimizes the terminal window upon script execution, making the keylogger run discreetly in the background.
# Requirements
Python 3.x

pynput library
# Installation
1. Clone the repository or download the source code.
2. Install the required Python library using pip:
pip install pynput
3. Run the keylogger script: python3 keylogger.py

# Usage
The keylogger will start capturing keystrokes as soon as it's executed.
On macOS, the terminal window will be minimized automatically after the script starts running.
Press the ESC key to stop the keylogger.

# Log File
The captured keystrokes are saved to Keylogger.log in the same directory as the script.
# Disclaimer
This software is intended for educational purposes only. Unauthorized use of this software for malicious purposes is illegal and unethical. The author is not responsible for any misuse of this software.
