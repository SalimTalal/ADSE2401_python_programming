# Python script to demonstrate strings and string functions in Python

# Declare a string variable
string_var = "hello Salim from Python programming"
print(string_var)

# Display the string variable with the first letter in uppercase using % and an f-string
print("'string_var' with the letter capitalised is : %s" % string_var.capitalize())
print(f"'string_var' with the first letter capitalized is : {string_var.capitalize()}")

# Display the type of 'string_var'
print(f"The type of 'string_var' is : {type(string_var)}")

# Display the contents of 'string_var' in uppercase
print(f"The content of 'string_var' on upper case is : {string_var.upper()}")

# Display the contents of 'string_var' in lowercase
print(f"The content of 'string_var' on lower case is : {string_var.lower()}")

string_2_center = "Programming"
# Center the above text with a specified width adn given fill character
print(string_2_center.center(32,"="))

# Count & display the numer of times a character appears in string ('o' in 'string_var')
print(f"The letter 'o' appears {string_var.count('o')} times in '{string_var}'")

# Display the highest and lowest alphabetical characters (using ASCII codes) in string_var
print(f"The highest and lowest alpahbetical characters in '{string_var}' are : "
      f"{max(string_var)} & {min(string_var)} respectively")

# Replace the 'he' with 'He' and 'Python' with 'C#'
new_str = string_var.replace("he","He")
new_str = new_str.replace("Python","C#")

# Display the replaced/modified string
print(f"The modified contents of 'string_var' are : {new_str}")

# Declare another string variable for more string operations
my_string = "    Hello World 123    "

# Get and display the number of characters using len()
print(f"Length of the string \n'{my_string}' is : {len(my_string)}")

# isalum() - checks if all characters are alphanumeric (no spaces, symbols)
print(f"Is the string \n{my_string} alphanumeric? {my_string.islower()}")

# isupper() - checks if all alphabetic characters are uppercase
print(f"Is the string \n{my_string} all uppercase? {my_string.isupper()}")

# lstrip() - removes any leading whitespace (from the left)
print(f"Remove the leading spaces from '{my_string}' to get : '{my_string.lstrip()}'")

# rstrip() - removes any trailing whitespace (from the right)
print(f"Remove the trailing spaces from '{my_string}' to get : '{my_string.rstrip()}'")

# strip() - removes any leading and trailing whitespace (from the left and right)
print(f"Remove the leading and trailing spaces from '{my_string}' to get : '{my_string.strip()}'")

# endswith() - checks if the specified string ends with the specified substring
print(f"Does the string '{my_string}' ends with '123'? {my_string.strip().endswith('123')}")

# startswith() - checks if the specified string starts with the specified/given substring (prefix)
print(f"Does the string '{my_string}' starts with '123'? {my_string.strip().startswith('123')}")
print(f'Does the string "{my_string}" starts with "    Hello"? {my_string.startswith("    Hello")}')

# find() - locates the first occurence of the speicified substring
print(f"The first uccurence of the string 'World' in {my_string} is at index : {my_string.find('World')}")

# index() - finds the first occurence of the substring, raises error when not found
print("Index of 'World' : ", my_string.index('World'))

# count() - coundt the number of occurences of the substring or character
print(f'The number of occurences of "or" in "{my_string}" = {my_string.count("or")}')

# rfind() - finds the last occurence of the specified substring
print(f"The last occurence of 'l' in '{my_string} is : {my_string.rfind('l')}")

# rindex() - finds the last occurence of the specified substring, raises error when not found
print(f"The last index of 'l' in '{my_string}' is at index : '{my_string.rindex('l')}'")