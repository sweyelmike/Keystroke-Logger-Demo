import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

key_logs = []

def save_json():
    with open("logs.json", "w") as f:
        json.dump(key_logs, f, indent=4)

def save_txt(log):
    with open("logs.txt", "a") as f:
        f.write(log + "\n")

def key_pressed(event):
    log = {
        "Key": event.keysym,
        "Action": "Pressed",
        "Time": datetime.now().strftime("%H:%M:%S")
    }
    key_logs.append(log)
    save_json()
    save_txt(str(log))

def key_released(event):
    log = {
        "Key": event.keysym,
        "Action": "Released",
        "Time": datetime.now().strftime("%H:%M:%S")
    }
    key_logs.append(log)
    save_json()
    save_txt(str(log))

def start_logging():
    messagebox.showinfo(
        "Information",
        "Keystroke logging started.\nOnly keys typed inside this box are logged."
    )
    entry.focus()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Keystroke Logging Demonstration")
root.geometry("600x400")
root.configure(bg="#f2f2f2")

title = tk.Label(
    root,
    text="Keystroke Logging Demonstration",
    font=("Verdana", 16, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=10)

warning = tk.Label(
    root,
    text="⚠ Educational & Ethical Use Only",
    fg="red",
    bg="#f2f2f2",
    font=("Arial", 10, "bold")
)
warning.pack()

entry = tk.Entry(root, width=45, font=("Arial", 12))
entry.pack(pady=20)

entry.bind("<KeyPress>", key_pressed)
entry.bind("<KeyRelease>", key_released)

btn = tk.Button(
    root,
    text="Start Logging",
    command=start_logging,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
)
btn.pack(pady=10)

root.mainloop()
