# Classes and Objects
# - In Python, classes and objects are the foundation of object-oriented programming (OOP). They help you organize code by grouping data and behavior together.

# 🔹 What is a Class?
# - A class is like a blueprint or template for creating objects. It defines properties (variables) and behaviors (functions).

# 🔹 What is an Object?
# - An object is an instance of a class. It represents a real-world entity created from the class

# 🔹 What is an constructor function?
#  - A constructor is a unique function that gets called automatically when an object is created of a class.

# 🔹 Key Concepts :
# 1. Class = blueprint | Object = instance of class | Classes contain attributes and methods
# 2. Attributes (Variables) -> Store data about the object || Example: brand, color
# 3. Methods (Functions) -> Define behavior || Example: drive()
# 4. self = refers to the current object and "self"  is NOT a keyword like if, for, while. But Python programmers always use self because it is the standard convention.
# You can technically write:
# def greet(me): and it still works.
# person.greet() -> Python secretly changes it into: Greeting.greet(person) where Greeting -> class, .greet() -> method and person -> object


# creating class
class Greeting:
    def greet():
        print("Hi, Greetings!")


Greeting.greet()


# creating class without methods
class Greeter:
    pass


# Classes and Objects - Examples
class trip:
    username = "enter name:"
    drink = ""

    def party(self):
        print("Party starts here!")

    def beach(self):
        print("Seeing sunsets")

    def personDrinks(self):
        print("slef:", self)


ram = trip()
sam = trip()

ram.username = "Ramu"
ram.drink = "yes"
print(ram.username, "drinks:", ram.drink)

sam.username = "Sammy"
sam.drink = "no"
print(sam.username, "drinks:", sam.drink)


# 1)Create a class called laptop and create a following variables and functions. Variables = > Price, Processor, Ram | Create Object HP, DELL, LENOVO


# without constructor
class laptop:
    processor = ""
    ram = ""
    price = ""

    def lapDetails(_, a, b, c):
        print(a, b, c)


hp = laptop()
dell = laptop()

hp.processor = "12"
hp.ram = "8GB"
hp.price = "56000"
hp.lapDetails(hp.processor, hp.price, hp.ram)

dell.processor = "11"
dell.ram = "16GB"
dell.price = "60000"
dell.lapDetails(dell.processor, dell.price, dell.ram)


# with constructor function
class Laptop:
    # constructor function, "self" refers to current object
    def __init__(self):
        self.price = 0
        self.ram = 0
        self.processor = 0

    def display(self):
        print(self.price, self.ram, self.processor)


# creating object - HP
hp = Laptop()
hp.processor = "12"
hp.ram = "8GB"
hp.price = "56000"
hp.display()

# creating object - DELL
dell = Laptop()
dell.processor = "11"
dell.ram = "16GB"
dell.price = "60000"
dell.display()
