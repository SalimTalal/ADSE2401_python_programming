# Python file to demonstrate the use of a closure to increment a counter and return its value

# Define a closure function
def counter(): # Enclosing function
    count = 0

    # Define an inner function (the return object of the enclosing function)
    def inner():
        nonlocal count # refers to the count in the enclosing function
        count += 1
        return count
    return inner

# Create 2 counter instances
c1 = counter()
c2 = counter()

# Display the return type of the counter() function
print(f'The "counter()" returns : {type(c1)}')

# Display the first 10 values of c1 using a for loop
for n in range(10):
    print(f'Current value of counter c1 is : {c1()}')

# Display the first 5 values of c2 manually
print(f'\nValues for counter c2 are : ')
print(f"Current value of counter c2 is : {c2()}")
print(f"Current value of counter c2 is : {c2()}")
print(f"Current value of counter c2 is : {c2()}")
print(f"Current value of counter c2 is : {c2()}")
print(f"Current value of counter c2 is : {c2()}")

# Display the subsequent value of counter1
print(f"\nCurrent value of counter c1 is : {c1()}")