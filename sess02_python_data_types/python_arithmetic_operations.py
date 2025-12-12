# Python script to demonstrate the various arithmetic operations on numeric values

# Declare and get two values for the user
num1 = int(input("Enter first number to be used in the calculation: \n"))
num2 = int(input("Enter second number to be used in the calculation: \n"))

# Addition
sum = num1 + num2

# Subtraction
difference = num1 - num2

# Multiplication
product = num1 * num2

# Division
floating_division = num1 / num2
integer_division = num1 // num2

# Modulus
modulus = num1 % num2

# Exponentiation
exponent = num1 ** num2

# Display the results
print(f"Addition of {num1} and {num2} is {sum}")
print(f"Subtraction of {num1} and {num2} is {difference}")
print(f"Multiplication of {num1} and {num2} is {product}")
print(f"Floating Division of {num1} and {num2} is {floating_division}")
print(f"Integer Division of {num1} and {num2} is {integer_division}")
print(f"Modulus of {num1} and {num2} is {modulus}")
print(f"Exponent of {num1} and {num2} is {exponent}")