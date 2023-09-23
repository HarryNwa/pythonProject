import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buddy Diary")
        self.current_user = None
        self.diary = Diaries()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Buddy Diary", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Log in", command=self.login)
        self.login_button.pack(pady=5)

        self.create_account_button = tk.Button(self.root, text="Create new account", command=self.create_account)
        self.create_account_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def login(self):
        if self.current_user:
            messagebox.showinfo("Error", "You are already logged in as " + self.current_user)
            return

        username = simpledialog.askstring("Login", "Enter your username:")
        password = simpledialog.askstring("Login", "Enter your password:", show="*")

        if not username or not password:
            messagebox.showinfo("Error", "Username and password cannot be empty.")
            return

        if self.diary.validate_user(username, password):
            self.current_user = username
            self.main_menu()
        else:
            messagebox.showinfo("Error", "Invalid username or password.")

    def create_account(self):
        if self.current_user:
            messagebox.showinfo("Error", "You are already logged in as " + self.current_user)
            return

        username = simpledialog.askstring("Create Account", "Enter a username:")
        password = simpledialog.askstring("Create Account", "Enter a password:", show="*")

        if not username or not password:
            messagebox.showinfo("Error", "Username and password cannot be empty.")
            return

        if self.diary.create_user(username, password):
            messagebox.showinfo("Success", "Account created successfully!")
        else:
            messagebox.showinfo("Error", "Username already exists. Please choose a different username.")

    def main_menu(self):
        self.label.config(text="Welcome, " + self.current_user)
        self.login_button.config(state=tk.DISABLED)
        self.create_account_button.config(state=tk.DISABLED)
        self.exit_button.config(text="Logout", command=self.logout)

        self.lock_button = tk.Button(self.root, text="Lock Diary", command=self.lock_diary)
        self.lock_button.pack(pady=5)

        self.unlock_button = tk.Button(self.root, text="Unlock Diary", command=self.unlock_diary, state=tk.DISABLED)
        self.unlock_button.pack(pady=5)

        self.create_entry_button = tk.Button(self.root, text="Create Entry", command=self.create_entry, state=tk.DISABLED)
        self.create_entry_button.pack(pady=5)

        self.view_entries_button = tk.Button(self.root, text="View Entries", command=self.view_entries, state=tk.DISABLED)
        self.view_entries_button.pack(pady=5)

    def logout(self):
        self.current_user = None
        self.label.config(text="Welcome to Buddy Diary")
        self.login_button.config(state=tk.NORMAL)
        self.create_account_button.config(state=tk.NORMAL)
        self.exit_button.config(text="Exit", command=self.root.quit)
        self.lock_button.pack_forget()
        self.unlock_button.pack_forget()
        self.create_entry_button.pack_forget()
        self.view_entries_button.pack_forget()

    def lock_diary(self):
        if self.diary.lock_diary(self.current_user):
            self.lock_button.config(state=tk.DISABLED)
            self.unlock_button.config(state=tk.NORMAL)
            self.create_entry_button.config(state=tk.NORMAL)
            self.view_entries_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "Diary locked successfully!")
        else:
            messagebox.showinfo("Error", "Diary is already locked!")

    def unlock_diary(self):
        password = simpledialog.askstring("Unlock Diary", "Enter your password:", show="*")
        if password:
            if self.diary.unlock_diary(self.current_user, password):
                self.lock_button.config(state=tk.NORMAL)
                self.unlock_button.config(state=tk.DISABLED)
                self.create_entry_button.config(state=tk.DISABLED)
                self.view_entries_button.config(state=tk.DISABLED)
                messagebox.showinfo("Success", "Diary unlocked successfully!")
            else:
                messagebox.showinfo("Error", "Invalid password.")

    def create_entry(self):
        title = simpledialog.askstring("Create Entry", "Enter the title:")
        body = simpledialog.askstring("Create Entry", "Enter the body:")

        if title and body:
            if self.diary.create_entry(self.current_user, title, body):
                messagebox.showinfo("Success", "Entry created successfully!")
            else:
                messagebox.showinfo("Error", "Failed to create entry.")
        else:
            messagebox.showinfo("Error", "Title and body cannot be empty.")

    def view_entries(self):
        entries = self.diary.get_entries(self.current_user)
        if entries:
            entry_text = "Your Entries:\n\n"
            for entry in entries:
                entry_text += f"Title: {entry['title']}\nBody: {entry['body']}\n\n"
            messagebox.showinfo("Entries", entry_text)
        else:
            messagebox.showinfo("Entries", "No entries to display.")

class Diaries:
    def __init__(self):
        self.users = {}
        self.locked_diaries = {}

    def create_user(self, username, password):
        if username not in self.users:
            self.users[username] = password
            self.locked_diaries[username] = True
            return True
        return False

    def validate_user(self, username, password):
        return username in self.users and self.users[username] == password

    def lock_diary(self, username):
        if username in self.locked_diaries and self.locked_diaries[username]:
            self.locked_diaries[username] = False
            return True
        return False

    def unlock_diary(self, username, password):
        if username in self.users and self.users[username] == password:
            self.locked_diaries[username] = True
            return True
        return False

    def create_entry(self, username, title, body):
        if username in self.users and self.locked_diaries[username]:
            if username not in self.users:
                self.users[username] = []
            self.users[username].append({'title': title, 'body': body})
            return True
        return False

    def get_entries(self, username):
        return self.users.get(username, [])


if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
