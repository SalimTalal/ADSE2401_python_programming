# Python script to demonstrate working with assertions

# Function to divide 2 numbers then return the quotient
def divide(x, y):
    assert y != 0, "Cannot divide by zero!" # Raise an AssertionError when y (denominator) is zero '0'
    return x / y

try:
    result = divide(10, 2)
    print(f"10 / 2 = {result}")

    # Attempt divide by zero (will result in an error)
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
except AssertionError as ae:
    print(f"AssertionError: {ae}")

# Use an assertion for post condition check
def factorial(n):
    # n != n×(n−1)!
    # This is the rule that factorization follows AND thus leading to why factor of zero is one
    # 1 != 1×0! -->
    # 1 != 1 - --> only
    # works if: 0 != 1!
    # Otherwise, the rule would break.
    assert n > 0, "Factorial of negative numbers is not defined!"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get the factorial of 5 and -3
try:
    print(f"The factorial of 5 is : {factorial(5)}") # Expected output is 120
    print(f"The factorial of -3 is : {factorial(-3)}") # Raises an AssertionError: Factorial of negative numbers
except AssertionError as ae:
    print(f"AssertionError: {ae}")

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    try:
        assert len(numbers) > 0, "Cannot calculate average of empty list!"
        average = sum(numbers) / len(numbers)
        print(f"The average of numbers is : {average}")
    except AssertionError as ae:
        print(f"AssertionError: {ae}")

# Test the function with a non-empty and empty list
calculate_average([1,2,3,4,5]) # Expected output => 3
calculate_average([]) # Expected output : AssertionError: Cannot calculate average of an empty list.