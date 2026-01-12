"""
Python Dictionaries:
This is a built in data type that represents a collction of key-value pairs, like a dictionary,
where each word has a corresponding definition.
Dictionaries are unordered, mutable and can store elements of different typs.
Each elelment in a dictionay is accessed by its key rather than its index.
Dictionaries are created usin {} curly brackets /braces.
Some dictionary operations are given below:
"""

# Student dictionary declaration
student = {"name":'Abigail', "age":25, "major":'Computer Science'}

# Display the length (number of key-value pairs) of the student dictionary
print(f"The number of key-value pairs in the 'student' dictionary is : {len(student)}")

# Fetch and display a view object (method to get the keys or values from a dictionary)
# of the keys in the 'student' dictionary
print(f'The keya from the "student" dictionary are : \n{student.keys()}')

# Fetch and display a view object of the values in the 'student' dictionary
print(f'The values from the "student" dictionary are : \n{student.values()}')

# Fetch and display a view object of the contents in the 'student' dictionary
print(f'The contents from the "student" dictionary are : \n{student.items()}')

# Get and display a value using its key from the 'student' dictionary
print(f'The key "name" in the "student" dictionary points to : \n{student["name"]}') # \n{student.get("name")}

# Remove and sidplay the contents of a given key when it exists ina dictionary
# else return/give back an optional default value
phone_no = student.pop('phone_no','Not Specified')
print(f"Tne value of 'phone_no' in the student dictionary is : {phone_no}.")

# Remove and display the contents of the last key-value pair in the 'student' dictionary
print(f"The last key-value pair in teh 'student' dictionary is : {student.popitem()}.")

# Update/modify and dispaly the contents of the 'student' dictionary
student.update({"age":21, "grade":'A', "phone":"07123458"})
print(f"The updated contents for the 'student' dictionary are : \n{student.items()}") # or {student}

# Create a copy of the "student" dictionary
copy_of_student = student.copy()
print(f"The contents of the 'copy_of_student' dictionary are : \n{copy_of_student}")

# Fetch and return the value associated with a given key, and when not found assign it with a default value
major = student.setdefault('major','Not defined')
print(f"The value of the key 'major' in the student dictionary is : {major}.")

# Create and display a new dictionary for the keys of an existing dictionary
new_student = dict.fromkeys(student.keys()) # new_student = dict.fromkeys(["name","age","grade","phone"])
print(f"The keys-value pairs in the 'new_student' dictionary are : {new_student}")

# Delete a specific key-value pair from the 'student' disctionary
del student['grade']
print(f"After removing/deleting the 'grade' key from the 'student' dictionary, the remaining key-value"
      f" pairs are : \n{student}")

# Findt out nd display whether a given key sxists/is present in a dictionary
print(f'The key "age" is present in the "student" dictionary : {"age" in student}.')
print(f'The key "grade" is present in the "student" dictionary : {"grade" in student}.')

# Remove all the content from the student dictionary and display
student.clear()
print(f"After clearing the 'student' dictionary, we get: \n{student}")