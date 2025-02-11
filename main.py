import tkinter


# PASSWORD GENERATOR

# SAVE PASSWORD

# UI SETUP

root = tkinter.Tk()
root.title("Password Manager")

logo = tkinter.PhotoImage(file="logo.png")

content = tkinter.Frame(root)
content.config(width=200, height=200)
content.grid(column=1, row=0)

image = tkinter.Label(content, image=logo)
image.grid()


root.mainloop()
