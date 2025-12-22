# Python script/file to demonstrate the map() function

# set of Fibonacci numbers -> golden rationing 1.61803
numbers = sorted(set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]))

# Get and display the tripple of each of the Fibonacci numbers in the above set
tripled_num = sorted(set(map(lambda x: x ** 3, numbers)))

print(f"Set of Fibonacci numbers : \n{numbers}"
      f"\nTriples of Fibonacci numbers : \n{tripled_num}")

# List of names and ages
names = ['Abigail','Bernice','Charlene','Denise']
ages = [21,24,22,19]

# Use the map function to combine the above names and ages for each person
combined_data = map(lambda name, age : name + " is " + str(age) + " years old", names, ages)

# Convert the combined map object to a list and display the result
name_age_results = list(combined_data)
for result in name_age_results:
    print(result)