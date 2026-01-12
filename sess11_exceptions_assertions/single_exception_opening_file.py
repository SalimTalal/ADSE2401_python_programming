# Python script that handles an exception raised when the user tries to open a non-existent file.

file = None

try: # Write the code that may raise an exception(s) here
    file = open("non-existent.bin","rb")
    content = file.read()
    print(f"File contents are : \n{content}")
except FileNotFoundError: # Handle the file error here
    print(f"Error, sorry the file was not found. \nPlease check the path and file name "
          f"and ensure that you have access permission(s), then try again.")
finally: # Resource clean up
    #if 'file' in locals():
    if file is not None:\
        file.close()


# The code could also be written as :
# try:
#     with open("non-existent.bin", "rb") as file:
#         content = file.read()
#         print(f"File contents are:\n{content}")
# except FileNotFoundError:
#     print(
#         "Error, sorry the file was not found.\n"
#         "Please check the path and file name and ensure that you have access permission(s), then try again."
#     )