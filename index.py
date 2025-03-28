import tkinter as tk
from tkinter import font
import subprocess
import time

def emergency_action():
    print("🚨 Emergency SOS Activated! 🚨")
    subprocess.Popen(["python", "whatsaap.py"])
    time.sleep(10)  # Wait for 10 seconds before starting the next process
    subprocess.Popen(["python", "sender.py"])
   

def toggle_mode():
    global dark_mode
    root.configure(bg="#000000")
    title_label.configure(bg="#000000", fg="#00ffcc")
    subtitle_label.configure(bg="#000000", fg="#cccccc")
    emergency_btn.configure(bg="#ff0033", fg="#ffffff", activebackground="#cc0022")
    instruction_label.configure(bg="#000000", fg="#cccccc")
    methods_frame.configure(bg="#111111")
    methods_label.configure(bg="#111111", fg="#00ffcc")
    for label in method_labels:
        label.configure(bg="#111111", fg="#cccccc")
    mode_btn.configure(text="Dark Mode Enabled", bg="#00ffcc", fg="#000000", activebackground="#009977")
    dark_mode = True

# Create the main window
root = tk.Tk()
root.title("SafeGuard")
root.geometry("350x700")  # Mobile-like dimensions
root.configure(bg="#000000")

dark_mode = True  # Ensure dark mode is enabled by default

# Title label
title_font = font.Font(family="Arial", size=18, weight="bold")
title_label = tk.Label(root, text="Welcome to SafeGuard", font=title_font, bg="#000000", fg="#00ffcc")
title_label.pack(pady=(20, 5))

# Subtitle label
subtitle_label = tk.Label(root, text="Your personal safety companion. Stay protected with our advanced safety features.", wraplength=300, bg="#000000", fg="#cccccc", font=("Arial", 10))
subtitle_label.pack(pady=(0, 20))

# Emergency Button
btn_font = font.Font(size=16, weight="bold")
emergency_btn = tk.Button(root, text="🚨 Emergency SOS 🚨", font=btn_font, fg="white", bg="#ff0033", padx=30, pady=15, borderwidth=3, relief="raised", cursor="hand2", activebackground="#cc0022", activeforeground="white", command=emergency_action)
emergency_btn.pack(pady=15)

# Instruction label
instruction_label = tk.Label(root, text="Press in case of emergency to alert contacts and authorities", wraplength=300, bg="#000000", fg="#cccccc", font=("Arial", 10, "italic"))
instruction_label.pack(pady=(0, 20))

# Activation Methods section
methods_frame = tk.Frame(root, bg="#111111", padx=20, pady=10, relief="groove", borderwidth=2)
methods_label = tk.Label(methods_frame, text="Activation Methods", font=("Arial", 12, "bold"), bg="#111111", fg="#00ffcc", anchor="center")
methods_label.pack(fill="x", pady=5)

methods = [
    "📱 Shake your phone rapidly",
    "🎙️ Say your code word: \"Help me\"",
    "🔘 Press power button 5 times"
]

method_labels = []
for method in methods:
    label = tk.Label(methods_frame, text=method, bg="#111111", fg="#cccccc", font=("Arial", 10), anchor="w", justify="left")
    label.pack(fill="x", pady=3)
    method_labels.append(label)

methods_frame.pack(pady=10, fill="x", padx=20)

# Dark mode toggle button
mode_btn = tk.Button(root, text="Dark Mode Enabled", font=("Arial", 12, "bold"), bg="#00ffcc", fg="#000000", padx=10, pady=5, cursor="hand2", activebackground="#009977", command=toggle_mode)
mode_btn.pack(pady=10)

toggle_mode()  # Apply dark mode after all widgets are created

# Run the application
root.mainloop()