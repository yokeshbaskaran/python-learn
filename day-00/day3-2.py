# Inheritance in python
# - Inheritance in Python is a core concept of object-oriented programming (OOP).
# - It allows one class (child or derived class) to reuse and extend the properties and methods of another class (called parent or base class).

# Types of Inheritance
# 1. Single Inheritance: One child class inherits from one parent class.
# 2. Multiple Inheritance: One child class inherits from multiple parent classes.
# 3. Multi-level Inheritance:- Inheritance happens in levels (grandparent → parent → child).
# 4. Hierarchical Inheritance:- Multiple child classes inherit from one parent class.


# Examples
# 1. Single Inheritance
class Father:
    def phone(self):
        print("Pa phones")


class Son(Father):  # Single Inheritance
    def lap(self):
        print("Son laptop")


ramu = Son()
ramu.lap()
ramu.phone()


# 2. Mutliple Inheritance
class Father:
    def phone(self):
        print("Pa phones")


class Mother:
    def purse(self):
        print("Rs.100")


class Son(Father, Mother):  # Multiple Inheritance
    def lap(self):
        print("Son laptop")


ramu = Son()
ramu.lap()
ramu.phone()
ramu.purse()


# 3. multi-level inheritance
class Grand:
    def land(self):
        print("Lands")


class Father(Grand):
    pass


class Son(Father):
    pass


person = Son()
person.land()


# 4. Hierarchical Inheritance
class Dad:
    def home(self):
        print("Family Home!")


class Son(Dad):
    pass


class Daughter(Dad):
    pass


ram = Son()
dora = Daughter()

ram.home()
dora.home()
