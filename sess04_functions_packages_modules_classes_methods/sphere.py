# Python file to define a Sphere class

# Import the required modules
from circle import Circle

class Sphere(Circle):
    """
     A class that inherits from the Circle class to represent a geometric sphere.

     Attributes:
     -----------
     radius (float): The radius of the sphere in units (e.g. meters, cm, feet or inches).

     Methods:
     ---------
      calc_surface_area():
         Calculates & returns the surface area of the sphere.

      calc_volume():
         Calculates & returns the volume of the sphere.
      __str__():
         Returns a formatted string representing sphere's dimensions.
     """
    def __init__(self, radius):
        """
        Initializes the sphere with a given radius by calling the Circle's __init__()/constructor/method.

        Parameters:
        -----------
        radius: float, default 0
            The radius of the sphere in units (e.g. meters, cm, feet or inches).
        """
        super().__init__(radius)

    def calc_volume(self):
        """
        Calculates the volume of the sphere.

        Returns:
        --------
        float
            The volume of the sphere using the formula 4/3πr³
        """
        return 4.0/3.0 * self.calc_area() * self.radius

    def calc_surface_area(self):
        """
        Calculates the surface area of the sphere.

        Returns:
        --------
        float
            The surface area of the sphere using the formula 4πr²
        """
        return 4.0 * self.calc_area()

    def __str__(self): # dunder method works like toString() in Java or ToString() in C#
        """
        Returns a formatted string representing sphere's dimensions.

        Returns:
        --------
        str
            A readable summary of the radius, surface area and volume of the sphere.
        """
        return (f"Sphere's dimensions"
                f"\n" + "-" * 40 +
                f"\nRadius: {self.radius} cm."
                f"\nSurface Area: {self.calc_surface_area():.2f} cm^2."
                f"\nVolume: {self.calc_volume():.2f} cm^3."
                f"\n" + "-" * 40)