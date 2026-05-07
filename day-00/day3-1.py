# Types of Variables in Classes
# 1. Class Variable: shared by all objects of the class.
# 2. Instance Variable: unique for each object. the variables used in constructor are instance variables
# 3. Local Variable: exists only inside the method.


# Examples
class Phone:
    c_type = "C-type"  # class variable

    def __init__(self, brand, price):
        self.brand = brand  # instance variables
        self.price = price

    def display(self):
        result = self.brand + "" + self.price + "" + self.c_type  # local variable
        print(result, type(result))


Phone.c_type = "USB"
iphone = Phone("iphone", "60k")
iphone.display()

redmi = Phone("redmi", "11k")
redmi.display()

google = Phone("google", "18k")
google.display()


# Types of methods in Classes
# 1. ➡️ Instance methods modify or access object-specific data. -> Works with object (instance) data. -> Uses self
# 2. ➡️ Class methods modify or access class-wide data shared by all objects. -> Works with class-level data. Uses cls. -> Changes variables shared by all objects
# 3. ➡️ Static methods are utility methods that don’t use object or class data. -> Independent of object and class data. -> No self or cls.


class Laptop:
    chargertype = "C TYPE"

    def __init__(self):
        self.brand = ""
        self.price = 34

    def setPrice(self, price):
        # instance method
        self.price = price

    def getPrice(self):
        print(self.price)

    # class method
    @classmethod
    def setChargerType(cls):
        cls.chargertype = "USB"
        print("Changed type:")

    # static method
    @staticmethod
    def info():
        print("This is Lap class!")


hp = Laptop()
hp.getPrice()
hp.setPrice(56000)
hp.getPrice()
Laptop.setChargerType()
print(hp.chargertype)
hp.info()
