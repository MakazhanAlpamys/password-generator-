
import tkinter as tk
from tkinter import ttk
import random
import string

def generate_passwords():
    password_length = int(spin_length.get())
    num_passwords = int(spin_count.get())
    characters = ""
    if var_digits.get():
        characters += string.digits
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_symbols.get():
        characters += "!@#$%^&*()"
    
    passwords = []
    for _ in range(num_passwords):
        password = "".join(random.choice(characters) for _ in range(password_length))
        passwords.append(password)
    
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, "\n".join(passwords))

root = tk.Tk()
root.title("Купия сөз генераторы")
root.geometry("500x400")

frame_options = tk.LabelFrame(root, text="Параметрлер")
frame_options.pack(pady=10)

tk.Label(frame_options, text="Құпия сөздің ұзындығы:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin_length = tk.Spinbox(frame_options, from_=4, to=32, width=5)
spin_length.grid(row=0, column=1, padx=5, pady=5)
spin_length.delete(0, tk.END)
spin_length.insert(0, 12)  

tk.Label(frame_options, text="Құпия сөздер саны:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
spin_count = tk.Spinbox(frame_options, from_=1, to=20, width=5)
spin_count.grid(row=1, column=1, padx=5, pady=5)
spin_count.delete(0, tk.END)
spin_count.insert(0, 5)  

frame_characters = tk.LabelFrame(root, text="Символдар")
frame_characters.pack(pady=10)

var_digits = tk.BooleanVar(value=True)
var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

check_digits = tk.Checkbutton(frame_characters, text="0-9", variable=var_digits)
check_digits.grid(row=0, column=0, padx=5, pady=5, sticky="w")
check_uppercase = tk.Checkbutton(frame_characters, text="A-Z", variable=var_uppercase)
check_uppercase.grid(row=1, column=0, padx=5, pady=5, sticky="w")
check_lowercase = tk.Checkbutton(frame_characters, text="a-z", variable=var_lowercase)
check_lowercase.grid(row=0, column=1, padx=5, pady=5, sticky="w")
check_symbols = tk.Checkbutton(frame_characters, text="!@#$%^&*", variable=var_symbols)
check_symbols.grid(row=1, column=1, padx=5, pady=5, sticky="w")

generate_button = tk.Button(root, text="Құпия сөздерді жасау", command=generate_passwords)
generate_button.pack(pady=10)

text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=10)

root.mainloop()
