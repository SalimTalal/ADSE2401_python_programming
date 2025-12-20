# Python file/script to get a person's details from the user and store them
# in the 'person_pathlib.txt' file in the files folder/directory
# This version uses the pathlib module in the standard Python library which is more
# portable and works across different Operating systems without the need to manually handle
# file seperators or absolute paths.

# Import the required modules
import pickle
from pathlib import Path
from person import Person

# Prompt the user for their namd and age
name = input("Plese enter your name: \n")
age = input("Plese enter your age: \n")

# Create/instantiate a Person object
user = Person(name,age)

# Get the path to the file to be created/appended
#file_path = os.path.abspath(os.path.join(os.getcwd(),"..","files","person_os.txt"))
file_path = Path.cwd().parent / "files" / "person_pathlib.txt"

# Ensure that the directory exists, if not create it
file_path.parent.mkdir(parents=True, exist_ok=True)

# Pickle the Person object
with open(file_path,"ab") as f:
    pickle.dump(user,f)

# Notify user about successfully pickling their details
print(f"The 'user' object has been successfully pickled in:\n{file_path}")
