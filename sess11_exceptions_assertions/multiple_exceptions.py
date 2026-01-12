# Python script to demonstrate how to handle multiple exceptions

try: # Code that may raise error(s)/exception(s)
    num_list = [3,5,8]
    # Try to display a number at an invalid index
    print(f"Value at index 7 is : {num_list[7]}")

    # Other possible exceptions
    num_list + 5 # Type error as you cannot sum an integer and a list
    num_list.remove(4) # Value error as the list doesn't contain number 4

    # Attempt integer division by zero
    quotient = 12 / 0

# Handle the above exceptions
except IndexError:
    print(f"Error: Index out of range. Please use a valid index.")
except TypeError:
    print(f"Error: Unsupported operation between list and integer.")
except ValueError:
    print(f"Error: The value you are trying to remove does not exist in the list.")
except ZeroDivisionError:
    print(f"Error: Division by zero is not allowed.")
except Exception as e: # Handle any other error type that may occur apart from the above
    print(f"An unexpected error occurred: {e}")
finally:
    print(f"Program execution completed.")