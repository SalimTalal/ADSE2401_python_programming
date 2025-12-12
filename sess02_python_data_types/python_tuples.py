"""
Python Tuples
A tuple is a built in data type that represents an ordered collection of elements of the same type.
Tuples allow duplicates and are immutable (their elements cannot be modified).
Tuples are created using () rounded brackets/parentheses of tuple() constuctor.
Tuples are generally faster than lists as Python doesn't have to worry about growing or shrinking
them. Some tuple operations are given below:
"""

# Create a tuple of fruits
fruits = ('blueberry', 'orange','apple', 'banana', 'cherry','avocado','guava','pitches')

# Display the fruits in the tuple and their number
print(f"The fruits in the tuple are : \n{fruits}.\n"
      f"The number of fruits in the tuple are : {len(fruits)}")

# Get and display the index of an item/element in the tuple
print(f"The index of 'avocado' is : {fruits.index('avocado')}")

# Get and display the number of occurrences of blueberry in the tuple
print(f"'blueberry' appears {fruits.count('blueberry')} times in the fruit tuple.")

# Combine two tuples to create a third one and display its contents
combined_fruits = fruits + ('kiwi','watermelon','pineapple','dragon fruit')
print(f"The combined fruits tuple contains : \n{combined_fruits}.")

# Create a tuple that repeats the fruit tuple twice
fruits_repeated = fruits * 2
print(f"The fruits repeated tuple contains : \n{fruits_repeated}.")

# Create a sortedd tuple of fruits
sorted_fruits = sorted(fruits)
print(f"The fruits sorted tuple contains : \n{sorted_fruits}.")

# Display the minimum and maximum items (fruits) in a tuple (least and highest fruits letterwise)
print(f"The least fruits letterwise is : \n{min(fruits)}"
      f"\nThe highest fruits letterwise is : \n{max(fruits)}")

# Declard a tuple of numbers
numbers = (1,2,3,4,5)

# Display the tuple of numbers and its sum
print(f"The numbers tuple contains : {numbers} and their sum is : {sum(numbers)}")

# Display the first 3 numbers in the tuples
print(f"The first 3 numbers in the 'numbers' tuple are : {numbers[:3]}") # same as {numbers[0:3]}

# Display only the odd numbers from the numbers tuple
print(f"The odd numbers in the 'numbers' tuple are : {numbers[::2]}") # same as {numbers[0::2]}

# Use the 'any()' function to check if any element in the 'numbers' tuple is true
# In Python, non-zero numbers are considered true. Since all numbers in the tuple are non-zero,
# 'any(numbers)' will return True.
any_true = any(numbers)
print(f"The only non-zero numbers in the 'numbers' tuple are : {any_true} using 'any()'")

# Use the 'all()' function to check if all elements in the numbers tuple are true
# Since all elemnts (1,2,3,4,5) are non-zero, they are all considered true,
# so 'all(numbers)' will also return True.
print(f"The only non-zero numbers in the 'numbers' tuple are : {all(numbers)} using 'all()'")
