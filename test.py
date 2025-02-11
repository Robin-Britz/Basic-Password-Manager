import tkinter as tk

root = tk.Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

form_frame = tk.Frame(root)
form_frame.grid(column=0, row=1, columnspan=3, pady=20)

# Make columns evenly sized
form_frame.columnconfigure(1, weight=1)
form_frame.columnconfigure(2, weight=1)

# Labels (set width to align them)
website_label = tk.Label(form_frame, text="Website:", width=15)
website_label.grid(column=0, row=0)
website_entry = tk.Entry(form_frame)
website_entry.grid(column=1, row=0, columnspan=2, sticky="ew")

email_username_label = tk.Label(form_frame, text="Email/Username:", width=15)
email_username_label.grid(column=0, row=1)
email_username_entry = tk.Entry(form_frame)
email_username_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

password_label = tk.Label(form_frame, text="Password:", width=15)
password_label.grid(column=0, row=2)
password_entry = tk.Entry(form_frame, width=21)
password_entry.grid(column=1, row=2, sticky="ew")
password_generate_button = tk.Button(form_frame, text="Generate Password")
password_generate_button.grid(column=2, row=2)

add_button = tk.Button(form_frame, text="Add", width=36)
add_button.grid(column=0, row=3, columnspan=3)

root.mainloop()
