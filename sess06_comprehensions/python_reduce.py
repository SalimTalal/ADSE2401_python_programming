# Python file/script to demonstrate the reduce() function

# Import the reduce() function from the functools module
from functools import reduce

# A list of numbers to be manipulated using the reduce function
numbers = [17, 45, 23, 68, 144, 8, 51]

# Get the largest numbers from the numbers list using the reduce() function
largest_num = reduce(lambda x, y: max(x, y), numbers)

# Get the least number from the numbers list using the reduce() function
least_num = reduce(lambda x, y: min(x, y), numbers)

# Obtain the product of all numbers in the list using the reduce() function
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# Obtain the sum of all the numbers in the list using the reduce() function
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Display the results
print(f"The list of numbers is : \n{numbers}")
print(f"The largest number from the list is : {largest_num}")
print(f"The least number from the list is : {least_num}")
print(f"The product of numbers in the list is : {product_of_numbers}")
print(f"The sum of numbers in the list is : {sum_of_numbers}")