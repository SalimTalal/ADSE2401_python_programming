# Python tkinter GUI script to demonstrate a Tkinter login window

# Import the required module
import tkinter as tk
from tkinter import messagebox

# Define a custom function to authenticate the user
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check that the user has filled both their username and password
    if username.strip() == "" or password.strip() == "": # when any of them is empty
        tk.messagebox.showerror("Missing username or password","Please enter both username and password")
        return
    if username == "admin" and password == "pa$s!1": # Hard-coded username & password
        tk.messagebox.showinfo("Login Successful","Welcome admin, you're now logged in!")
    else:
        tk.messagebox.showinfo("Login Denied","Incorrect username or password!")

# Function to toggle password visibilty
def toggle_password():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# Create/instantiate the main window
root = tk.Tk()
root.title("Login Screen")
root.geometry('640x480')
root.resizable(width=False, height=False)

# Create a centered frame
frame = tk.Frame(root)
frame.place(relx=0.5,rely=0.5,anchor='center')

# Labels
label_username = tk.Label(frame, text="Username:")
label_username.grid(row=0, column=0,padx=10, pady=10,sticky='e')

label_password = tk.Label(frame, text="Password:")
label_password.grid(row=1, column=0,padx=10, pady=10,sticky='e')

# Entry fields
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1,padx=10, pady=10)

entry_password = tk.Entry(frame,show="*")
entry_password.grid(row=1, column=1,padx=10, pady=10)

# Checkbox for showing/hiding the password
show_password_var = tk.BooleanVar()
checkbox_show_password = tk.Checkbutton(frame, variable=show_password_var,text="Show password",command=toggle_password)
checkbox_show_password.grid(row=2, column=1,padx=10,pady=10, sticky='w')

# Login button
button_login = tk.Button(frame, text="Login", command=login)
button_login.grid(row=3, column=0, columnspan=2,pady=20)

# Run the application
root.mainloop()