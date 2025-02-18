import json
import tkinter
from tkinter import messagebox
import random

# PASSWORD GENERATOR
chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '|', ';', ':', '"', ',', '<', '>', '.', '/',
    '?', '`', '~'
]


# SEARCH CREDENTIALS
def search():
    """Search for existing credentials"""
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"No Data File Found.")
        return
    else:
        if website not in data:
            messagebox.showerror(title="Error", message=f"No Details Found For Website: {website}")
        else:
            messagebox.showinfo(title="Details Found", message=f"Website: {website}\n"
                                                               f"Username: {data[f"{website}"]["email"]}\n"
                                                               f"Password: {data[f"{website}"]["password"]}\n")


# SAVE CREDENTIALS
def save():
    """Stores Site, Username, Password in JSON"""
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            tkinter.messagebox.showinfo("Saved", f"Entry added:\nWebsite: {website}\n"
                                                 f"Username: {email}\nPassword: {password}")
            website_entry.delete(0, len(website))
            password_entry.delete(0, len(password))
            website_entry.focus()


def generate_password():
    """Generates a random 12 digit password"""
    password = ''
    for i in range(0, 13):
        letter = random.choice(chars)
        password += letter
    password_entry.delete(0, len(password_entry.get()))
    password_entry.insert(0, password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)


# UI SETUP
root = tkinter.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

content = tkinter.Canvas(root, width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
content.create_image(100, 100, image=logo)
content.grid(column=1, row=0)

# WEBSITE LABEL AND ENTRY
website_label = tkinter.Label(root, text="Website:")
website_label.grid(column=0, row=1)
website_entry = tkinter.Entry(root)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

# USERNAME LABEL AND ENTRY
email_username_label = tkinter.Label(root, text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_entry = tkinter.Entry(root)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_username_entry.insert(0, "iThinkImAnAlien@gmail.com")

# PASSWORD LABEL AND ENTRY
password_label = tkinter.Label(root, text="Password:")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(root)
password_entry.grid(column=1, row=3, sticky="ew")
password_generate_button = tkinter.Button(root, text="Generate Password", borderwidth=0.5, command=generate_password)
password_generate_button.grid(column=2, row=3)

# ADD BUTTON
add_button = tkinter.Button(root, text="Add", borderwidth=0.5, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# SEARCH BUTTON
add_button = tkinter.Button(root, text="Search", borderwidth=0.5, command=search)
add_button.grid(column=2, row=1, columnspan=2, sticky="ew")

root.mainloop()
