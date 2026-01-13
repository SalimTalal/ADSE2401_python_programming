# Python script to demonstrate creating an addition functionality and its unit test
# using introspection

def add(a, b):
    """
    Calculates the sum of two numbers
    :param a(int, float): The first number to be summed/added
    :param b(int, float): The second number to be summed/added :
    :returns:
        int, float: The sum of the two numbers. The return type
        depends on the type of input.

    Example:
        >>> add(1, 2)
        3
        >>> add(3, 4.5)
        7.5
        >>> add(2.5, 3.1)
        5.6

    Notes:
        - The function can handle both floats and integers.
        - The result type will match the type of the inputs. For example,
          adding an integer to a float will yield a float
        - If either 'a' or 'b' are non-numeric type, a 'TypeError' is raised.

    Raises:
        TypeError: If either 'a' or 'b' are not integers or floats.
    """
    return a + b

# Display the documentation string of the add() function
print(f"The documentation string of the 'add()' function is given below : \n{add.__doc__}")

# Function to accept an arithmetic operator and two number to perform the operation on
def perform_operation(operation,x,y):
    """
    Performs a basic arithmetic operation ('add', 'subtract', 'multiply' or 'divide')
    on two numbers.

    :param operation: A string indicating the type of arithmetic operation to be performed.
        Accepted values are 'add', 'subtract', 'multiply' or 'divide' (case-insensitive).
    :type operation: str
    :param x: The first numeric operand
    :type x: int or float
    :param y: The second numeric operand
    :type y: int or float

    :return: The result of the arithmetic operation  on the two numeric operands.
    :rtype: int or float

    :raises ValueError: If the operation is not one of the supported options.
    :raises ZeroDivisionError: If division by zero is attempted.

    Example:
        >>> perform_operation('add',2 ,3)
        5
        >>> perform_operation('SUBTRACT',10 ,4)
        6
        >>> perform_operation('MULTIPLY',2.5 ,4)
        10.0
        >>> perform_operation('dIVide',9 ,3)
        3.0

    Notes:
        - The operation string is case-insensitive.
        - Both integer and floating point numbers are accepted/supported.
        - If 'y' is 0 (zero) and the operation is 'divide', a ZeroDivisionError will be raised.
    """
    if operation.lower() == 'add':
        return x + y # add(x,y)
    elif operation.lower() == 'subtract':
        return x - y
    elif operation.lower() == 'multiply':
        return x * y
    elif operation.lower() == 'divide':
        return x / y
    else:
        raise ValueError(f'Operation "{operation}" is not recognised. \n'
                         f'Please use "add", "subtract", "multiply" or "divide" instead.')

# Use global(s) to dynamically access and execute the operation() function
operation, num1, num2 = 'adD', 5, 3
print(f"Result of operation : '{operation.lower()}' on {num1} and {num2} is : \n"
      f"{perform_operation(operation,num1,num2)}")

# Get values from the user
operation = input(f"Please enter the arithmetic operation you would like to perform:"
                  f"\n:'add' for addition, "
                  f"\n:'subtract' for subtraction, "
                  f"\n:'multiply' for multiplication, "
                  f"\n:'divide' for division, \n ")
num1 = int(input("Please enter the first numeric operand:"))
num2 = int(input("Please enter the second numeric operand:"))

# Perform the operation and display the result
print(f"Result of operation : {operation.lower()} on {num1} and {num2} is : \n"
      f"{perform_operation(operation.lower(),num1,num2):.2f}")