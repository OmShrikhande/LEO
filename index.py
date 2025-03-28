import tkinter as tk
from tkinter import font
from tkinter import ttk
import subprocess
import time
import json
from tkinter import simpledialog
from tkinter import messagebox

def emergency_action():
    print("🚨 Emergency SOS Activated! 🚨")
    messagebox.showinfo("Process Started", "Emergency SOS process has been activated.")
    subprocess.Popen(["python", "whatsaap.py"])
    time.sleep(10)  # Wait for 10 seconds before starting the next process
    subprocess.Popen(["python", "sender.py"])

def abort_process():
    try:
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
            stored_pin = user_data.get("pin")
        
        entered_pin = simpledialog.askstring("Abort Process", "Enter your 4-digit PIN:")
        if entered_pin == stored_pin:
            print("✅ Process aborted successfully.")
            messagebox.showinfo("Process Terminated", "Emergency SOS process has been terminated.")
            # Logic to cancel the process (if applicable)
        else:
            print("❌ Incorrect PIN. Process not aborted.")
            messagebox.showerror("Error", "Incorrect PIN. Process not aborted.")
    except FileNotFoundError:
        print("❌ user_data.json not found. Cannot verify PIN.")
        messagebox.showerror("Error", "user_data.json not found. Cannot verify PIN.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

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
    dark_mode = True

def animate_button(button):
    def grow():
        button.config(width=20)
        button.after(100, shrink)

    def shrink():
        button.config(width=15)

    grow()

# Create the main window
root = tk.Tk()
root.title("LEO")
root.geometry("400x750")  # Slightly larger dimensions for better spacing
root.configure(bg="#000000")

dark_mode = True  # Ensure dark mode is enabled by default

# Title label
title_font = font.Font(family="Arial", size=20, weight="bold")
title_label = tk.Label(root, text="Welcome to SafeGuard", font=title_font, bg="#000000", fg="#00ffcc")
title_label.pack(pady=(30, 10))

# Subtitle label
subtitle_label = tk.Label(root, text="Your personal safety companion. Stay protected with our advanced safety features.", wraplength=350, bg="#000000", fg="#cccccc", font=("Arial", 11))
subtitle_label.pack(pady=(0, 30))

# Emergency Button with animation and rounded corners
btn_font = font.Font(size=16, weight="bold")
emergency_btn = tk.Button(root, text="🚨 Emergency SOS 🚨", font=btn_font, fg="white", bg="#ff0033", padx=30, pady=15, borderwidth=0, relief="raised", cursor="hand2", activebackground="#cc0022", activeforeground="white", command=lambda: [emergency_action(), animate_button(emergency_btn)])
emergency_btn.pack(pady=20)
emergency_btn.configure(highlightbackground="#ff0033", highlightthickness=2)

# Instruction label
instruction_label = tk.Label(root, text="Press in case of emergency to alert contacts and authorities", wraplength=350, bg="#000000", fg="#cccccc", font=("Arial", 10, "italic"))
instruction_label.pack(pady=(0, 30))

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

methods_frame.pack(pady=20, fill="x", padx=30)

# Abort process button with rounded corners
abort_btn = tk.Button(root, text="Abort Process", font=("Arial", 12, "bold"), bg="#ffcc00", fg="#000000", padx=10, pady=5, cursor="hand2", activebackground="#ffaa00", borderwidth=0, command=abort_process)
abort_btn.pack(pady=20)
abort_btn.configure(highlightbackground="#ffcc00", highlightthickness=2)

toggle_mode()  # Apply dark mode after all widgets are created

# Run the application
root.mainloop()