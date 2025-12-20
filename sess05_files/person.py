# Python file/script to define a Person class

class Person:
    """Represents a person."""
    def __init__(self, name, age):
        """
        Constructor for Person class.
        :param name(str): name of person.
        :param age(int): age of person.
        """
        self.name = name
        self.age = age