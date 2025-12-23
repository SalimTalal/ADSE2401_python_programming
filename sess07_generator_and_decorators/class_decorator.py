# Python script/file to demonstrate decorating a class (using a logger function)

# Define the logger function
def log_dimensions(cls):
    def wrapper(*args, **kwargs):
        print(f"Logging dimensions of {cls}")
        rectangle = cls(*args, **kwargs)
        print(f"Rectangle dimensions logged!")
        return rectangle
    return wrapper

@log_dimensions
class Rectangle:
    def __init__(self,width = 0, length = 0):
        self.width = width
        self.length = length

    def get_length(self):
        return self.length
    def get_width(self):
        return self.width
    def set_length(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width
    def calculate_area(self):
        return self.width * self.length
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return(
            f"Rectangle's Dimensions"
            f"\n" + "-" * 45 +
            f"\nWidth: {self.width} cm."
            f"\nLength: {self.length} cm."
            f"\nArea: {self.calculate_area()} cm."
            f"\nPerimeter: {self.calculate_perimeter()} cm."
            f"\n" + "-" * 45
        )

# Prompt the user for the dimensions of a new Rectangle
length = int(input("Enter the length of rectangle in cm : \n"))
width = int(input("Enter the width of rectangle in cm : \n"))
# Create/instantiate a Rectangle object with the above dimensions
rectangle = Rectangle(length, width)
print(rectangle)

# Create/instantiate a rectangle using hard-coded values
rectangle2 = Rectangle(width = 8, length = 5)
print(rectangle2)