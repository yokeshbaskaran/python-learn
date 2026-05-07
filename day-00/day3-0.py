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


# 1)Create a class called student. create a variable = name and register number using constructor. Create a function called display which should display the name and register number of the student
class Student:
    def __init__(self):
        self.name = "nthg"
        self.regno = "000"

    def printDetail(self):
        print("name:", self.name)
        print("reg number:", self.regno)


person1 = Student()
person1.name = "Rocky"
person1.regno = "CS01"
person1.printDetail()

person2 = Student()
person2.name = "singh"
person2.regno = "CS02"
person2.printDetail()

# 2)Create a class called Fruit. Create a variable called color using _init method. Create a object called apple "Pass the color variable as a parameter through object".


# Sample1
class fruit:
    def __init__(self):
        pass  # Nothing happens during object creation

    def printDetails(self):
        print("hi")


apple = fruit()
apple.printDetails()


# Example
class Fruit:
    # self -> refers to current Object ("apple") and col -> refers to variable from apple "yellow"
    def __init__(self, col):
        self.color = col


apple = Fruit("Yellow")
print(apple.color)

# 3)Create a class called teacher. Create a variable = name and register number using constructor. Create a function called display which should display the name and register number of the teacher. Create t1 and t2 object and pass the name and reg no value through object.


class Teacher:
    def __init__(self, name, reg):
        self.name = name
        self.reg = reg

    def display(self):
        print("name:", self.name)
        print("regs:", self.reg)


t1 = Teacher("krish", "12")
t1.display()
t2 = Teacher("manu", "10")
t2.display()

# 4)Create a class called calculator. Create 2 variables a and b. Create a function called add,sub,mul,div all functions should take 2 variables as parameter. I Pass the a and b value through object().


# Method1 = Best: Cleaner and reusable
class CalCulate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        return result

    def sub(self):
        result = self.a - self.b
        return result

    def mul(self):
        result = self.a * self.b
        return result

    def div(self):
        result = self.a / self.b
        return result


n1 = int(input("enter a:"))
n2 = int(input("enter b:"))
result = CalCulate(n1, n2)
print(result.add())
print(result.sub())
print(result.mul())
print(result.div())


# Method2 = Medium:Easy to understand and Must pass values every time
class CalCulate:
    def add(self, a, b):
        result = a + b
        return result


result = CalCulate()
print(result.add(1, 2))


# Method3 - ok:without constructor
class CalCulate:
    def add(self):
        return self.a + self.b


obj = CalCulate()

obj.a = int(input("enter a: "))
obj.b = int(input("enter b: "))

print(obj.add())
