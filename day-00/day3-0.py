# Classes and Objects
# - In Python, classes and objects are the foundation of object-oriented programming (OOP). They help you organize code by grouping data and behavior together.

# 🔹 What is a Class?
# - A class is like a blueprint or template for creating objects. It defines properties (variables) and behaviors (functions).

# 🔹 What is an Object?
# - An object is an instance of a class. It represents a real-world entity created from the class

# 🔹 Key Concepts :
# 3. Class = blueprint | Object = instance of class | Classes contain attributes and methods
# 1. Attributes (Variables) -> Store data about the object || Example: brand, color
# 2. Methods (Functions) -> Define behavior || Example: drive()


class trip:
    drink = ""

    def party(self):
        print("Party starts here!")

    def beach(self):
        print("Seeing sunsets")


ram = trip()
sam = trip()
ram.party()
ram.beach()
