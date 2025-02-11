import tkinter


# PASSWORD GENERATOR

# SAVE PASSWORD

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

# USERNAME LABEL AND ENTRY
email_username_label = tkinter.Label(root, text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_entry = tkinter.Entry(root)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")

# PASSWORD LABEL AND ENTRY
password_label = tkinter.Label(root, text="Password:")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(root)
password_entry.grid(column=1, row=3, sticky="ew")
password_generate_button = tkinter.Button(root, text="Generate Password", borderwidth=0.5)
password_generate_button.grid(column=2, row=3)

# ADD BUTTON
add_button = tkinter.Button(root, text="Add", borderwidth=0.5)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

root.mainloop()
