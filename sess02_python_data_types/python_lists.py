"""
Python Lists
A Python List is a built in data type that repesents an ordered collection of items/elements, that are homogeneous in nature.
Liest allow duplicates and are mutable (i.e. their elements can be modified, added or removed).
Lists are created using [] or the list() constructor.
A sample list and some of its operations are given below.
"""

# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Display the fruits in the fruit list
print(f"The initial list of fruits are: {fruits}")

# Display the number of items/elements in the fruit list
print(f"The number of fruits in the fruits list is : {len(fruits)}")

# Add a fruit in the end of the fruit list
fruits.append("orange")
print(f"After adding 'orange' to the fruits list we get: \n{fruits}")

# Add the contents of another list of fruits to our fruit list
fruits.extend(["mango",'grapes','kiwi','pineapple','strawberry','guava','avocado'])

# Display the combined list of fruits
print(f"The combined fruits list is : \n{fruits}")

# Insert a fruit (item/element) at a given/specified index
fruits.insert(1,"pear")
print(f"After inserting 'pear' to the fruits list we get: \n{fruits}")

# Remove a fruit (item/element) at a given/specified index
remove_fruit = fruits.pop(3)
print(f"The removed fruit is:\n{remove_fruit}")
print(f"After removing {remove_fruit} from the fruits list we get: \n{fruits}")

# Remove a specific fruit (item/element) from the list
fruits.remove("banana")
print(f"After removing 'banana' from the fruits list we get: \n{fruits}")

#Get and display the index of an item/element in the list
print(f"The first aoccurence of 'mango' is at index: {fruits.index('mango')}")

# Get and display the occurences of a given item/element in the list
print(f"'apple' occurs {fruits.index('apple')} times in the fruits list.")

# Sort and display the fruits in lexicographical/alphabetical ascending order
fruits.sort()
print(f"The list of fruits in lexicographical order: {fruits}")
print(f"After sorting the fruits list is : {fruits}")

# Get and display the minimum and maximum items/elements in the list
# (least and highest fruits letterwise)
print(f"The least fruit letterwise is: {min(fruits)}"
      f"\nThe highest fruit letterwise is: {max(fruits)}")

# Get and display a copy of the fruit list
copy_of_fruits = fruits.copy()
print(f"The copied fruits list is : \n{copy_of_fruits}")

# Remove all the fruits from the list and display the empty list of fruits
fruits.clear()
print(f"After removing all fruits we get: \n{fruits}")

# Python list slice operations
fruits = ['apple', 'kiwi','grape','orange','tangerine','lemon','avocado','coconut','fig'] # re-assign the fruit list

print(f"-"*30)
print(f"After re-assignment, the new fruits list is: \n{fruits}")

# Display the first 3 fruits in the list
print(f"The first 3 fruits in the fruits list are : {fruits[:3]}")

