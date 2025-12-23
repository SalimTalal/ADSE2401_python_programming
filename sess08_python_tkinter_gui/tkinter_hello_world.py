# Python tkinter script/file with a label and button to display a message on the screen
# once the button is clicked

# Import the tkinter module
import tkinter as tk

# Instantiate a tk object
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y positions to center the window/GUI
x = (screen_width - 649) // 2
y = (screen_height - 480) // 2

# Set the dimensions of the window
root.geometry('640x480+{}+{}'.format(x,y))

# Create a lable with it's content/text and font size
label = tk.Label(root, text="Hello World!", font=("Arial", 20),fg='red')
label.pack()

# Function definition
def toggle_text():
    if label['text'] == "Hello World!":
        label['text'] = "Bye World!"
    else:
        label['text'] = "Hello World!"

# Create a buttton with its content and font size
button = tk.Button(root, text="Toggle Text", command=toggle_text, font=("Arial",25),fg='blue')
button.pack()

# Run the application
root.mainloop()