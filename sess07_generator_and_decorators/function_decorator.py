# Python script/file to demonstrate function decorators

# Function to get nth Fibonacci number using recursion
def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion.
    :param n (int): the nth Fibonacci number.
    :return: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci() function decorator
def fib_decorator(func):
    """
    Decorator function that adds a print() statement before and after executing the decorated function.
    :param func(function): The function to decorate.
    :return: The wrapper function that adds the print() statements.
    """
    def wrapper(n):
        print("Calculating the Fibonacci numbers...")
        result = func(n)
        print(f"Fibonacci numbers are: \n{result}!")
        return result
    return wrapper

# Make use of the above decorator
@fib_decorator
def generate_fibonacci_numbers(n):
    """
    Generates a list of Fibonacci numbers up to the value of n using the fibonacci() function.
    :param n(int): The count of the Fibonacci numbers.
    :return (list): A list of Fibonacci numbers.
    """
    return [fibonacci(a) for a in range(n)]

# Call/invoke the generate_fibonacci_numbers() function to get the first 7 Fibonacci numbers
generate_fibonacci_numbers(7)
print("\n")

# Call/invoke the generate_fibonacci_numbers() function to get the first 18 Fibonacci numbers
generate_fibonacci_numbers(18)
print("\n")