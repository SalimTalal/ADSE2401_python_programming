# Python script to demonstrate getting input from the user

# Import the math module
import math

# Prompt the user for their name
name = input("What is your name? : ")

# Greet the user
print(f'Hello {name}, welcome to Python Programming!')

# Read in two numbers from the user and perform some bsic arithmetic operations on them
print(f'Please enter the first number/value to be used in the calculations :')
first_number = int(input())
second_number = int(input(f'Please enter the second number to be used in the calculation: \n'))

# Perform the arithmetic operations
sum = first_number + second_number
product = first_number * second_number
difference = first_number - second_number
quotient = first_number / second_number
modulus = first_number % second_number
square = first_number ** 2 # math.pow(first_number, y:2)
cube = math.pow(second_number, 3) # second_number ** 3

# Display the results of the above calculations
print(f'Calculation Results' .center(42))
print(f'-'*42)
print(f'{first_number} + {second_number} = {sum}')
print(f'{first_number} X {second_number} = {product}')
print(f'{first_number} - {second_number} = {difference}')
print(f'{first_number} \u00f7 {second_number} = {quotient}')
print(f'{first_number} % {second_number} = {modulus}')
print(f'{first_number} squared = {square}')
print(f'{second_number} cubed = {cube}')
print(f'-'*42)

# Notes on Python division
# 1. Standard Division(/) : The / operator performs floating-point
# division. This means it will always return a float, even if the
# division results in a whole number.
quotient1 = 10 / 3
print(f'quotient1 (10 / 3) = {quotient1}') # Output: 3.3333333333333335

quotient2 = 10 / 2
print(f'quotient2 (10 / 2) = {quotient2}') # Output: 5.0

# 2. Floor Division(//) Also called integer division : The // operator
# performs floor division. This means it divides and then rounds down to
# the nearst whole number (integer).
quotient3 = 10 // 3
print(f'quotient3 (10 // 3) = {quotient3}') # Output: 3

quotient4 = 10 // 2
print(f'quotient4 (10 // 2) = {quotient4}') # Output: 5

quotient5 = 10.0 // 3
print(f'quotient5 (10.0 // 3) = {quotient5}') # Output: 3.0 (the result is still a float, but floored)
