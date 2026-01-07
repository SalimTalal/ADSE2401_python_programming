# Python script that uses closures to serialize and deserialize a student object
# to and form a JSON file

# Import the required modules
import json, os
from datetime import datetime,date

# Define a Student class
class Student:
    """
     A class to represent a student.

     Attributes:
         reg_no (str): The student's registration number.
         name (str): The student's full name.
         birthdate (date): The student's birthdate as a `datetime.date` object.
         gender (str): The student's binary gender.

     Methods:
         to_dict(): Converts the student instance into a dictionary for serialisation.
         from_dict(data): Creates a Student instance from a dictionary (typically after deserialisation).
     """

    # Constructor
    def __init__(self,reg_no, name, birthdate,gender):
        """
         Constructs all the necessary attributes for the Student object.

         Args:
             reg_no (str): Registration number.
             name (str): Full name of the student.
             birthdate (date): Birthdate of the student.
             gender (str): Gender of the student.
        """
        self.reg_no = reg_no
        self.name = name
        self.birthdate = birthdate
        self.gender = gender

    # Instance method to convert the student object to a dictionary
    def to_dict(self):
        """
        Serializes the student object to a dictionary format suitable for JSON conversion.

        Returns:
            dict: Dictionary with student's data including ISO-formatted birthdate.
        """
        return {
            'reg_no':self.reg_no,
            'name':self.name,
            'birthdate':self.birthdate.isoformat(),
            'gender':self.gender
        }

    # Static method to deserialize a dictionary back to a Student object
    @staticmethod
    def from_dict(data):
        """
        Deserializes a dictionary to create a Student object.

        Args:
            data (dict): A dictionary containing student information.

        Returns:
            Student: A new instance of the Student class.
        """
        return (Student(reg_no=data['reg_no'],
                        name=data['name'],
                        birthdate=datetime.strptime(data['birthdate'],'%Y-%m-%d').date(),
                        gender=data['gender']
                        ))

    # Closures
    def student_json_handler(file_path):
        # Demonstrating serialize and deserialize functions to a JSON file
        def serialize(student):
            """
            Serializes a Student object and writes it to a JSON file.

            Args:
                student (Student): The Student instance to serialize.
            """
            with open(file_path,'w') as f:
                json.dump(student.to_dict(),f)
                print(f"Student details serialized to JSON successfully in the file : \n{file_path}")

        def deserialize():
            """
            Deserializes a Student object from a JSON file.

            Returns:
                 Student: The deserialized Student object.
            """
            with open(file_path,'r') as f:
                data = json.load(f)
                student = Student.from_dict(data)
                print(f"Deserialized student details from : \n{file_path}")
            return student

        return serialize,deserialize

# Run the application
if __name__ == '__main__':
    # Example to create a student object, save then load it using the above closures
    student = Student("DS2005_S8", "Abigail Wilfred", date(2016,3,25), "Female")
    file_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'files','students.json'))
    os.makedirs(os.path.dirname(file_path), exist_ok=True) # Ensure the above directory is created to avoid errors
    serialize,deserialize = Student.student_json_handler(file_path)
    serialize(student) # Save the student details to the json file
    loaded_student = deserialize() # Read in the student's details from the json file
    # Display the loaded student's details
    print(f"Loaded student details : \n{loaded_student.name}, {loaded_student.birthdate}, {loaded_student.gender}")

# Code below is for working with multiple students

# # Import the required modules
# import json, os
# from datetime import date, datetime
#
# # Define a Student Class
# class Student:
#     def __init__(self, reg_no, name, birthdate, gender):
#         self.reg_no = reg_no
#         self.name = name
#         self.birthdate = birthdate
#         self.gender = gender
#
#     def to_dict(self):
#         return {
#             'reg_no': self.reg_no,
#             'name': self.name,
#             'birthdate': self.birthdate.isoformat(),
#             'gender': self.gender
#         }
#
#     @staticmethod
#     def from_dict(data):
#         return Student(
#             reg_no=data['reg_no'],
#             name=data['name'],
#             birthdate=datetime.strptime(data['birthdate'], '%Y-%m-%d').date(),
#             gender=data['gender']
#         )
#
# # Closures
# def student_json_handler(file_path):
#     """
#     Creates serialize and deserialize functions to handle Student objects.
#     Works with single Student or list of Students.
#     """
#
#     def serialise(students):
#         """
#         Serialises one or many Student objects into a JSON file.
#         """
#         # Normalize: always write a list
#         if isinstance(students, Student):
#             students = [students]
#
#         with open(file_path, 'w') as f:
#             json.dump([s.to_dict() for s in students], f, indent=4)
#
#         print(f"Saved {len(students)} student(s) to JSON file:\n{file_path}")
#
#     def deserialize():
#         """
#         Deserializes JSON data into a list of Student objects.
#         Returns a list (even if it only contains one).
#         """
#         with open(file_path, 'r') as f:
#             data = json.load(f)
#
#         # If file contained a single dict, wrap in list
#         if isinstance(data, dict):
#             data = [data]
#
#         students = [Student.from_dict(d) for d in data]
#         print(f"Loaded {len(students)} student(s) from JSON file:\n{file_path}")
#         return students
#
#     return serialize, deserialize
#
#
# # Run the application
# if __name__ == '__main__':
#     # Define multiple students
#     students = [
#         Student("DS2508_S9", "Victor Gikeno Kuria", date(2001, 10, 15), "Male"),
#         Student("DS2510_S3", "Jane Doe", date(2002, 5, 21), "Female"),
#         Student("DS2515_S7", "John Smith", date(2000, 12, 1), "Male")
#     ]
#
#     file_path = os.path.abspath(os.path.join(os.getcwd(), '..', 'files', 'students.json'))
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#     serialize, deserialize = student_json_handler(file_path)
#
#     # Save all students
#     serialise(students)
#
#     # Reload them
#     loaded_students = deserialize()
#
#     # Display
#     for s in loaded_students:
#         print(f"{s.reg_no} - {s.name}, {s.birthdate}, {s.gender}")