import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Create the main window
root = tk.Tk()
root.title("Ladies Empowerment Organization")
root.geometry("350x700")  # Mobile-like dimensions
root.configure(bg="#000000")

# Function to open index.py
def open_index():
    try:
        root.destroy()  # Destroy the main window if it exists
    except tk.TclError:
        pass  # Ignore if the window has already been destroyed
    os.system(f"python \"{os.path.abspath('index.py')}\"")

# Check if user_data.json exists at startup
if os.path.exists("user_data.json"):
    root.after(100, open_index)

def save_user_data():
    user_data = {
        "name": entry_name.get(),
        "aadhar": entry_aadhar.get(),
        "gender": gender_var.get(),
        "email": entry_email.get(),
        "family_contacts": [entry_contact1.get(), entry_contact2.get(), entry_contact3.get()],
        "pin": entry_pin.get()
    }

    # Validation checks
    if "" in user_data.values() or "" in user_data["family_contacts"]:
        messagebox.showerror("Error", "All fields are required!")
        return

    if not user_data["aadhar"].isdigit() or len(user_data["aadhar"]) != 12:
        messagebox.showerror("Error", "Aadhar number must be exactly 12 digits!")
        return

    if not user_data["pin"].isdigit() or len(user_data["pin"]) != 4:
        messagebox.showerror("Error", "PIN must be exactly 4 digits!")
        return

    for contact in user_data["family_contacts"]:
        if not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Error", "Each contact number must be exactly 10 digits!")
            return

    if "@" not in user_data["email"] or not user_data["email"].endswith((".com", ".org", ".net")):
        messagebox.showerror("Error", "Invalid email format!")
        return

    # Check if the user agreement checkbox is selected
    if not agreement_var.get():
        messagebox.showerror("Error", "You must accept the User Agreement to proceed!")
        return

    # Save data if all validations pass
    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)
    messagebox.showinfo("Success", "User information saved successfully!")
    open_index()

def open_user_info_window():
    global entry_name, entry_aadhar, gender_var, entry_email, entry_contact1, entry_contact2, entry_contact3, entry_pin, agreement_var
    root.destroy()
    
    user_info_window = tk.Tk()
    user_info_window.title("User Information")
    user_info_window.geometry("350x700")
    user_info_window.configure(bg="#000000")

    def create_entry(parent, label_text):
        frame = tk.Frame(parent, bg="#000000")
        tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), fg="#00ffcc", bg="#000000").pack(side="left", padx=5)
        entry = ttk.Entry(frame, width=25)
        entry.pack(side="left", padx=5)
        frame.pack(pady=10)
        return entry

    tk.Label(user_info_window, text="Enter Your Details", font=("Arial", 16, "bold"), fg="#00ffcc", bg="#000000").pack(pady=10)

    entry_name = create_entry(user_info_window, "Name:")
    entry_aadhar = create_entry(user_info_window, "Aadhar Card:")
    entry_pin = create_entry(user_info_window, "4-Digit PIN:")

    tk.Label(user_info_window, text="Gender:", font=("Arial", 10, "bold"), fg="#00ffcc", bg="#000000").pack(pady=10)
    
    gender_var = tk.StringVar(value="Male")
    gender_frame = tk.Frame(user_info_window, bg="#000000")
    ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left", padx=5)
    ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=5)
    ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left", padx=5)
    gender_frame.pack(pady=10)

    entry_email = create_entry(user_info_window, "Email:")
    entry_contact1 = create_entry(user_info_window, "Family Contact 1:")
    entry_contact2 = create_entry(user_info_window, "Family Contact 2:")
    entry_contact3 = create_entry(user_info_window, "Family Contact 3:")

    # Add User Agreement section
    agreement_text = (
        "By proceeding, you agree that the mic and camera will only be used in critical situations, "
        "not every time. This software does not harm any personal life or personal information. "
        "In case of misuse, you are eligible for legal action."
    )
    tk.Label(user_info_window, text=agreement_text, wraplength=300, font=("Arial", 8), fg="#ffffff", bg="#000000").pack(pady=10)
    agreement_var = tk.BooleanVar(value=False)
    tk.Checkbutton(user_info_window, text="I Agree", variable=agreement_var, bg="#000000", fg="#00ffcc", selectcolor="#000000").pack(pady=5)

    tk.Button(user_info_window, text="Save", command=save_user_data, bg="#00ffcc", fg="#000000",
              font=("Arial", 12, "bold"), padx=10, pady=5, relief="flat").pack(pady=15)

    user_info_window.mainloop()

# Welcome Screen
def animate_label(label, text, index=0):
    if index < len(text):
        label.config(text=label.cget("text") + text[index])
        root.after(100, animate_label, label, text, index + 1)

welcome_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#00ffcc", bg="#000000")
welcome_label.pack(pady=20)
animate_label(welcome_label, "Welcome to LEO!")

tk.Label(root, text="Please enter your details before proceeding.", fg="#00ffcc", bg="#000000").pack(pady=10)
ttk.Button(root, text="Enter Details", command=open_user_info_window).pack(pady=20)

root.mainloop()
