# This script demonstrates Python's iteration/repetition/looping constructs
# ---------------------------------------------------------
# 1. for loop
# ---------------------------------------------------------
# Create a list of fruits
from sess02_python_data_types.python_numeric_types import false_value

fruits = ['kiwi', 'watermelon', 'pineapple', 'strawberry', 'banana','mango','blackberry','blueberry','grapes','guava',
          'orange','passion','date','tomato','avocado','apple','plums','cashew fruits','dragon fruit','lemon']

# Display each of the above fruits using a 'for' loop
for fruit in fruits:
    print(f"The current fruit is {fruit}")

# Create a list of numbers and siplay the musing a for loop
numbers = [8, 2, 5, 7, 12, 40, 39, 17, 1, 100, 22]
for num in numbers:
    print(f"The current number is {num}")

# ---------------------------------------------------------
# 2. range
# ---------------------------------------------------------
print(f"range" .center(42,"-"))

# Basic range: generate the first 5 nimbers
for n in range(5): # Note: basic range starts from 0 to speicified number minus 1
    print(f"The current number in the range is {n}")

print(f"range with parameters".center(42,"-"))
# Genetate even numbers starting from 2 to 10 (exclusively) using a range with start, stop and
for n in range(2,10,2):
    print(f"The current even number is {n}")

# Display the cubes of the first 5 integers using a ranged 'for' loop and list comprehension
cubes = [n ** 3 for n in range(1,6)]
print(f"The cubes of the first five integers are : \n{cubes}")

# ---------------------------------------------------------
# 3. while loop
# ---------------------------------------------------------
print(f"While loop".center(42,"-"))
# Display the first 5 multiples of 8
n = 1
print(f"The first five multiples of 8 are : ")
while n <= 5:
    print(f"{n} X 8 = {n * 8}")
    print("%d X 8 = %d" % (n, n * 8)) # %d is a format specifier for integers
    n += 1

# Create a list of even numbers
n, even_nums = 1, []
print(f"The even numbers between 1 - 20 are :")
while n <= 20:
    if n % 2 == 1: # When the number is odd (same as if n % 2 != 0)
        n += 1
        continue # Skip the current iteration when the number is odd
    even_nums.append(n)
    n += 1

# Display the list of even numbers
print(even_nums)

# Practical use of a while loop to search for some text in a paragraph
paragraph = """
Click Insert and then choose the elements you want from the different galleries. Themes and styles also help keep your 
document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change 
to match your new theme. When you apply styles, your headings change to match the new theme. Save time in Word with new
buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for 
layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then 
click the plus sign. Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus 
on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on 
another device.
""".lower() # convert to lower/upper for case insensitive search since default search is case sensitive

# Variable to hold the word/text to search for in the above paragraph
text_to_search = "Document".lower() # convert to lower/upper for case insensitive search
found = False
index = 0

while index < len(paragraph):
    # find the index of the word/search text
    if paragraph[index: index + len(text_to_search)] == text_to_search:
        found = True
        break # exit from the while loop as we've found the word/text we're looking for
    index += 1

if found:
    print(f"\nThe text/word '{text_to_search}' was found at index {index}")
else:
    print(f"\nThe text/word '{text_to_search}' was not found in paragraph!")