import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Generator")
        self.saved_passwords = []

        # Create the purpose label and entry
        self.purpose_label = tk.Label(self.root, text="Purpose:")
        self.purpose_label.grid(row=0, column=0, padx=5, pady=5)
        self.purpose_entry = tk.Entry(self.root, width=50)
        self.purpose_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create the length label and entry
        self.length_label = tk.Label(self.root, text="Length:")
        self.length_label.grid(row=1, column=0, padx=5, pady=5)
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create the generate button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_and_save_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Create the password label
        self.password_label = tk.Label(self.root, text="")
        self.password_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Create the saved passwords button
        self.saved_passwords_button = tk.Button(self.root, text="Saved Passwords", command=self.display_saved_passwords)
        self.saved_passwords_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Start the GUI event loop
        self.root.mainloop()

    def generate_password(self, length):
        """
        Generate a strong password with a mix of uppercase letters, lowercase letters, special characters, and numbers.
        
        Args:
            length (int): The length of the password.
        
        Returns:
            str: The generated password.
        """
        # Define the character sets
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        special_characters = string.punctuation
        numbers = string.digits
        
        # Combine the character sets
        all_characters = uppercase_letters + lowercase_letters + special_characters + numbers
        
        # Ensure the password includes at least one character from each set
        password = [
            random.choice(uppercase_letters),
            random.choice(lowercase_letters),
            random.choice(special_characters),
            random.choice(numbers),
        ]
        
        # Fill the rest of the password with random characters
        for _ in range(length - 4):
            password.append(random.choice(all_characters))
        
        # Shuffle the password to avoid the first characters always being in the same character set order
        random.shuffle(password)
        
        # Join the password into a single string
        return ''.join(password)

    def generate_and_save_password(self):
        # Get the purpose and password length from the GUI
        purpose = self.purpose_entry.get()
        length = int(self.length_entry.get() or 7)
        
        # Ensure the password length is at least 7
        if length < 7:
            messagebox.showerror("Error", "Password length must be at least 7.")
            return
        
        # Generate the password
        password = self.generate_password(length)
        
        # Save the password
        self.saved_passwords.append({'purpose': purpose, 'password': password})
        
        # Display the generated password
        self.password_label.config(text=f"Generated password: {password}")

    def display_saved_passwords(self):
        # Create a new window to display the saved passwords
        saved_passwords_window = tk.Toplevel(self.root)
        saved_passwords_window.title("Saved Passwords")
        
        # Create a text box to display the saved passwords
        saved_passwords_text = tk.Text(saved_passwords_window, width=50, height=10)
        saved_passwords_text.pack(padx=5, pady=5)
        
        # Insert the saved passwords into the text box
        for password in self.saved_passwords:
            saved_passwords_text.insert(tk.END, f"Purpose: {password['purpose']}\nPassword: {password['password']}\n\n")

if __name__ == "__main__":
    PasswordGenerator()