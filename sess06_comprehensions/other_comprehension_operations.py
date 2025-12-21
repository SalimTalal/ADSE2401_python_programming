# Python script to demonstrate working with comprehesions 1759

# List of Fibonacci numbers -> golden ration 1.61803
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Get and display the squares of the above fibonacci numbers using a list comprehension
squares = [n ** 2 for n in numbers]
print(f"First 12 Fibonacci numbers : \n{squares}\nFibonacci squares : \n{squares}")

# Get and display the cubes of the even Fibonacci numbers above using a list comprehension
cubes = [n ** 3 for n in numbers if n % 2 == 0]
even_fibonacci = [n for n in numbers if n % 2 == 0]
print(f"Even Fibonacci numbers : \n{even_fibonacci}\nEven Fibonacci cubes : \n{cubes}")

# Dictionary of students and their mean scores in an exam
student_scores = {'Sue':56,'Jim':72,'Mark':61,'Micha':55,'William':78,'Jane':51,'Xi':56,'Abigail':92}

# Display the students and their scores
print(f"Students and their exam scores are : \n{student_scores}")

# Get and display a dictionary of the student's that passed (passmark:55)
passed_students = {name:score for name, score in student_scores.items() if score > 55}
print(f"Students that passed and their exam scores are : \n{passed_students}")

# TODO: Get and display the dictionary of students that failed

# Extract and display the set of student names from the student_scores dictionary keys
student_names = set(student_scores.keys())
print(f"Student names : \n{student_names}")

# Get and display the set of students names with 4 or more letters/characters
names_with4_or_more = {name for name in student_names if len(name) >= 4}
print(f"Student names with 4 or more letters : \n{names_with4_or_more}")

# Comprehension with string functions
paragraph = """
Click Insert and then choose the elements you want from the different galleries. Themes and styles also help keep your 
document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change 
to match your new theme. When you apply styles, your headings change to match the new theme. Save time in Word with new
buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for 
layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then 
click the plus sign. Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus 
on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on 
another device.
"""

# Remove all the manual line breaks (\n or newline characters) and replace them with a space (" ")
cleaned_paragraph = paragraph.replace("\n"," ")

# Split the above paragraph into sentences using the split function
sentences = cleaned_paragraph.split('.')

# Display each sentence on a new line
for sentence in sentences:
    # Strip the leading/trailing whitespace and ensure the sentence isn't empty
    cleaned_sentence = sentence.strip()
    if cleaned_sentence: # Avoid printing/displaying empty sentences
        print(cleaned_sentence)

