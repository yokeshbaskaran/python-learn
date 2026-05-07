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
