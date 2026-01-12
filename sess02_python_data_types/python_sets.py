"""
Python Sets
A set in Python is a built in type that represents an unordered collection of elements of the same or different types.
Sets DON'T allow duplicates and are mutable. They are suitable for tasks that involve checking
membership, removing duplicates and performing mathematical operations like
instersection, union, difference, and symmetric_difference.
Sets are created using the curly braces/brackets {} or set() constructor
Some set operations are given below.
"""
from sess02_python_data_types.python_tuples import combined_fruits

# Create a set of fruits
fruits = {'apple', 'banana', 'cherry', 'durian','orange','elephant apple'}

# Display the contents of the fruit set
print(f"The fruits in the fruit set are : \n{fruits }")

# Display the number of fruits in the fruit set
print(f"The fruit set contains : {len(fruits)} fruits.")

# Add 'orange' to the fruit set
fruits.add('orange')
print(f"After adding 'orange' to the fruit set we get : \n{fruits }")

# Remove 'banana' from the fruit set
fruits.remove('banana')
print(f"After removing banana from the fruit set we get : \n{fruits }")

# Discard 'cherry' from the fruit set
fruits.discard('cherry')
print(f"After removing cherry from the fruit set we get : \n{fruits }")

# Remove the last item (fruit) from a set
popped_fruit = fruits.pop()
print(f"After popping {popped_fruit} from the fruit set we get : \n{fruits }")

# Copy the set of remaining fruits to a new set and display them
copy_of_fruits = fruits.copy()
print(f"After copying the remaining fruits to a new fruit set we get : \n{copy_of_fruits }")

# Declare another set of fruits
more_fruits = {'pear','avocado','mango','pineapple'}

# Create a new combined set of fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"The combined set of fruits is : \n{combined_fruits }")

# Get and display the common fruits in the 'fruits' and 'more_fruits' sets & display them
common_fruits = combined_fruits.intersection(more_fruits)
print(f"The common set of fruits in 'combined_fruits' and 'more_fruits' are : \n{common_fruits }")

# Get and display the fruits that are in 'fruits' set but not in 'more_fruit' set & display them
different_fruits = fruits.difference('more_fruits')
print(f"The fruits in the 'fruit' set but not in the 'more_fruits' set are : \n{different_fruits }")

# Get and display the fruits that are either in 'fruits' or 'more_fruits' sets but not in both
symmetric_diff_fruits = fruits.symmetric_difference(more_fruits)
print(f'The fruits that are either in "fruits" set or "more_fruits" set but not both, are : \n{symmetric_diff_fruits }')

# Check and display whether fruit set is a subset of "more_fruits"
print(f"'fruit' set is a subset of 'more_fruits' : \n{fruits.issubset(more_fruits)}" )

# Check and sidplay whether fruit set is a superset of "more_fruits"
print(f"'fruit set is a superset of 'more_fruits' : \n{fruits.issuperset(more_fruits)}")

# Check and display whether 'fruit' set and 'more_fruit' set have no common fruits/elements
is_disjoint_fruits = fruits.isdisjoint(more_fruits)

# Create another fruit set and use it to update the set of fruits : CAUTION ... overwrites set element
other_fruits = {'watermelon','strawberry','blueberry'}
fruits.update(other_fruits)
print(f'After updating the "fruits" set we get : \n{fruits }')

# Clear and display the 'fruits' set
fruits.clear()
print(f"After clearing the fruits set we get : \n{fruits }")