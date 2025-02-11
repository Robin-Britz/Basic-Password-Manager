import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

root.grid_columnconfigure(0, weight=1)  # Column 0 stretches
root.grid_columnconfigure(1, weight=2)  # Column 1 stretches more

root.grid_rowconfigure(0, weight=1)  # Row 0 stretches
root.grid_rowconfigure(1, weight=2)  # Row 1 stretches more

tk.Label(root, text="Resizable", bg="lightblue").grid(row=0, column=0, columnspan=2, sticky="nsew")
tk.Button(root, text="Button 1").grid(row=1, column=0, sticky="nsew")
tk.Button(root, text="Button 2").grid(row=1, column=1, sticky="nsew")

root.mainloop()
