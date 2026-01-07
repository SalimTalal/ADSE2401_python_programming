# Python script to demonstrate the __closure__ attribute to access closure variables

def outer_funct(outer_var):
    """
    Outer function that defines an inner function and captures
    the variable `outer_var` in its closure.

    Args:
        outer_var (int): A variable to be captured by the inner function.

    Returns:
        function: An inner function that uses the captured variable.
    """
    def inner_funct(inner_var):
        """
         Inner function that uses the variable `outer_var` from the outer
         function's scope and accepts an argument `inner_var`.

         Args:
             inner_var (int): A variable to be used within the inner function.

         Returns:
             int: The sum of `outer_var` and `inner_var`.
         """
        return outer_var + inner_var
    return inner_funct

# Using the above closures to add numbers
add_five = outer_funct(5)
print(f"add_five is : {add_five.__closure__[0].cell_contents}")
result = add_five(10)
print(f"result is : {result}")

# Create a closure by calling the outer function
closure_func = outer_funct(10)

# Display the '__closure__' attribute of the closure function
print(f"closure_func's __closure__ is :")
print(closure_func.__closure__)

# Demonstrate the use of the closure_func
result = closure_func(5)
print(f"Result of calling closure_func() with argument 5 is : {result}")

# Access the captured variable for the closure's cell
if closure_func.__closure__:
    captured_cell = closure_func.__closure__[0]
    captured_value = captured_cell.cell_contents
    print(f"The captured value in the closure is : {captured_value}")
