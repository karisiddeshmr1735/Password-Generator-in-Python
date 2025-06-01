project : Password Generator in Python
                                                                                                                                                                                                                  import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator(tk.Tk):
    def _init_(self):
        super()._init_()

        self.title("Password Generator")
        self.geometry("400x300")
        self.configure(bg="#f4f4f4")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
        title.pack(pady=15)

        # Frame for options
        options_frame = tk.Frame(self, bg="#f4f4f4")
        options_frame.pack(pady=10, padx=20, fill="x")

        # Password Length
        length_label = tk.Label(options_frame, text="Length:", font=("Arial", 12), bg="#f4f4f4")
        length_label.grid(row=0, column=0, sticky="w")
        self.length_var = tk.IntVar(value=12)
        length_spinbox = tk.Spinbox(options_frame, from_=4, to=64, textvariable=self.length_var, font=("Arial", 12), width=5)
        length_spinbox.grid(row=0, column=1, sticky="w")

        # Checkboxes for character sets
        self.upper_var = tk.IntVar(value=1)
        self.lower_var = tk.IntVar(value=1)
        self.digits_var = tk.IntVar(value=1)
        self.special_var = tk.IntVar(value=1)

        upper_cb = tk.Checkbutton(options_frame, text="Include Uppercase (A-Z)", variable=self.upper_var, bg="#f4f4f4", font=("Arial", 12))
        upper_cb.grid(row=1, column=0, columnspan=2, sticky="w", pady=2)

        lower_cb = tk.Checkbutton(options_frame, text="Include Lowercase (a-z)", variable=self.lower_var, bg="#f4f4f4", font=("Arial", 12))
        lower_cb.grid(row=2, column=0, columnspan=2, sticky="w", pady=2)

        digits_cb = tk.Checkbutton(options_frame, text="Include Numbers (0-9)", variable=self.digits_var, bg="#f4f4f4", font=("Arial", 12))
        digits_cb.grid(row=3, column=0, columnspan=2, sticky="w", pady=2)

        special_cb = tk.Checkbutton(options_frame, text="Include Special Characters", variable=self.special_var, bg="#f4f4f4", font=("Arial", 12))
        special_cb.grid(row=4, column=0, columnspan=2, sticky="w", pady=2)

        # Generate Button
        generate_btn = tk.Button(self, text="Generate Password", command=self.generate_password, font=("Arial", 12), bg="#007acc", fg="white")
        generate_btn.pack(pady=15, ipadx=10, ipady=5)

        # Result Label and Entry
        result_frame = tk.Frame(self, bg="#f4f4f4")
        result_frame.pack(padx=20, fill="x")

        self.password_var = tk.StringVar()
        password_entry = tk.Entry(result_frame, textvariable=self.password_var, font=("Consolas", 14), state="readonly")
        password_entry.pack(side="left", fill="x", expand=True)

        copy_btn = tk.Button(result_frame, text="Copy", command=self.copy_to_clipboard, font=("Arial", 12), bg="#28a745", fg="white")
        copy_btn.pack(side="left", padx=10)

    def generate_password(self):
        length = self.length_var.get()
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length must be at least 4 characters.")
            return

        char_sets = []
        if self.upper_var.get():
            char_sets.append(string.ascii_uppercase)
        if self.lower_var.get():
            char_sets.append(string.ascii_lowercase)
        if self.digits_var.get():
            char_sets.append(string.digits)
        if self.special_var.get():
            char_sets.append(string.punctuation)

        if not char_sets:
            messagebox.showwarning("No Characters Selected", "Please select at least one character type.")
            return

        # Ensure at least one char from each selected set
        password_chars = [random.choice(char_set) for char_set in char_sets]

        # Fill remaining length with random chars from all sets combined
        all_chars = ''.join(char_sets)
        password_chars += random.choices(all_chars, k=length - len(password_chars))

        # Shuffle final password
        random.shuffle(password_chars)

        password = ''.join(password_chars)
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if _name_ == "_main_":
    app = PasswordGenerator()
    app.mainloop()
