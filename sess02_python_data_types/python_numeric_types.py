# Python script to demonstrate Python's number/numeric types
import decimal
# Get the code to make Decimal numbers work
from decimal import Decimal, getcontext, ROUND_DOWN
# Get the code to make Fraction numbers work
from fractions import Fraction

# Demonstrate integers (whole numbers, both +ve and -ve)
int_value = 8
print("Interger Demonstration")
print(f"-"*22)
print(f"The value of int_value is {int_value}")
print(f"The type of int_value is {type(int_value)}\n")

# Demonstrate floats/floating point numbers (numbers with fractional component, both +ve and -ve)
float_value = 3.1415927
print("Floating-point Number Demonstration")
print(f"-"*36)
print(f"The value in the variable float_value is {float_value}")
print(f"The value in the variable float_value correct to 4 d.p. is {float_value:.4f}")
print(f"The value in the variable float_value correct to 4 d.p. is %.4f" % float_value)
print(f"The type of float_value is {type(float_value)}\n")

# Demonstrate Decimal (with decimal places and a fixed precision, both -ve and +ve)
# Set the precision for decimal operations
getcontext().prec = 7 # Set a higher precision when you nedd to maintian accuracy
# For rounding numbers with lots of decimal places e.g. Decimal('345.234567890123456789')
decimal_value = Decimal(8.1415923892)
print('Decimal Number Demonstration')
print('-'*32)
print(f"The original value of decimal_value is: {decimal_value}")
# Using ROUND_DOWN to ensure no rounding up takes place
decimal_value = Decimal('1.2345678901234578').quantize(Decimal('0.0001'),rounding=ROUND_DOWN)
print(f"The modified value of decimal_value correct to four d.p. is: {decimal_value}")
print(f"The type of decimal_value is {type(decimal_value)}\n")

# Demonstrate Complex Numbers
complex_value = 3 + 4j
print("Complex Number Demonstration")
print(f"-"*32)
print(f"The value of complex_value is {complex_value}")
print(f"The type of complex_value is {type(complex_value)}\n")
print(f"The real part of the value of complex_value is {complex_value.real}")
print(f"The imaginary part of the value of complex_value is {complex_value.imag}")

# Demonstrate Fraction (rational numbers)
fraction_value = Fraction(7, 3)
print("Fraction Number Demonstration")
print(f"-"*32)
print(f"The value of fraction_value is {fraction_value}")
print(f"The type of fraction_value is {type(fraction_value)}\n")

# Demonstrating Boolean (True or False)
true_value = True
false_value = False; n = 5; a = 8 # How to declare multiple variable on a single in Python
print(f"Boolean Value Demonstration")
print(f"-"*32)
print(f"The Boolean value in true_value is : {true_value}")
print(f"The Boolean value in false_value is : {false_value}")
print(f"The type of true_value is {type(true_value)}, and false_value is {type(false_value)}")
print(f"\nUsing booleans in arithmetic operations")
print(f"-"*42)
print(f"True + True = {true_value + true_value}")
print(f"True + False = {true_value + false_value}")
print(f"False + False = {false_value + false_value}")
print(f"False + n(5) is : {false_value + n}")
print(f"True + a(8) is : {true_value + a}")
print(f"True x n(5) is : {true_value * n}")
print(f"(n < a) x 10 + (n == a) x 20 is : {(n < a) * 10 + (n == a) * 20}")
