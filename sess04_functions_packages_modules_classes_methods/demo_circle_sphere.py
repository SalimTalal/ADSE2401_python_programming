# Python file/script to demonstrate working with user-defined/custom class and instantiating them.

# Import the required modules
from circle import Circle
from sphere import Sphere

# Prompt the user for the circle's radius
radius = int(input('Please enter the radius of the circle in cm:\n'))

# Create/instantiate a Circle object
circle1 = Circle(radius)

# Prompt the user for the sphere's radius
radius = int(input('Please enter the radius of the sphere in cm:\n'))

# Create/instantiate a Sphere object
sphere1 = Sphere(radius)

# Display the circle's & sphere's dimensions
print("\n")
print(circle1)
print("\n")
print(sphere1)