# Python script to demonstrate simple comprehension operations on a set and dictionary

# A list of name and initials
names = ['Sam','Paul','Nemo','PAUL','j','memo']
print(f"List of names and initial : \n{names}")

# Obtain a set of unique names that have more than one character using a set comprehension
names_set = {name[0].upper() + name[1:] for name in names if len(name) > 1}

# Display the unique set of names
print(f"The unique names with more than one letter are : \n{names_set}")

# Dictionary of the occurrences of different letters in the lower & uppercase forms
test_dic = {'l':10, 'b':34, 'Z':2, 'N':4, 'L':4,'z':5}

# Display the dictionary in its original form
print(f"Original letter count in dictionary is : \n{test_dic}")

# Get and display the total occurences of each letter regardless of the case using a dictionary comprehension
letter_count = {k.lower(): test_dic.get(k.lower(),0) + test_dic.get(k.upper(),0) for k in test_dic.keys()}
print(f"The total count for each letter, regardless of case, is : \n{letter_count}")