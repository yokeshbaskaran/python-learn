# Super keyword in python
# - The super() keyword is used in inheritance.

# Examples:


class A:
    def __init__(self):
        print("A class")

    def display(self):
        print("inside class A")


# class B(A): # shows error when C(A,B)
class B:
    def __init__(self):
        super().__init__()  # gets constructor from class A
        # super().display()
        print("B class")

    def display(self):
        print("inside class B")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("C class")

    def display(self):
        print("inside class C")


print("---")
obj1 = A()
print("---")
obj2 = B()
print("---")
obj3 = C()
print("---")

# class C(B, A):  # prints B first becoz of order and, B is first mentioned in arguments and print first A before B becoz super() in Class B
# output:
# ---
# A class
# B class
# C class

# class C(A, B):  # prints A first becoz of order, A is first mentioned in arguments
# output:
# ---
# A class
# C class
