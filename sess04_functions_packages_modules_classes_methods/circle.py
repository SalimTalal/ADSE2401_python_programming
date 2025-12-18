# Python file to define a Circle class

# Import the required modules
import math # Allows us to access the inbuit value of pi and pow() functions

class Circle:
    """
    A class to represent a geometric circle.

    Attributes:
    -----------
    radius (float): The radius of the circle in cm.

    Methods:
    ---------
     calc_area(self):
        Calculates & returns the area of the circle.

     calc_perimeter(self):
        Calculates & returns the perimeter of the circle.
     __str__(self):
        Returns a formatted string representing circle's dimensions.
    """

    def __init__(self, radius):
        """
        Initializes the Circle with a given radius.

        Parameters:
        -----------
        radius: float, default 0
            The radius of the circle in units (e.g. meters, cm, feet or inches).
        """
        self.radius = radius

    def calc_area(self):
        """
        Calculates the area of the circle.

        Returns:
        --------
        float
            The area of the circle using the formula πr²
        """
        # return math.pi * self.radius ** 2 # Same as below code
        return math.pi * math.pow(self.radius,2)

    def calc_perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
        ---------
        float
            The perimeter of the circle using the formula π(2r).
        """
        return math.pi * (2 * self.radius)

    def __str__(self): # dunder method works like toString() in Java or ToString() in C#
        """
        Returns a formatted string representing circle's dimensions.

        Returns:
        --------
        str
            A readable summary of the radius, area and circumference of the circle.
        """
        return (f"Circle's dimensions"
                f"\n" + "-" * 40 +
                f"\nRadius: {self.radius} cm."
                f"\nArea: {self.calc_area():.2f} cm^2."
                f"\nPerimeter: {self.calc_perimeter():.2f} cm."
                f"\n" + "-" * 40)

print(f"The documentation string of the calc_area() method is : \n{Circle(5).calc_area.__doc__}")
