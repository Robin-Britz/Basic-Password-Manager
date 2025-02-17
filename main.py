import tkinter
from tkinter import messagebox
import random

# PASSWORD GENERATOR
chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '>', '.', '/',
    '?', '`', '~'
]


# SAVE PASSWORD
def save():
    """Stores Site, Username, Password, pipe delimited"""
    with open("data.txt", "a") as file:
        file.write(f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n")

    tkinter.messagebox.showinfo("Saved", f"Entry added:\nWebsite: {website_entry.get()}\n"
                                         f"Username: {email_username_entry.get()}\nPassword: {password_entry.get()}")
    website_entry.delete(0, len(website_entry.get()))
    password_entry.delete(0, len(password_entry.get()))
    website_entry.focus()


def generate_password():
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
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
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

root.mainloop()
