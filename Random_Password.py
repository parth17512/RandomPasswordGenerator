import os
import random
import string
import tkinter as tk
from tkinter import messagebox, ttk


def generate_password(length):
    """Generate a random password of specified length."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    
    # Ensure the password includes at least one character from each set
    char_sets = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "symbols": string.punctuation,
    }
    password = [
        random.choice(char_sets["lowercase"]),
        random.choice(char_sets["uppercase"]),
        random.choice(char_sets["digits"]),
        random.choice(char_sets["symbols"]),
    ]
    
    # Fill the remaining characters randomly
    all_chars = ''.join(char_sets.values())
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)


def generate_password_gui():
    """Handle password generation for the GUI."""
    try:
        length = int(password_length_var.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric length.")


def copy_password():
    """Copy the generated password to the clipboard."""
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Keeps the clipboard content
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy. Please generate one first.")


# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("600x400")  # Window dimensions
root.configure(bg="#f5f5f5")

# Apply styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 12, "bold"), background="#f5f5f5")
style.configure("TButton", font=("Segoe UI", 12, "bold"), background="#0078D7", foreground="white")
style.map("TButton", background=[("active", "#005a9e")])
style.configure("TEntry", font=("Segoe UI", 12))

# Variables
password_length_var = tk.StringVar(value="12")  # Default password length
password_var = tk.StringVar()

# Header
header_label = ttk.Label(
    root,
    text="Random Password Generator",
    font=("Segoe UI", 20, "bold"),
    background="#0078D7",
    foreground="white",
    anchor="center",
)
header_label.place(x=0, y=20, width=600, height=40)

# Password Length Input
length_label = ttk.Label(root, text="Password Length:")
length_label.place(x=50, y=100, width=200, height=30)

length_entry = ttk.Entry(root, textvariable=password_length_var, width=10)
length_entry.place(x=250, y=100, width=100, height=30)

# Generate Button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.place(x=50, y=150, width=300, height=40)

# Generated Password Display
password_label = ttk.Label(root, text="Generated Password:")
password_label.place(x=50, y=220, width=200, height=30)

password_entry = ttk.Entry(root, textvariable=password_var, width=50, state="readonly")
password_entry.place(x=250, y=220, width=300, height=30)

# Copy Password Button
copy_button = ttk.Button(root, text="Copy Password", command=copy_password)
copy_button.place(x=50, y=270, width=300, height=40)

# Mainloop
root.mainloop()
