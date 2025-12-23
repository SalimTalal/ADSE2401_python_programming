# Python script/file to demonstrate the use of formal, positional and keyword arguments in a function
from tkinter import messagebox

from sess03_python_statements_and_syntax.python_decision_constructs import password


# function definition
def profile(name, *args, **kwargs):
    print(f"Name: {name}") # format argument
    if args:
        print(f"Hobbies: ") # Positional variable arguments
        for hobby in args:
            print(f"- {hobby}")
    if kwargs:
        print(f"Other info: ") # Keyword variable arguments
        for key, value in kwargs.items():
            print(f"- {key}: {value}")

# Function call/invocation
profile("Salim","Cooking","Reading","Travelling",gender="Male",age=20,
        password="78ha;df;!",job="Engineer",city="Nakuru",country="Kenya")

# Formal arguments are defined in the function signature(name)
# *args: collects positional arguments as a tuple
# **kwargs: collects extra keyword arguments as a dictionary