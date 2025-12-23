# Python GUI app to accept an email address from the user and validate it using regex

# Import the required modules
import re
import tkinter as tk
from tkinter import messagebox,END

# Function to validate email address
def validate_email():
    """
    A function to validate the email address.

    :return:
        Returns a message if the email address is valid or not.
    """
    email = entry_email.get().strip()
    if email == "": # same as not email
        messagebox.showerror("Missing Email Address","Please enter the email address to be validated")
        return
    pattern = r"^[a-zA-Z\d.+_-]+@[a-zA-Z\d._]+\.[a-zA-Z]+$"

    if re.fullmatch(pattern,email):
        messagebox.showinfo("✔Success!!","Valid Email Address")
    else:
        messagebox.showerror("❌Void!!","Invalid Email Address")

# Function to clear email address
def clear_text():
    """
    A function to clear the email text from the entry field.
    :return:
        Clears the entry field leaving it empty for new email text entry.
    """
    entry_email.delete(0, END)
    entry_email.focus()

# Set up the GUI
root = tk.Tk()
root.title("Validate Email Address")

# Labels
label_email = tk.Label(root, text="Enter Email Address : ")
label_email.grid(row=0, column=0,padx=10,pady=5)

# Entry fields
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1,padx=10,pady=5)

# Buttons
button_validate = tk.Button(root, text="Validate Email",command=validate_email)
button_validate.grid(row=1,column=0,padx=10,pady=5)

button_clear = tk.Button(root, text="Clear Email",command=clear_text)
button_clear.grid(row=1,column=1,padx=10,pady=5)


# Run the application
root.mainloop()