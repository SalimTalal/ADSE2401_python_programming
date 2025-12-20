# Python script to demonstrate the scope of global and local variables

# Declare a global variable
global_var = 5

# Define a function to display the value passed to it
def display_value(value):
    print(f"The value passed in is : {value}")

# Call the display_value function and pass in the global variable (global_var)
display_value(global_var)

def random_function():
    random_variable = "Hello" # random_variable is only accessible within random_function
    return random_variable

 # Call the display_value function and pass in the random_variable
 display_value(random_variable)