import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import sys

# JSON file name to save the EXE path
JSON_FILE = "ubisoft_path.json"

def load_saved_path():
    default_path = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\UplayWebCore.exe"
    if os.path.exists(default_path):
        return default_path
    """Loads the last saved file path"""
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("exe_path", "")
        except json.JSONDecodeError:
            return ""
    return ""

def save_path(exe_path):
    """Saves the selected file path, replacing the old one"""
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump({"exe_path": exe_path}, file, indent=4)

def modify_firewall(action):
    exe_path = exe_path_var.get().strip()

    if not exe_path or not os.path.isfile(exe_path):
        messagebox.showerror("Error", "Please select a valid .exe file.")
        return

    # Convert / to \ for Windows compatibility
    exe_path = exe_path.replace("/", "\\")

    # Save the new file path
    save_path(exe_path)

    # Unique rule name based on the file name
    rule_name = f"Firewall_{os.path.basename(exe_path)}"

    # Delete existing rules (incoming + outgoing)
    delete_command_in = f'netsh advfirewall firewall delete rule name="{rule_name}_IN"'
    delete_command_out = f'netsh advfirewall firewall delete rule name="{rule_name}_OUT"'

    try:
        subprocess.run(delete_command_in, shell=True, check=False)
        subprocess.run(delete_command_out, shell=True, check=False)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Warning: Unable to delete existing rules (maybe they don’t exist): {e}")

    # Add new rules (incoming + outgoing)
    exe_path_quoted = f'"{exe_path}"'

    if action == "allow":
        command_in = f'netsh advfirewall firewall add rule name="{rule_name}_IN" dir=in action=allow program={exe_path_quoted} enable=yes'
        command_out = f'netsh advfirewall firewall add rule name="{rule_name}_OUT" dir=out action=allow program={exe_path_quoted} enable=yes'
    elif action == "block":
        command_in = f'netsh advfirewall firewall add rule name="{rule_name}_IN" dir=in action=block program={exe_path_quoted} enable=yes'
        command_out = f'netsh advfirewall firewall add rule name="{rule_name}_OUT" dir=out action=block program={exe_path_quoted} enable=yes'
    else:
        messagebox.showerror("Error", "Invalid action.")
        return

    try:
        print(f"Adding rules:\n  - {command_in}\n  - {command_out}")
        subprocess.run(command_in, shell=True, check=True)
        subprocess.run(command_out, shell=True, check=True)
        messagebox.showinfo("Success", f"The program '{os.path.basename(exe_path)}' has been {action}ed (incoming and outgoing) in the firewall.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to modify the firewall: {e}")

def select_file():
    """Opens a file explorer and saves the selected path"""
    file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    if file_path:
        exe_path_var.set(file_path)

def get_icon_path():
    """Gère l'embarquement de l'icône dans l'exécutable"""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, "icon.ico")
    else:
        # Mode développement : chemin local
        return "icon.ico"
    
# Tkinter GUI
root = tk.Tk()
root.title("Ubisoft Offline Locker")
root.iconbitmap(get_icon_path())

# Load saved file path and pre-fill the input field
exe_path_var = tk.StringVar(value=load_saved_path())

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

tk.Label(frame, text='Select the "UplayWebCore.exe" file in the Ubisoft Connect installation folder', font=('Sans','9','bold')).pack()
tk.Entry(frame, textvariable=exe_path_var, width=50).pack()
tk.Button(frame, text="Browse files", command=select_file, background="#2563eb", fg="#ffffff", activebackground="#2563eb", activeforeground="#ffffff", font=('Sans','10','bold'), borderwidth="0", padx=10, pady=3).pack(pady=5)

tk.Button(frame, text="Allow connection", command=lambda: modify_firewall("allow"), background="#059669", fg="#ffffff", activebackground="#059669", activeforeground="#ffffff", font=('Sans','9','bold'), borderwidth="0", padx=10, pady=3).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Block connection", command=lambda: modify_firewall("block"), background="#dc2626", fg="#ffffff", activebackground="#dc2626", activeforeground="#ffffff", font=('Sans','9','bold'), borderwidth="0", padx=10, pady=3).pack(side=tk.RIGHT, padx=5)

root.mainloop()
