# Python script to demonstrate how to create, write and read from a text file

# Import the os module
import os # Module to enable our script work with the operating system (OS) and its file system

# Create a file to create and write to a file
def create_file(path,content):
    """
    Create a file with the given path and writes the specified content to it.
    :param path(str): The path of the file to be created.
    :param content(str): The content to be written to the file.
    :return:
    """
    with open(path,"w",encoding="utf-8") as f:
        f.write(content)
    print(f"File created and contents written successfully!")

# Get and display the current working directory
current_dir = os.getcwd()
print(f"Current directory is : \n{current_dir}")

# Get and display the path to the 'files' directory by going up one folder
file_directory = os.path.abspath(os.path.join(current_dir,'..',"files"))
print(f"The path to the 'files' directory is : \n{file_directory}")

# Specify and display the file path and name of the file to be created
file_path = os.path.join(file_directory,"hello.txt")
print(f"The pull path to the file to be created is : \n{file_path}")

# Specify the text/content to be written to the file using a hard-coded/user-input string
content = input("Please enter the text you want to write to the file:\n")
content = "Hello 👋👋 from text files in Python!!!\n" # emoji in windows <window> + <.>

# Call/invoke the create_file() function to create and write to the text file
create_file(file_path,content)

# TODO: Write code to read the contents of the 'hello.txt' file and display them