# Python file/script to get a person's details from the user and store them
# in the 'person_os.txt' file in the files folder/directory

# Import the required modules
import pickle
import os
from person import Person

# Prompt the user for their namd and age
name = input("Plese enter your name: \n")
age = input("Plese enter your age: \n")

# Create/instantiate a Person object
user = Person(name,age)

# Get the path to the file to be created/appended
file_path = os.path.abspath(os.path.join(os.getcwd(),"..","files","person_os.txt"))

# Display the path to the file to be created or appended to
print(f"Path to the 'person_os.txt' file is:\n{file_path}")

# Pickle the Person object
with open(file_path,"ab") as f:
    pickle.dump(user,f)

# Notify user about successfully pickling their details
print(f"The 'user' object has been successfully pickled in:\n{file_path}")
