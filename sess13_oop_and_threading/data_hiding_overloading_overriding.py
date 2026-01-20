# Python script to demonstrate OOP concepts of Data hiding, Overloading (simulation) and Overriding

# Define an animal class
class Animal:
    def __init__(self, name, age):
        self._name = name # Protected by convention
        self.__age = age # Private (name mangled to _Animal__age) # Truly private (name-mangled)

    def get_private_age(self):
        return self.__age # Access the private variable __age via a getter

    def speak(self):
        return f"{self._name} makes a sound"

    def make_sound(self,*args): # Simulate overloading with *args
        base_sound = self.speak()
        if not args:
            return base_sound
        elif len(args) == 1 and isinstance(args[0], (int, float)):
            volume = args[0]
            return f"{base_sound} at volume {volume}"
        else:
            extras = ', '.join(str(arg) for arg in args)
            return f"{base_sound} with extras: {extras}"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self): # Override the Animal's (parent class) speak method
        return f"{self._name} barks 'WOOF' loudly!"

# Instantiate a dog object and call the various methods
dog = Dog("Jimmy",5)
print(dog.speak()) # Overriding, the Animal's speak() method
print(dog.make_sound()) # Overloading simulation: no arguments passed
print(dog.make_sound(8)) # Overloading with volume argument
print(dog.make_sound(12,"with toy","excited")) # with extras
print(f"{dog._name}'s age {dog.get_private_age()} years.") # Data hiding: access via a getter
