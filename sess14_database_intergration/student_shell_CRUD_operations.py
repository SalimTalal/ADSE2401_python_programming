# Python script to demonstrate MySQL database CRUD operations on the command line/shell
# NB: Ensure you've installed the mysql python connector => pip install mysql-connector-python

# ----------------------------
# Import the required modules
# ----------------------------
import mysql.connector
from db_conn import db_config
from student import Student

# ------------------------------------
# Database connection functions
# ------------------------------------
def connect_to_database():
    """Create and return a database connection."""
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to python232401 MySQL database!") # remove in production code
            return connection
    except mysql.connector.Error as err:
        print(f"Error: Unable to connect to MySQL database:\n{err}")
        return None

def close_connection(connection):
    """Close the database connection."""
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

# --------------------------------
# CRUD operations
# --------------------------------
def read_students(connection):
    """Fetch all students from the database."""
    students = []
    query = "SELECT * FROM student"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            students = [Student(*row) for row in rows]
    except mysql.connector.Error as err:
        print(f"Error: Unable to fetch student details:\n{err}")

    return  students

def insert_student(connection, student):
    """Insert/add a new student into the database"""
    query = """
        INSERT INTO student(StudentNO, Name, Birthdate, Gender, City)
        values (%s, %s, %s, %s, %s)
    """

    data = (
        student.student_no,
        student.name,
        student.birthdate,
        student.gender,
        student.city
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, data)
            connection.commit()
            return True
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Error: Unable to insert student into MySQL:\n{err}")
        return False

def update_student(connection, student):
    """Update/modify an existing student record details."""
    query = """
        UPDATE student
        SET Name=%s, Birthdate=%s, Gender=%s, City=%s
        WHERE StudentNO = %s
    """

    data = (
        student.name,
        student.birthdate,
        student.gender,
        student.city,
        student.student_no
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, data)
            connection.commit()
            return cursor.rowcount > 0
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Error: Unable to update student record details into MySQL:\n{err}")
        return False

def delete_student(connection, student_no):
    """Delete a student's record from the database."""
    query = "DELETE FROM student WHERE StudentNO=%s"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (student_no,)) # Fixed tuple bug
            connection.commit()
            return cursor.rowcount > 0
    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Error: Unable to delete student record into MySQL:\n{err}")
        return False

# --------------------------------------------------------
# Main script execution: Script to perform CRUD operations
# ---------------------------------------------------------

if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        # Create some student objects
        new_student1 = Student(
            'EICN_ADSE232401_S010',
            'Peter Njuguna',
            '1996-04-09',
            'M',
            'Githunguri'
        )
        dummy_student = Student(
            'EICN_ADSE232401_S011',
            'Some Dummy Student',
            '2010-08-11',
            'M',
            'Nyali'
        )

        # Insert example
        if insert_student(connection, new_student1):
            print(f"Student {new_student1.name} inserted successfully")
        if insert_student(connection, dummy_student):
            print(f"Student {dummy_student.name} inserted successfully")

        # Read example. Get all the students from the database
        students = read_students(connection)
        for student in students:
            print(student)

        # Update example
        new_student1.city = "Nairobi"
        if update_student(connection, new_student1):
            print(f"Student {new_student1.student_no} updated successfully")

        # Delete example
        if delete_student(connection, dummy_student.student_no):
            print(f"Student {dummy_student.student_no} deleted successfully")

        close_connection(connection)